# Review manuscript

- Source: `co-speech-gesture-atlas.md`.
- Reading copy: `../output/pdf/co-speech-gesture-atlas.pdf` (five pages).
- Frozen evidence: `snapshot.json`, including data-file SHA-256 hashes, collection totals, application-audit results, and citation-analysis results.

The source is a review draft, not a preprint submission. Authorship and affiliations must be finalized by the project authors before submission. The manuscript uses the 12 October 2026 collection snapshot and the 3 October 2026 application audit. It describes associations, not causal effects. Corresponding-author information is not present in the schema.

Rebuild the reading copy with `python scripts/build_manuscript.py` after installing `reportlab` and `pypdf`. These are document-tool dependencies and are not needed to deploy the website. The renderer reads Markdown; `<!-- pagebreak -->` comments define the five-page layout.

Refresh the website summaries with `python scripts/build_site.py`; that also runs `scripts/analyze_citations.py`. Do not automatically update manuscript figures or claims when rebuilding the site. Revise the source and intentionally replace the frozen snapshot only when preparing a new manuscript version.

The citation analysis uses unique directed pairs in `data/citations.csv`, exact venue labels, recorded code links, and exact author names. Generation research excludes theory and theses. The code-link comparisons include all generation categories and stratify by publication cohorts; the author proxy uses strictly earlier recorded generation publications, not total career output. Graph incompleteness, date conflicts, source depth, author-name variants, and paper-role differences constrain interpretation.
