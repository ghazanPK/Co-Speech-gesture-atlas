# Co-Speech Gesture Atlas

A maintained, structured map of research on co-speech gesture generation: papers, datasets, metrics and code, with a comparison table per paper rather than a bare link.

> Status: scaffold. The paper tables below are generated from `data/papers/` and are not filled in yet.

## Scope

Included:
- Body and hand gesture generation that accompanies speech, from text, audio or both.
- Monologue, dyadic (speaker and listener) and multi-party settings.
- Face or holistic methods, when body gestures are part of the output.

Not included:
- Face-only or lip-sync-only methods.
- Text-to-motion without a speech context.
- Sign language production.

## Papers

*Generated section — do not edit by hand.*

| Year | Venue | Paper | Input | Output | Approach | Setting | Real-time | Dataset | Code | Open copy |
|---|---|---|---|---|---|---|---|---|---|---|

## Datasets

*To be filled from `data/datasets.yaml`.*

## Evaluation metrics

*To be filled from `data/metrics.yaml`.*

## Surveys and challenges

*To be filled.*

## Contributing

Add one record to `data/papers/<year>.yaml` following [docs/SCHEMA.md](docs/SCHEMA.md) and open a pull request. Inclusion rule: the work must be publicly identifiable (DOI, arXiv ID or proceedings page) and fall inside the scope above.

Check your record before opening the pull request:

```bash
pip install -r requirements.txt
python scripts/validate.py
```

## License

List content: CC0. Scripts: MIT.
