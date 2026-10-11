# Co-Speech Gesture Atlas: An Open, Living Map of Gesture Generation Research and Its Use

Review draft | 12 October 2026

## Abstract

Co-speech gesture research spans animation, embodied conversational agents, robotics, and the human sciences. Its literature is difficult to compare when bibliographic lists omit inputs, outputs, evaluation choices, and evidence of downstream use. We present Co-Speech Gesture Atlas, an open collection of structured publication, dataset, and metric records with a filterable explorer, citation graph, and evidence-linked application audit. The snapshot described here contains 2,690 publication records spanning 1965-2026: 619 generation-research records, 1,989 human gesture theory records, and 82 examined theses. It also describes 69 named datasets, 36 evaluation metrics, and 32,161 internal citation links. Two worked examples demonstrate analytical uses of the resource. An application audit identifies 57 distinct papers reporting functional interactive reuse of 17 method publications across 13 groups. A citation analysis finds that the ten most-cited generation-research records receive 20.9% of recorded citations to that subset. Code-link availability, publication venue, age, and prior author publication presence show descriptive associations of varying strength. These findings characterize the recorded collection rather than field-wide deployment, global citation impact, or causal influence. The atlas combines useful coverage with explicit provenance and correction mechanisms; most records still require independent verification.

**Keywords:** co-speech gesture; embodied agents; research atlas; application reuse; citation concentration; open research infrastructure.

## 1. Introduction

Generating gestures that accompany speech requires more than plausible motion. Systems may need to express semantic content, synchronize movement with speech, adapt to a speaker, and operate within an interactive application. Rule-based behavior planning, exemplified by BEAT [1], and learned multimodal generation, exemplified by Gesticulator [2], address this problem through different representations and assumptions. Benchmark initiatives such as GENEA provide shared evaluation conditions and emphasize the difficulty of comparing systems across datasets and embodiments [3].

A researcher entering this literature consequently faces several connected questions: which methods fit an intended input and embodiment, which datasets and metrics support comparison, which theoretical ideas motivate design, and which generators have been used beyond their original evaluation? A list of links is helpful for discovery but does not, by itself, organize the evidence needed to answer these questions.

Co-Speech Gesture Atlas [4] provides a maintained, inspectable map. Its contribution is the structured resource and the ability to connect its records, rather than a new gesture generator or a claim to exhaustive coverage. This manuscript describes its scope and data model, then uses application reuse and citation concentration as worked examples of findings that can be derived from it. The website presents an introduction and live summaries before directing readers to specialized exploration tools. The manuscript fixes one dated snapshot; later totals belong to the living resource.

<!-- pagebreak -->

## 2. Collection, provenance, and research interface

### 2.1 Scope and snapshot

The practical collection covers speech-associated body and hand gesture generation, including monologue, dyadic and multi-party settings. It includes methods, integrated systems, datasets, surveys, challenges and evaluation studies, and holistic or video-based generation when body or hand gesture is part of the output. The stated scope excludes sign-language production, face-only animation, and general text-to-motion work without a speech context. Public records are intended to represent published peer-reviewed work and examined theses; schema validation alone does not independently confirm publication status.

**Table 1. Collection snapshot, built 12 October 2026.** The latest paper-record addition is dated 3 October 2026; this is not a certified search cutoff. The three publication partitions below are mutually exclusive.

| Collection item | Count | Interpretation |
|---|---:|---|
| Publication records | 2,690 | All public paper records |
| Generation research | 619 | Non-theory records, excluding theses |
| Human gesture theory | 1,989 | Theory records, excluding theses |
| Examined theses | 82 | All records of type thesis |
| Named datasets | 69 | Excludes the custom-data placeholder |
| Evaluation metrics | 36 | Excludes the other-metric placeholder |
| Internal citation links | 32,161 | Unique directed edges between records |
| Records linking code | 77 | A link, not tested reproducibility |
| Independently verified records | 132 | Marked verified in the catalogue |

The theory collection is reference-derived: it follows literature cited by generation research rather than sampling all gesture studies independently. The broad chronological range therefore reflects both practical research and its intellectual background, not sixty years of a single generation paradigm.

### 2.2 Structured records and quality controls

Year-indexed YAML files contain stable paper identifiers, publication information, links, category, and reading provenance. Where supported by the source, records additionally describe input modalities, moving body regions, motion representation, generation approach, interaction setting, datasets, languages, metrics, user evaluation, code, and reported runtime. Dataset and metric registries provide shared identifiers and explanations. Required fields and allowed values are enforced by a JSON schema and cross-record validation. Missing values are retained rather than guessed.

The snapshot has 219 full-text-derived records (8.1%), 2,120 abstract-derived records (78.8%), and 351 metadata-derived records (13.0%). These categories describe extraction basis; they do not establish correctness. Independent verification is a separate flag: 132 records (4.9%) are marked verified. Automated assistance was used in collection and extraction. The current files do not constitute a complete, reproducible systematic-review search log or an inter-rater reliability study.

### 2.3 Interface and reuse

The browser explorer filters generation research, theory, theses, datasets and metrics, with filters encoded in shareable URLs. The citation view presents internal reference relationships. Application findings expose method-paper links with evidence and decision rationale. The data are released under CC0 and the public scripts under MIT. Thus users can inspect a displayed number, retrieve its underlying records, and adapt the analysis instead of treating the website as a closed summary.

<!-- pagebreak -->

## 3. Worked example: from methods to applications

### 3.1 Evidence model

The application audit asks whether an existing generator or behavior planner produced gestures in a separate application paper. It distinguishes functional interactive applications from animation comparisons, presentation or prepared-stimulus uses, platform integration, component-only reuse, candidates, and unresolved cases. An application purpose and technical reuse must be supported before a record contributes to the functional count. Author overlap is recorded but does not automatically establish or disqualify reuse.

Generation timing is a separate axis: online, prepared, or unknown. An interactive system can play precomputed utterance animations; a scripted presentation can use a runtime-capable generator. The audit therefore avoids equating interactivity with online inference or a presentation setting with an offline-only model. Runtime evidence can include whole-utterance generation and does not imply low-latency streaming.

### 3.2 Findings in the audited collection

The audit snapshot, dated 3 October 2026, contains 302 method-paper links connecting 59 method publications in 35 groups with 275 distinct paper identities. Functional interactive reuse is documented for 17 method publications across 13 groups in 57 distinct application papers. Thirteen functional papers have runtime evidence; three of those rely on explicitly labelled author clarification that is not independently verified. These are report counts, not independent deployed-system counts or counts of atlas users.

**Table 2. Selected method groups with functional interactive reuse.** Counts are deduplicated within groups. A paper may use multiple methods or occur in multiple groups, so rows cannot be added as independent deployments.

| Method group | Functional papers | Runtime | Prepared | Timing unknown |
|---|---:|---:|---:|---:|
| BEAT / REA | 32 | 6 | 6 | 20 |
| NVBG / Cerebella / USC ICT | 7 | 0 | 5 | 2 |
| WikiTalk | 6 | 0 | 0 | 6 |
| Ali / Hwang rule-map lineage | 3 | 3 | 0 | 0 |
| Tuyen / Chong / Celiktutan cGAN | 2 | 0 | 0 | 2 |
| Greta / Pelachaud | 1 | 0 | 0 | 1 |

The strongest recorded concentration is in BEAT/REA. Its 32 functional paper reports suggest a durable connection to application research, but their publication history and repeated reporting of systems limit comparison with newer generators. The Tinker museum guide illustrates why system identity matters: related reports can describe one system, not multiple deployments [5]. Learned methods also have supported application matches; the audit does not establish that only older pipelines are useful.

A related threshold analysis finds ten individual method publications with at least two counted downstream uses. Eight method groups contain at least one such publication; sixteen method publications in those groups have at least one counted use. This distinction prevents the misleading interpretation that all sixteen methods individually achieved repeated reuse. Adjacent uses enter this threshold, while unresolved, platform-only and component-only records do not.

### 3.3 What the example establishes

The audit demonstrates that a structured atlas can distinguish citation, implementation, application purpose, and timing. It identifies evidence worth following and gaps worth correcting. It does not estimate a field-wide adoption rate: candidate harvesting is incomplete, evidence depth varies, and method publications are neither unique algorithms nor an appropriate denominator for deployments. Claims about application success or user benefit require the underlying studies and their evaluation designs.

<!-- pagebreak -->

## 4. Worked example: citation concentration and associated factors

### 4.1 Measurement and concentration

We count unique directed edges in the public citation CSV. For a record, its internal citation count is the number of other recorded publications with an edge to it. These are within-atlas counts, not global scholarly citation counts. For generation research, we rank the 619 non-theory, non-thesis records by incoming edges and divide the top-ten total by all edges received by that subset. Incoming edges may originate anywhere in the atlas.

The ten leading generation-research records receive 1,531 of 7,325 incoming edges (20.9%), although they form only 1.6% of that subset. Across all 2,690 records, the corresponding top-ten share is 2,497 of 32,161 edges (7.76%). The difference shows why theoretical and generation literature should not be pooled without stating the denominator. The generation leaders include trimodal gesture generation (234), BEAT (205), Speech2Gesture (183), robot gesture learning (168), Gesticulator (142), and the BEAT dataset (131). Concentration spans method, system, and dataset roles rather than a single type of contribution.

### 4.2 Code availability, venue, and publication age

Among generation records, the 76 with a recorded code link have a median of 10 internal citations, versus 2 for the 543 without a recorded link. To reduce age mixing, Table 3 compares publication cohorts. The association persists in these cohorts, but their uneven code-link coverage, topic composition and publication ages preclude a causal code-release effect.

**Table 3. Internal citation medians by recorded code-link status.** Missing links mean no link is recorded, not that code is unavailable.

| Publication cohort | With code link: n | Median | No link recorded: n | Median |
|---|---:|---:|---:|---:|
| 2015-2019 | 4 | 58.5 | 58 | 4.5 |
| 2020-2022 | 25 | 22 | 90 | 5 |
| 2023-2026 | 47 | 5 | 239 | 0 |

Venue summaries use exact catalogue labels and include only labels with at least ten generation records. TOG has a median of 57 recorded citations (n=13), CVPR 13 (n=31), IVA 8.5 (n=38), and ICMI 6 (n=47). These groups differ in publication years, paper roles, code links, and reference coverage. Venue visibility, foundational status, reusable implementations and benchmark utility are plausible mechanisms for concentrated attention; these measurements do not identify which mechanism caused it or recommend a venue on that basis.

### 4.3 Author visibility and sensitivity checks

For 611 generation records with author names, an exploratory visibility proxy is the maximum number of strictly earlier generation publications recorded for any listed author. Exact name matching is used. Its Spearman rank correlation with incoming citations is 0.192 overall, but varies by cohort: -0.111 in 2015-2019 (n=59), -0.006 in 2020-2022 (n=114), and 0.178 in 2023-2026 (n=285). The weak, inconsistent pattern does not support a general claim of author influence. Corresponding-author influence is not assessed because the data do not identify that role; author order is not substituted for it.

Reference coverage is incomplete: 556 of 619 generation records have at least one recorded outgoing edge. There are also 238 edges whose recorded cited year exceeds the citing year. These may reflect publication/preprint timing, identity errors or date errors and remain visible for correction. Excluding them leaves the generation top-ten share at 20.95% (7,295 incoming edges). This sensitivity check supports stability to that exclusion, not correctness of the remaining graph or freedom from selection bias.

<!-- pagebreak -->

## 5. Discussion, maintenance, and limitations

The worked examples answer different questions. Citation concentration measures recorded attention to publications; the application audit measures supported reuse in separate paper reports. Neither substitutes for the other. A highly cited method can serve as a baseline, theoretical reference, or source of data without becoming an interactive application. Conversely, a planner embedded in a long-running application lineage may have substantial practical reuse that benchmark comparisons overlook. Preserving both relationships makes these differences inspectable.

The resource has several limitations. Its scope and reference expansion favor the literature reachable from the curated generation collection. Abstract and metadata extraction constrain field completeness; only a small fraction of records are independently verified. Citation harvesting is uneven, venue labels are not fully normalized, and author names are not disambiguated. Book, chapter and review identities can also complicate citation assignment. Application evidence varies from checked primary sources to citation contexts and author clarification. The present analyses are descriptive, with no causal design, significance claims, or claim to a complete census of the field.

A stronger study of citation mechanisms would need validated publication identities, systematic reference coverage, normalized venues, disambiguated authors and affiliations, explicit corresponding-author information, and a time-resolved citation history. It could then examine code-release timing, topic, publication age and paper role together. The present association between code links and citations supplies a hypothesis for that work, while the author-cohort results caution against a simple reputation explanation. We similarly avoid interpreting unknown application timing as absence of runtime generation.

The atlas is maintained through a public GitHub repository. Searches are currently manual; authors and readers can propose additions or corrections through pull requests. Validation and site generation precede automatic publication after an update to main. The landing page displays regenerated statistics and identifies snapshot and audit dates separately. This workflow supports incremental correction, but does not itself make a search exhaustive or a deployment timestamp a literature cutoff.

For citation of numerical claims, readers should specify the dated snapshot and record the source commit or archived release. This review draft uses paper data from source commit **8878e5f85511053c9ec32b14bcd86b5c69b9539d**, with analysis scripts accompanying the manuscript; input hashes are saved in the snapshot file. The permanent website and repository provide subsequent updates. A stable resource manuscript can remain useful while the collection grows, with substantial methodological or analytical changes reserved for future manuscript versions.

## 6. Conclusion

Co-Speech Gesture Atlas organizes a dispersed literature into an open, inspectable resource connecting generation research, gesture theory, datasets, metrics and application evidence. Its application audit and citation analysis demonstrate how structured records can support findings beyond paper discovery. The principal value is traceability: users can examine the evidence, distinguish missing information from negative findings, and improve the map through explicit corrections.

## References

[1] Cassell, J., Vilhjalmsson, H. H., and Bickmore, T. (2001). BEAT: The Behavior Expression Animation Toolkit. SIGGRAPH. [doi:10.1145/383259.383315](https://doi.org/10.1145/383259.383315).

[2] Kucherenko, T., et al. (2020). Gesticulator: A framework for semantically-aware speech-driven gesture generation. ICMI. [doi:10.1145/3382507.3418815](https://doi.org/10.1145/3382507.3418815).

[3] Kucherenko, T., et al. (2023). The GENEA Challenge 2023: A large-scale evaluation of gesture generation models in monadic and dyadic settings. ICMI. [Open manuscript](https://arxiv.org/abs/2308.12646).

[4] Co-Speech Gesture Atlas (2026). [Research website](https://co-speech-gesture-atlas.github.io/) and [source repository](https://github.com/ghazanPK/Co-Speech-gesture-atlas). Collection and analysis snapshot: 12 October 2026; application audit: 3 October 2026.

[5] Bickmore, T., et al. (2013). Tinker: a relational agent museum guide. Autonomous Agents and Multi-Agent Systems. [doi:10.1007/s10458-012-9216-7](https://doi.org/10.1007/s10458-012-9216-7).
