# Record schema

The data lives in three places:

| File | One record per |
|---|---|
| `data/papers/<year>.yaml` | paper, filed under its publication year |
| `data/datasets.yaml` | dataset |
| `data/metrics.yaml` | objective evaluation metric |

`schema/schema.json` is the enforced definition. `scripts/validate.py` checks every record against it, plus the cross-file rules at the end of this page.

## Paper

Fields marked **always** are required on every record. Fields marked **verified** are required once `verified: true` on a `method` record. Everything else is optional; leave a field out rather than guess.

| Field | Required | Value |
|---|---|---|
| `id` | always | First author's family name, year, one keyword: `ali2025ridge`. Lowercase letters and digits only. |
| `title` | always | Exact published title. |
| `authors` | verified | List, in published order. |
| `year` | always | Publication year. Must match the file name. |
| `venue` | always | Short venue name: `SIGGRAPH`, `CVPR`, `ICMI`, `CAVW`, `arXiv`. |
| `type` | always | `journal`, `conference`, `workshop`, `poster`, `preprint`, `thesis` |
| `category` | always | `method`, `dataset`, `survey`, `challenge`, `evaluation`, `system` |
| `doi` | one identifier | Bare DOI, `10.1002/cav.70034`. |
| `arxiv` | one identifier | Bare identifier in quotes, `"2303.09119"`, no version suffix. |
| `links.paper` | one identifier | Publisher or proceedings page. |
| `links.open` | | Free full text when `links.paper` is paywalled. |
| `links.code` | | Repository. |
| `links.project` | | Project page. |
| `links.video` | | Demo video. |
| `weights` | | `true` or `false`: are trained weights released. Only with `links.code`. |
| `input` | verified | List of `text`, `audio`, `speaker-id`, `style`, `emotion`, `seed-motion`, `image`, `video`, `interlocutor` |
| `output` | verified | List of `upper-body`, `full-body`, `hands`, `face`, `locomotion` |
| `representation` | verified | List of `keypoints-2d`, `joints-3d`, `smpl-x`, `video-pixels`, `other` |
| `approach` | verified | List of `rule-based`, `retrieval`, `regression`, `vae`, `gan`, `normalizing-flow`, `vq`, `autoregressive`, `masked-modeling`, `diffusion`, `flow-matching`, `llm`, `hybrid`, `other` |
| `setting` | verified | List of `monologue`, `dyadic`, `multi-party` |
| `realtime` | verified | `real-time`, `offline` or `unreported`. Use `real-time` only when the paper reports a speed or latency figure. |
| `latency` | | Free text as reported, e.g. `"45 fps on an RTX 3090"`. |
| `datasets` | verified | List of ids from `data/datasets.yaml`. |
| `languages` | verified | Spoken languages covered, ISO 639-1: `[en, ko]`. |
| `metrics` | verified | List of ids from `data/metrics.yaml`. |
| `user_study` | verified | `true` or `false`: does the paper report a human evaluation. |
| `summary` | verified | One plain sentence saying what the method does. 300 characters at most. |
| `notes` | | Anything a reader should know that has no field. |
| `added` | always | Date the record was added, quoted: `"2026-10-02"`. |
| `verified` | always | `true` once every field has been checked against the paper itself. |

At least one of `doi`, `arxiv` or `links.paper` must be present.

### Choosing values

- **`category`**: `method` proposes a generation model. `system` describes an integrated agent or application built on existing methods. `evaluation` studies metrics or evaluation practice.
- **`output` and `representation`** answer different questions: which parts of the body move, and in what form the motion is produced. A model that renders video frames directly is `representation: [video-pixels]`.
- **`approach`** lists every technique that matters to how the method generates motion. A VQ tokenizer with a diffusion prior is `[vq, diffusion]`. Use `hybrid` when learned and non-learned components are combined.
- **`interlocutor`** as an input means the model conditions on the other speaker's speech or motion.
- **Preprint later published**: keep one record. Set `venue`, `type` and `year` to the published version, move the record to that year's file, and keep the `arxiv` identifier.

## Dataset

| Field | Required | Value |
|---|---|---|
| `id` | always | Lowercase slug: `beat2`, `ted-gesture`. |
| `name` | always | Name as used in the literature. |
| `year` | verified | Release year. |
| `paper` | | `id` of the paper record that introduced it. |
| `links.page`, `links.download`, `links.paper` | verified (at least `links`) | URLs. |
| `modalities` | verified | List of `audio`, `text`, `video`, `body-motion`, `hand-motion`, `face-motion`, `annotations` |
| `capture` | verified | `mocap`, `pose-estimation`, `synthetic`, `mixed` |
| `representation` | | Same values as on papers. |
| `hours` | | Total duration in hours. |
| `speakers` | | Number of speakers. |
| `languages` | verified | ISO 639-1 codes. |
| `setting` | verified | List of `monologue`, `dyadic`, `multi-party` |
| `access` | verified | `open`, `on-request`, `unavailable` |
| `license` | | As stated by the authors. |
| `summary` | verified | One plain sentence. |
| `notes` | | Free text. |
| `added`, `verified` | always | As on papers. |

## Metric

| Field | Required | Value |
|---|---|---|
| `id` | always | Lowercase slug: `fgd`, `beat-align`. |
| `name` | always | Full name. |
| `aka` | | Other names and abbreviations in use. |
| `measures` | verified | `realism`, `synchrony`, `diversity`, `semantics`, `accuracy`, `smoothness`, `other` |
| `better` | verified | `higher`, `lower`, `closer-to-reference` |
| `paper` | | `id` of the paper record that introduced it, if in scope. |
| `links.paper`, `links.code` | | URLs. |
| `summary` | verified | One plain sentence saying what it computes. |
| `caveats` | | Known weaknesses, e.g. dependence on the feature extractor. |
| `added`, `verified` | always | As on papers. |

## Cross-file rules

- Paper `id`s are unique across all year files; dataset and metric `id`s are unique within their file.
- No two papers share a DOI, an arXiv identifier or a title.
- A paper's `year` matches the file it is in.
- Every id in a paper's `datasets` and `metrics` exists in the corresponding file.
- Every `paper` reference on a dataset or metric points to an existing paper record.

## YAML pitfalls

- Quote dates and arXiv identifiers: `"2026-10-02"`, `"2303.09119"`. Unquoted, YAML reads them as a date and a number.
- Quote titles and summaries that contain a colon.
