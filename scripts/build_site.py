#!/usr/bin/env python3
"""Export the data for the filterable site in docs/ and draw the papers-per-year chart.

Usage: python scripts/build_site.py
Writes docs/data.json (read by docs/index.html) and docs/papers-per-year.svg (shown in the README).
"""

import datetime
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate import DATA, ROOT, Loader  # noqa: E402
from build_applications import main as build_applications  # noqa: E402

DOCS = ROOT / "docs"
FIELDS = ["id", "title", "authors", "year", "venue", "type", "category", "area", "doi", "arxiv", "links", "weights", "input",
          "output", "representation", "approach", "setting", "realtime", "latency", "datasets", "languages", "metrics",
          "user_study", "summary", "notes", "checked", "verified"]


def load(path):
    return yaml.load(path.read_text(encoding="utf-8"), Loader=Loader) or []


def chart(papers):
    """Stacked bars per year: generation work (including theses) and theory."""
    years = sorted({p["year"] for p in papers})
    if not years:
        return
    lo, hi = max(min(years), 1985), max(years)
    gen = {y: 0 for y in range(lo, hi + 1)}
    theory = dict(gen)
    before = [0, 0]
    for p in papers:
        bucket = theory if p["category"] == "theory" else gen
        if p["year"] < lo:
            before[0 if bucket is gen else 1] += 1
        else:
            bucket[p["year"]] += 1
    cols = [(f"&lt;{lo}", before[0], before[1])] + [(str(y), gen[y], theory[y]) for y in range(lo, hi + 1)]
    top = max(g + t for _, g, t in cols) or 1
    w, h, left, bottom, gap = 960, 300, 44, 46, 3
    bar = (w - left - 10) / len(cols) - gap
    scale = (h - bottom - 24) / top
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family="system-ui, sans-serif" font-size="12">',
           '<style>.g{fill:#2a6f97}.t{fill:#c9a227}text{fill:#6b7280}@media (prefers-color-scheme: dark){text{fill:#9aa1ad}}</style>',
           f'<text x="{left}" y="16" font-size="13">Papers in the atlas by publication year</text>',
           f'<rect x="{w - 250}" y="6" width="12" height="12" class="g"/><text x="{w - 234}" y="17">generation (incl. theses)</text>',
           f'<rect x="{w - 90}" y="6" width="12" height="12" class="t"/><text x="{w - 74}" y="17">theory</text>']
    for i, (label, g, t) in enumerate(cols):
        x = left + i * (bar + gap)
        y0 = h - bottom
        if t:
            out.append(f'<rect x="{x:.1f}" y="{y0 - t * scale:.1f}" width="{bar:.1f}" height="{t * scale:.1f}" class="t"><title>{label}: {t} theory</title></rect>')
        if g:
            out.append(f'<rect x="{x:.1f}" y="{y0 - (t + g) * scale:.1f}" width="{bar:.1f}" height="{g * scale:.1f}" class="g"><title>{label}: {g} generation</title></rect>')
        if label.startswith("&lt;") or int(label) % 5 == 0:
            out.append(f'<text x="{x + bar / 2:.1f}" y="{h - bottom + 16}" text-anchor="middle">{label}</text>')
    for v in range(0, top + 1, 50 if top > 150 else 20):
        y = h - bottom - v * scale
        out.append(f'<text x="{left - 6}" y="{y + 4:.1f}" text-anchor="end">{v}</text>')
        out.append(f'<line x1="{left}" y1="{y:.1f}" x2="{w - 10}" y2="{y:.1f}" stroke="#9ca3af" stroke-opacity="0.25"/>')
    out.append("</svg>")
    (DOCS / "papers-per-year.svg").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")


def main():
    papers = [p for path in sorted((DATA / "papers").glob("*.yaml")) for p in load(path)]
    datasets, metrics = load(DATA / "datasets.yaml"), load(DATA / "metrics.yaml")
    edges = (ROOT / "data" / "citations.csv").read_text(encoding="utf-8").count("\n") - 1 if (ROOT / "data" / "citations.csv").exists() else 0
    cited = {}
    if edges > 0:
        for line in (ROOT / "data" / "citations.csv").read_text(encoding="utf-8").split("\n")[1:]:
            if "," in line:
                cited[line.split(",")[1]] = cited.get(line.split(",")[1], 0) + 1
    rows = []
    for p in papers:
        row = {k: p[k] for k in FIELDS if k in p}
        row["cited"] = cited.get(p["id"], 0)
        rows.append(row)
    data = {
        "generated": datetime.date.today().isoformat(),
        "papers": rows,
        "datasets": datasets,
        "metrics": metrics,
        "citations": edges,
    }
    (DOCS / "data.json").write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    chart(papers)
    print(f"docs/data.json: {len(rows)} papers, {len(datasets)} datasets, {len(metrics)} metrics; chart written.")
    if build_applications():
        raise SystemExit(1)


if __name__ == "__main__":
    main()
