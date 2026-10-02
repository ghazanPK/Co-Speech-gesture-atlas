# Co-Speech Gesture Atlas

A maintained, structured map of research on co-speech gesture generation: papers, datasets, metrics and code, with a comparison row per paper rather than a bare link.

<!-- BEGIN:stats -->
<!-- END:stats -->

## Contents

- [Scope](#scope)
- [How to read the tables](#how-to-read-the-tables)
- [Papers](#papers)
- [Surveys, challenges and evaluation studies](#surveys-challenges-and-evaluation-studies)
- [Dataset papers](#dataset-papers)
- [Datasets](#datasets)
- [Evaluation metrics](#evaluation-metrics)
- [Contributing](#contributing)

## Scope

Included:
- Body and hand gesture generation that accompanies speech, from text, audio or both.
- Monologue, dyadic (speaker and listener) and multi-party settings.
- Face or holistic methods, and co-speech video generation, when body gestures are part of the output.
- Datasets, surveys, challenges, evaluation studies and integrated systems on the above.

Not included:
- Face-only or lip-sync-only methods.
- Text-to-motion without a speech context.
- Sign language production.

## How to read the tables

Every row is generated from a record in [`data/`](data/); the records hold more fields than the tables show (motion representation, datasets, languages, metrics, user study, real-time claims, a one-sentence summary). The fields and their allowed values are defined in [docs/SCHEMA.md](docs/SCHEMA.md).

- No mark: the record was filled from the paper's full text.
- **†** The full text was not freely accessible, so the record was filled from the abstract only. Empty cells mean the abstract does not say.
- **‡** Only bibliographic metadata was available. The paper is listed so the map is complete, but its row is not filled in.

Most records were extracted with automated assistance and are marked `verified: false` in the data until confirmed by a second independent reading. If you spot an error, a correction by pull request or issue is welcome.

## Papers

Methods and systems, newest first, ordered by venue within each year.

<!-- BEGIN:papers -->
<!-- END:papers -->

## Surveys, challenges and evaluation studies

<!-- BEGIN:surveys -->
<!-- END:surveys -->

## Dataset papers

Papers whose main contribution is a dataset. The datasets themselves are compared in the next section.

<!-- BEGIN:dataset-papers -->
<!-- END:dataset-papers -->

## Datasets

<!-- BEGIN:datasets -->
<!-- END:datasets -->

## Evaluation metrics

Objective metrics reported by the papers above. Human evaluation is recorded per paper in the `user_study` field.

<!-- BEGIN:metrics -->
<!-- END:metrics -->

## Contributing

Add one record to `data/papers/<year>.yaml` following [docs/SCHEMA.md](docs/SCHEMA.md) and open a pull request. Inclusion rule: the work must be publicly identifiable (DOI, arXiv ID or proceedings page) and fall inside the scope above.

Check your record and regenerate the tables before opening the pull request:

```bash
pip install -r requirements.txt
python scripts/validate.py
python scripts/build_readme.py
```

## License

List content: CC0. Scripts: MIT.
