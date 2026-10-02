#!/usr/bin/env python3
"""Validate the data files against schema/schema.json and the cross-file rules.

Usage: python scripts/validate.py
Exits with status 1 and prints one line per problem if anything is wrong.
"""

import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


class Loader(yaml.SafeLoader):
    """SafeLoader that leaves dates as strings, so the schema sees what was typed."""


Loader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for tag, regexp in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def load_records(path, errors):
    """Return the list of records in a YAML file, or [] after reporting why not."""
    rel = path.relative_to(ROOT).as_posix()
    try:
        content = yaml.load(path.read_text(encoding="utf-8"), Loader=Loader)
    except yaml.YAMLError as exc:
        errors.append(f"{rel}: not valid YAML: {exc}")
        return []
    if content is None:
        return []
    if not isinstance(content, list):
        errors.append(f"{rel}: top level must be a list of records")
        return []
    return content


def check_schema(records, kind, rel, defs, errors):
    validator = Draft202012Validator({"$defs": defs, "$ref": f"#/$defs/{kind}"})
    for index, record in enumerate(records):
        label = record.get("id", f"record {index + 1}") if isinstance(record, dict) else f"record {index + 1}"
        for error in sorted(validator.iter_errors(record), key=lambda e: list(e.absolute_path)):
            field = ".".join(str(part) for part in error.absolute_path)
            where = f"{rel}: {label}" + (f": {field}" if field else "")
            # anyOf failures print the whole record; the only anyOf is the identifier rule
            message = "needs at least one of doi, arxiv or links.paper" if error.validator == "anyOf" else error.message
            errors.append(f"{where}: {message}")


def check_unique(entries, what, errors):
    """entries: iterable of (value, location). Report every value seen more than once."""
    seen = {}
    for value, location in entries:
        if value in seen:
            errors.append(f"{location}: duplicate {what} (also at {seen[value]})")
        else:
            seen[value] = location


def normalise_title(title):
    return re.sub(r"[^a-z0-9]", "", title.lower())


def main():
    errors = []
    defs = json.loads((ROOT / "schema" / "schema.json").read_text(encoding="utf-8"))["$defs"]

    papers = []  # (record, location)
    for path in sorted((DATA / "papers").glob("*.yaml")):
        rel = path.relative_to(ROOT).as_posix()
        if not re.fullmatch(r"\d{4}", path.stem):
            errors.append(f"{rel}: file name must be a four-digit year")
            continue
        records = load_records(path, errors)
        check_schema(records, "paper", rel, defs, errors)
        for record in records:
            if not isinstance(record, dict):
                continue
            location = f"{rel}: {record.get('id', '?')}"
            papers.append((record, location))
            if record.get("year") != int(path.stem):
                errors.append(f"{location}: year {record.get('year')} does not match the file name")

    datasets = load_records(DATA / "datasets.yaml", errors)
    check_schema(datasets, "dataset", "data/datasets.yaml", defs, errors)
    metrics = load_records(DATA / "metrics.yaml", errors)
    check_schema(metrics, "metric", "data/metrics.yaml", defs, errors)
    datasets = [r for r in datasets if isinstance(r, dict)]
    metrics = [r for r in metrics if isinstance(r, dict)]

    check_unique(((r["id"], loc) for r, loc in papers if "id" in r), "id", errors)
    check_unique(((r["doi"].lower(), loc) for r, loc in papers if isinstance(r.get("doi"), str)), "doi", errors)
    check_unique(((r["arxiv"], loc) for r, loc in papers if isinstance(r.get("arxiv"), str)), "arxiv id", errors)
    check_unique(
        ((normalise_title(r["title"]), loc) for r, loc in papers if isinstance(r.get("title"), str)),
        "title",
        errors,
    )
    check_unique(((r.get("id"), f"data/datasets.yaml: {r.get('id')}") for r in datasets), "id", errors)
    check_unique(((r.get("id"), f"data/metrics.yaml: {r.get('id')}") for r in metrics), "id", errors)

    paper_ids = {r.get("id") for r, _ in papers}
    dataset_ids = {r.get("id") for r in datasets}
    metric_ids = {r.get("id") for r in metrics}

    for record, location in papers:
        for field, known, target in (("datasets", dataset_ids, "data/datasets.yaml"), ("metrics", metric_ids, "data/metrics.yaml")):
            values = record.get(field)
            for value in values if isinstance(values, list) else []:
                if value not in known:
                    errors.append(f"{location}: {field}: '{value}' is not an id in {target}")

    for rel, records in (("data/datasets.yaml", datasets), ("data/metrics.yaml", metrics)):
        for record in records:
            if "paper" in record and record["paper"] not in paper_ids:
                errors.append(f"{rel}: {record.get('id')}: paper: '{record['paper']}' is not a paper id")

    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} problem(s) found.")
        return 1

    verified = sum(1 for r, _ in papers if r.get("verified") is True)
    print(f"OK: {len(papers)} papers ({verified} verified), {len(datasets)} datasets, {len(metrics)} metrics.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
