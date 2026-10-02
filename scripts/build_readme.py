#!/usr/bin/env python3
"""Regenerate the tables in README.md from the data files.

Usage: python scripts/build_readme.py [--check]
Replaces the text between <!-- BEGIN:name --> and <!-- END:name --> markers.
With --check, exits with status 1 if README.md is out of date and changes nothing.
"""

import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate import DATA, ROOT, Loader  # noqa: E402

README = ROOT / "README.md"
MARKS = {"abstract": "†", "metadata": "‡"}


def load(path):
    return yaml.load(path.read_text(encoding="utf-8"), Loader=Loader) or []


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def tags(values):
    return ", ".join(values) if values else ""


def paper_link(p):
    links = p.get("links") or {}
    url = links.get("paper")
    if not url and p.get("doi"):
        url = f"https://doi.org/{p['doi']}"
    if not url and p.get("arxiv"):
        url = f"https://arxiv.org/abs/{p['arxiv']}"
    title = cell(p["title"])
    text = f"[{title}]({url})" if url else title
    extra = []
    open_url = links.get("open") or (f"https://arxiv.org/abs/{p['arxiv']}" if p.get("arxiv") and "arxiv.org" not in (url or "") else None)
    if open_url and open_url != url:
        extra.append(f"[open copy]({open_url})")
    if links.get("project"):
        extra.append(f"[project]({links['project']})")
    if links.get("video"):
        extra.append(f"[video]({links['video']})")
    mark = MARKS.get(p.get("checked"), "")
    return text + mark + (" · " + " · ".join(extra) if extra else "")


def code_cell(p):
    code = (p.get("links") or {}).get("code")
    if not code:
        return ""
    return f"[code]({code})" + (" + weights" if p.get("weights") else "")


def table(header, rows):
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    lines += ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join(lines)


def venue_key(p):
    return (p["venue"].lower(), p["title"].lower())


def build_papers(papers):
    methods = [p for p in papers if p["category"] in ("method", "system")]
    out = []
    for year in sorted({p["year"] for p in methods}, reverse=True):
        group = sorted((p for p in methods if p["year"] == year), key=venue_key)
        rows = [[cell(p["venue"]), paper_link(p), tags(p.get("input")), tags(p.get("output")), tags(p.get("approach")),
                 tags(p.get("setting")), code_cell(p)] for p in group]
        out.append(f"### {year}\n\n" + table(["Venue", "Paper", "Input", "Output", "Approach", "Setting", "Code"], rows))
    return "\n\n".join(out) if out else "*No records yet.*"


def build_other(papers, categories):
    group = sorted((p for p in papers if p["category"] in categories), key=lambda p: (-p["year"], venue_key(p)))
    if not group:
        return "*No records yet.*"
    rows = [[str(p["year"]), cell(p["venue"]), p["category"], paper_link(p), cell(p.get("summary", ""))] for p in group]
    return table(["Year", "Venue", "Kind", "Paper", "Summary"], rows)


def build_datasets(datasets, papers):
    by_id = {p["id"]: p for p in papers}
    usage = {}
    for p in papers:
        for d in p.get("datasets") or []:
            usage[d] = usage.get(d, 0) + 1
    rows = []
    for d in sorted(datasets, key=lambda d: (-usage.get(d["id"], 0), d["name"].lower())):
        if d["id"] == "custom":
            continue
        links = d.get("links") or {}
        url = links.get("page") or links.get("download") or links.get("paper")
        if not url and d.get("paper") in by_id:
            url = re.search(r"\((.*?)\)", paper_link(by_id[d["paper"]]) + "()").group(1) or None
        name = f"[{cell(d['name'])}]({url})" if url else cell(d["name"])
        rows.append([name, str(d.get("year", "")), tags(d.get("modalities")), d.get("capture", ""),
                     str(d.get("hours", "")), tags(d.get("languages")), tags(d.get("setting")), d.get("access", ""),
                     str(usage.get(d["id"], 0))])
    if not rows:
        return "*No records yet.*"
    return table(["Dataset", "Year", "Modalities", "Capture", "Hours", "Languages", "Setting", "Access", "Papers here using it"], rows)


def build_metrics(metrics, papers):
    usage = {}
    for p in papers:
        for m in p.get("metrics") or []:
            usage[m] = usage.get(m, 0) + 1
    rows = []
    for m in sorted(metrics, key=lambda m: (-usage.get(m["id"], 0), m["name"].lower())):
        if m["id"] == "other":
            continue
        rows.append([cell(m["name"]), tags(m.get("aka")), m.get("measures", ""), m.get("better", ""),
                     cell(m.get("summary", "")), str(usage.get(m["id"], 0))])
    if not rows:
        return "*No records yet.*"
    return table(["Metric", "Also written", "Measures", "Better", "What it computes", "Papers here using it"], rows)


def build_theory(papers):
    group = sorted((p for p in papers if p["category"] == "theory"), key=lambda p: (p["year"], p["title"].lower()))
    if not group:
        return "*No records yet.*"
    out = []
    for start in sorted({p["year"] // 10 * 10 for p in group}):
        rows = [[str(p["year"]), p.get("area", ""), paper_link(p), cell(p["venue"])] for p in group if p["year"] // 10 * 10 == start]
        out.append(f"## {start}s\n\n" + table(["Year", "Area", "Paper", "Venue"], rows))
    return "\n\n".join(out)


def build_stats(papers, datasets, metrics):
    theory = sum(1 for p in papers if p["category"] == "theory")
    counts = f"**{len(papers) - theory} papers on gesture generation** and **{theory} on gesture theory**"
    full = sum(1 for p in papers if p.get("checked") == "full-text")
    abstract = sum(1 for p in papers if p.get("checked") == "abstract")
    meta = sum(1 for p in papers if p.get("checked") == "metadata")
    verified = sum(1 for p in papers if p.get("verified"))
    years = [p["year"] for p in papers]
    span = f"{min(years)}–{max(years)}" if years else "none"
    return (f"{counts} ({span}), {len([d for d in datasets if d['id'] != 'custom'])} datasets, "
            f"{len([m for m in metrics if m['id'] != 'other'])} metrics. "
            f"{full} records were filled from the full text, {abstract} from the abstract only (†), "
            f"{meta} from bibliographic metadata only (‡). {verified} have been independently verified.")


def main():
    papers = [p for path in sorted((DATA / "papers").glob("*.yaml")) for p in load(path)]
    datasets, metrics = load(DATA / "datasets.yaml"), load(DATA / "metrics.yaml")
    blocks = {
        "stats": build_stats(papers, datasets, metrics),
        "papers": build_papers(papers),
        "surveys": build_other(papers, ("survey", "challenge", "evaluation")),
        "dataset-papers": build_other(papers, ("dataset",)),
        "datasets": build_datasets(datasets, papers),
        "metrics": build_metrics(metrics, papers),
    }
    status = 0
    for path, names in ((README, list(blocks)), (ROOT / "THEORY.md", ["theory"])):
        text = old = path.read_text(encoding="utf-8")
        for name in names:
            body = blocks[name] if name in blocks else build_theory(papers)
            pattern = re.compile(rf"(<!-- BEGIN:{name} -->\n).*?(<!-- END:{name} -->)", re.S)
            if not pattern.search(text):
                print(f"{path.name} has no {name} markers")
                return 1
            text = pattern.sub(lambda m: m.group(1) + body + "\n" + m.group(2), text)
        if text == old:
            print(f"{path.name} is up to date.")
        elif "--check" in sys.argv:
            print(f"{path.name} is out of date; run python scripts/build_readme.py")
            status = 1
        else:
            path.write_text(text, encoding="utf-8", newline="\n")
            print(f"{path.name} updated.")
    return status


if __name__ == "__main__":
    sys.exit(main())
