# Co-Speech Gesture Atlas

A maintained, structured map of research on co-speech gesture generation: papers, datasets, metrics and code, with a comparison row per paper rather than a bare link.

<!-- BEGIN:stats -->
**621 papers on gesture generation**, **2001 on gesture theory** and **82 theses** (1965–2026), 69 datasets, 36 metrics. 219 records were filled from the full text, 2121 from the abstract only (†), 364 from bibliographic metadata only (‡). 132 have been independently verified.
<!-- END:stats -->

## Contents

- [Scope](#scope)
- [How to read the tables](#how-to-read-the-tables)
- [Papers](#papers)
- [Surveys, challenges and evaluation studies](#surveys-challenges-and-evaluation-studies)
- [Dataset papers](#dataset-papers)
- [Theses](#theses)
- [Datasets](#datasets)
- [Evaluation metrics](#evaluation-metrics)
- [Contributing](#contributing)

Elsewhere:
- [Gesture theory](THEORY.md): studies of human gesture (psychology, linguistics, neuroscience) that the generation work builds on.
- [Citation graph](docs/citations.html): which papers in the atlas cite which. Edge list in [`data/citations.csv`](data/citations.csv).

## Scope

Included:
- Body and hand gesture generation that accompanies speech, from text, audio or both.
- Monologue, dyadic (speaker and listener) and multi-party settings.
- Face or holistic methods, and co-speech video generation, when body gestures are part of the output.
- Datasets, surveys, challenges, evaluation studies and integrated systems on the above.

Not included:
- Face-only or lip-sync-only methods.
- Text-to-motion without a speech context, and general-purpose motion generators where speech is one condition among many.
- Agent, robot or interaction systems that use gestures without contributing how they are generated.
- Sign language production.
- **Preprints.** Only peer-reviewed publications are listed. A preprint is added once its published version exists, with the arXiv copy linked as the open copy.

## How to read the tables

Every row is generated from a record in [`data/`](data/); the records hold more fields than the tables show (motion representation, datasets, languages, metrics, user study, real-time claims, a one-sentence summary). The fields and their allowed values are defined in [docs/SCHEMA.md](docs/SCHEMA.md).

- No mark: the record was filled from the paper's full text.
- **†** The full text was not freely accessible, so the record was filled from the abstract only. Empty cells mean the abstract does not say.
- **‡** Only bibliographic metadata was available. The paper is listed so the map is complete, but its row is not filled in.

Most records were extracted with automated assistance and are marked `verified: false` in the data until confirmed by a second independent reading. If you spot an error, a correction by pull request or issue is welcome.

## Papers

Methods and systems, newest first, ordered by venue within each year.

<!-- BEGIN:papers -->
### 2026

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| AAAI | [DialoGen: Towards Dialog Gesture Generation via Identity-Decoupled Style Guidance in Interactive Diffusion Model](https://ojs.aaai.org/index.php/AAAI/article/view/38327)† | audio |  | diffusion | dyadic |  |
| AAAI | [Mitigating Error Accumulation in Co-Speech Motion Generation via Global Rotation Diffusion and Multi-Level Constraints](https://ojs.aaai.org/index.php/AAAI/article/view/38281) · [open copy](https://arxiv.org/abs/2511.10076) · [project](https://xiangyuezhang.com/GlobalDiff/) | audio, speaker-id, seed-motion | upper-body, hands, face | diffusion, flow-matching | monologue | [code](https://github.com/Xiangyue-Zhang/GlobalDiff) + weights |
| AAAI | [Playmate2: Training-Free Multi-Character Audio-Driven Animation via Diffusion Transformer with Reward Feedback](https://arxiv.org/abs/2510.12089) · [project](https://playmate111.github.io/Playmate2/) | text, audio, image | upper-body, face | diffusion, flow-matching | monologue, multi-party |  |
| AAAI | [Streaming Generation of Co-Speech Gestures via Accelerated Rolling Diffusion](https://doi.org/10.1609/aaai.v40i31.39807) · [open copy](https://ojs.aaai.org/index.php/AAAI/article/download/39807/43768) | audio, style, speaker-id | full-body | diffusion | monologue | [code](https://github.com/andrewbo29/co-speech-gestures-rolling-diffusion) |
| AAAI | [Training-Free Multi-Character Audio-Driven Animation via Diffusion Transformer with Reward Feedback](https://ojs.aaai.org/index.php/AAAI/article/view/37725)† | audio |  | diffusion |  |  |
| ACM | [An Interaction Motion Generation Model Based on A Diffusion Model and Graph Attention for Back-Channel Behavior Synthesis](https://doi.org/10.1145/3776734.3794490)† | interlocutor |  | diffusion | dyadic |  |
| ACM | [Holistic LLM-Based Expressive Behavior Generation for Robots](https://doi.org/10.1145/3776734.3794507)† | text |  | llm |  |  |
| ACM | [NeRAG: Neuro-Explicit Retrieval-Augmented Generation for Real-Time Interaction in Digital Humans](https://doi.org/10.1145/3805622.3810842)† |  |  | retrieval, hybrid |  |  |
| ACM MM | [Super Star: Towards Streaming Real-time Interactive Agents for Digital Humans](https://arxiv.org/abs/2608.24909) · [project](https://super-star-2026.github.io/) | audio, seed-motion | full-body, hands, face | autoregressive, vq | monologue |  |
| CAVW | [HoloDiff: Holistic Talking Human Animation Via Latent Diffusion](https://doi.org/10.1002/cav.70173)† | audio |  | diffusion | monologue |  |
| CCF TPCI | [Enhanced data techniques and optimization in conversational gesture generation](https://doi.org/10.1007/s42486-025-00213-z)‡ |  |  |  |  |  |
| CGF | [Conversational Gesture Model (CGM): Extending Speaker‐Centric Audio‐Driven Motion Generation to Full Conversation Gestures](https://doi.org/10.1111/cgf.70412)† | audio, text, interlocutor |  |  | dyadic |  |
| CGF | [SiGnature: Explicit Motion Diffusion for Stylized Semantic Gesture Generation](https://doi.org/10.1111/cgf.70557) · [open copy](https://arxiv.org/abs/2606.15889) | audio, text | full-body, hands | diffusion | monologue |  |
| CHI | [AgentHands: Generating Interactive Hand Gestures for Spatially Grounded Agent Conversations in XR](https://doi.org/10.1145/3772318.3790938)† | text | hands | llm |  |  |
| CVPR | [CoordSpeaker: Exploiting Gesture Captioning for Coordinated Caption-Empowered Co-Speech Gesture Generation](https://youngseng.github.io/publications/) · [open copy](https://arxiv.org/abs/2511.22863) | audio, text | full-body, hands | vae, diffusion | monologue |  |
| CVPR | [DyaDiT: A Multi-Modal Diffusion Transformer for Socially Favorable Dyadic Gesture Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Peng_DyaDiT_A_Multi-Modal_Diffusion_Transformer_for_Socially_Favorable_Dyadic_Gesture_CVPR_2026_paper.html) · [open copy](https://arxiv.org/abs/2602.23165) · [project](https://puckikk1202.github.io/dyadit_hp/) | audio, interlocutor | upper-body, hands | vq, diffusion | dyadic |  |
| CVPR | [MIBURI: Towards Expressive Interactive Gesture Synthesis](https://arxiv.org/abs/2603.03282) · [project](https://vcai.mpi-inf.mpg.de/projects/MIBURI/) | audio, text, speaker-id | full-body, hands, face | vq, autoregressive | monologue |  |
| CVPR | [StreamAvatar: Streaming Diffusion Models for Real-Time Interactive Human Avatars](https://arxiv.org/abs/2512.22065) · [project](https://streamavatar.github.io) | audio, image, text | full-body, hands, face | diffusion, autoregressive, gan |  |  |
| CVPR | [ViBES: A Conversational Agent with Behaviorally-Intelligent 3D Virtual Body](https://arxiv.org/abs/2512.14234) · [project](https://ai.stanford.edu/~juze/ViBES/) | text, audio, seed-motion | full-body, hands, face | autoregressive | dyadic |  |
| ECCV | [SICAGE: Speaker-Independent Culture-Aware Gesture Generation using TED4C-L Dataset](https://doi.org/10.1007/978-3-032-37225-3_22) · [open copy](https://arxiv.org/abs/2606.30001) · [project](https://arielgjaci.com/sicage) | audio, text, seed-motion | upper-body | vq, diffusion | monologue | [code](https://arielgjaci.com/sicage) |
| ECCV | [StreamTalk: Streaming Co-Speech Gesture Generation with Key-Pose Anchoring](https://doi.org/10.1007/978-3-032-37595-7_32) · [open copy](https://arxiv.org/abs/2608.01643) · [project](https://xiangyue-zhang.github.io/StreamTalk/) | audio, speaker-id | full-body, hands | diffusion, retrieval | monologue |  |
| ECCV 2026 Workshop on Interactive Social Avatars | [InteractGesture: Progressive Chunk Guidance for Continuous Streaming Co-Speech Gesture Control](https://www.ekkasit.com/interactgesture-page/) · [open copy](https://arxiv.org/abs/2608.25734) · [project](https://exitudio.github.io/interactgesture-page) | audio | full-body | vq, diffusion | monologue |  |
| EEITE | [Efficient Emotion-Aware Iconic Gesture Prediction for Robot Co-Speech](https://doi.org/10.1109/eeite69609.2026.11679713) · [open copy](https://arxiv.org/abs/2604.11417) | text, emotion |  | regression | monologue |  |
| ESWA | [GranuMamba: A multi-granularity state space model for co-speech gesture generation](https://doi.org/10.1016/j.eswa.2026.133415)‡ |  |  |  |  |  |
| ESWA | [Holistic co-speech motion generation via cross-gated attention and cross-limb interaction](https://doi.org/10.1016/j.eswa.2026.132711)‡ |  |  |  |  |  |
| Graphical Models | [Co-Speech Holistic 3D Motion Generation with Style from Video](https://doi.org/10.1016/j.gmod.2026.101332)† · [open copy](https://doi.org/10.2139/ssrn.6025969) | audio, video, style |  | diffusion |  |  |
| HRI | [Communicating Object Relations through Robot Gestures](https://doi.org/10.1145/3757279.3785554)† | text |  | llm |  |  |
| ICASSP | [AdaptiveDiffuseMotion: Adaptive Multi-Task Diffusion Model for Speech-Driven Holistic Motion Generation](https://doi.org/10.1109/icassp55912.2026.11463428)† · [project](https://symbolzzz.github.io/AdaptiveDiffuseMotion/) | audio | face | diffusion |  |  |
| ICASSP | [Audience-Aware Co-speech Gesture Generation in Public Speaking via Anticipation Tokens](https://doi.org/10.1109/icassp55912.2026.11462581)† | audio |  | diffusion |  |  |
| ICASSP | [Gelina: Unified Speech and Gesture Synthesis via Interleaved Token Prediction](https://doi.org/10.1109/icassp55912.2026.11464562) · [open copy](https://arxiv.org/abs/2510.12834) | text, audio | full-body | vq, autoregressive, flow-matching | monologue |  |
| ICASSP | [MAG: Multi-Modal Aligned Autoregressive Co-Speech Gesture Generation without Vector Quantization](https://doi.org/10.1109/icassp55912.2026.11462575) · [open copy](https://arxiv.org/abs/2503.14040) | audio, text, speaker-id | full-body | vae, masked-modeling, autoregressive, diffusion | monologue |  |
| ICASSP | [ReCoM: Realistic Co-Speech Motion Generation with Recurrent Embedded Transformer](https://doi.org/10.1109/icassp55912.2026.11464361) · [open copy](https://arxiv.org/abs/2503.21847) · [project](https://yong-xie-xy.github.io/ReCoM/) | audio, speaker-id | upper-body, hands, face | vq, other | monologue |  |
| ICASSP | [Style-Disentangled Diffusion for Controllable and Identity-Generalized Speech-Driven Body Motion Generation](https://doi.org/10.1109/icassp55912.2026.11462327)† | audio |  | diffusion |  |  |
| ICME | [Mamba-Enhanced Implicit Motion Learning for Audio-Driven Portrait Animation](https://arxiv.org/abs/2606.03402) | audio, image | face, hands, upper-body | diffusion, other | monologue |  |
| IEEE Access | [Generating Prosody-Aligned Gestures via Residual Vector Quantization With Uniform Regularization and Activity Loss](https://doi.org/10.1109/access.2026.3707129)† |  |  | vq |  |  |
| IJCBS | [Embodied Gesture Synchronized Virtual Coaches Train Conversational Skills with Nonverbal Feedback in Online Training Platforms](https://doi.org/10.66238/ijcbs93) · [open copy](https://ijcbs.org/index.php/IJCBS/article/download/93/106) | text, audio | upper-body, hands |  |  |  |
| IJCV | [Cosh-DiT: Co-Speech Gesture Video Synthesis via Hybrid Audio-Visual Diffusion Transformers](https://doi.org/10.1007/s11263-026-02752-z) · [open copy](https://arxiv.org/abs/2503.09942) · [project](https://sunyasheng.github.io/projects/COSH-DIT) | audio, image | upper-body, hands, face | vq, diffusion | monologue |  |
| JAV-CG @ ACM Multimedia 2026 | [EMODY Flow: Emotion-Aware Audio-Driven Full-Body Motion Generation](https://arxiv.org/abs/2609.16011) | audio, emotion | full-body, face | flow-matching | monologue | [code](https://github.com/krag-harsh/EMODY-Flow) |
| Lecture Notes in Computer Science | [CtrlCoMo: Controllable Co-speech Motion Generation with Gesture–Action Disentanglement](https://doi.org/10.1007/978-3-032-37211-6_15)‡ |  |  |  |  |  |
| Lecture Notes in Computer Science | [FaceCapGes: Real-Time Frame-by-Frame Gesture Generation from Audio, Facial Capture, and Head Pose](https://doi.org/10.1007/978-3-032-22267-1_33)‡ |  |  |  |  |  |
| LNCS | [AsynFusion: Towards Asynchronous Latent Consistency Models for Decoupled Whole-Body Audio-Driven Avatars](https://doi.org/10.1007/978-981-95-5676-2_35) · [open copy](https://arxiv.org/abs/2505.15058) | audio, speaker-id | upper-body, face | diffusion | monologue |  |
| LNCS | [RoboGesture: Real-Time Semantic-Aligned Co-speech Gestures Generation for Humanoid Interaction](https://doi.org/10.1007/978-3-032-37429-5_8) · [open copy](https://arxiv.org/abs/2608.28693) · [project](https://RoboGesture.github.io) | audio, seed-motion | upper-body, hands | diffusion, flow-matching | monologue |  |
| LNCS | [SemConFlow: Semantic Grounding of Holistic Co-Speech Gesture Generation with Contrastive Flow-Matching](https://doi.org/10.1007/978-3-032-37232-1_29) · [open copy](https://arxiv.org/abs/2603.26553) · [project](https://marcos452.github.io/HoliticSemGes/) | audio, text | full-body, hands, face | vq, flow-matching | monologue |  |
| MTI | [MAVAGEN: Multimodal Avatar Generation Framework for Personalized Human–Computer Interaction](https://doi.org/10.3390/mti10050055)† | text, image | upper-body, hands, face |  |  |  |
| Neurocomputing | [DESformer: Disentangling emotion and style for co-speech body-motion synthesis](https://doi.org/10.1016/j.neucom.2026.133544)‡ |  |  |  |  |  |
| RA-L | [Speech-Driven Gesture Generation via Conditional Flow Matching With Masked Training and Clamped Sampling](https://doi.org/10.1109/lra.2026.3700424)† | audio |  | flow-matching |  |  |
| TCE | [Emo-gestor: 3D Co-speech Body Generation Based on Multimodal Emotion-Driven](https://doi.org/10.1109/tce.2026.3697391)† | audio, text, emotion | full-body | diffusion |  |  |
| TCSVT | [PAGE: Parts-Aware GuidancE for Co-Speech Gesture Portrait Video Generation](https://doi.org/10.1109/tcsvt.2026.3738661)‡ |  |  |  |  |  |
| THRI | [Enhancing End-user Engagement in Human–Robot Interaction by Performing LLM-driven Expressive Behaviors](https://doi.org/10.1145/3813107)† |  |  | llm |  |  |
| TiiS | [ImaGGen: Zero-Shot Generation of Co-Speech Semantic Gestures Grounded in Language and Image Input](https://doi.org/10.1145/3845992) · [open copy](https://arxiv.org/abs/2510.17617) · [project](https://review-anon-io.github.io/ImaGGen.github.io/) | text, image | upper-body, hands | hybrid, llm | monologue |  |
| TIP | [Generation in Generation: Fluid Co-Speech Gesture Synthesis With Generative Continuous Quantization](https://doi.org/10.1109/tip.2026.3715321)† | audio |  | other |  |  |
| TMM | [MambaGesture2: Co-Speech Gesture Generation via Hierarchical Fusion and Spatiotemporal Aggregation](https://doi.org/10.1109/tmm.2026.3668541)† · [project](https://fcchit.github.io/mambagesture2) |  |  | diffusion |  |  |
| TVCG | [ExGes: Expressive Human Motion Retrieval and Modulation for Audio-Driven Gesture Synthesis](https://doi.org/10.1109/tvcg.2026.3679469) · [open copy](https://arxiv.org/abs/2503.06499) | audio | full-body | retrieval, diffusion | monologue |  |
| WACV | [InteracTalker: Prompt-Based Human-Object Interaction with Co-Speech Gesture Generation](https://doi.org/10.1109/wacv61042.2026.00146) · [open copy](https://arxiv.org/abs/2512.12664) · [project](https://sreeharirajan.github.io/projects/InteracTalker/) | text, audio | full-body | diffusion | monologue |  |

### 2025

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| 3DV | [HoleGest: Decoupled Diffusion and Motion Priors for Generating Holisticly Expressive Co-Speech Gestures](https://doi.org/10.1109/3dv66043.2025.00074) · [open copy](https://arxiv.org/abs/2503.13229) · [project](https://cyk990422.github.io/HoloGest.github.io/) | audio, text | full-body, hands, locomotion | diffusion, gan | monologue |  |
| AAAI | [DIDiffGes: Decoupled Semi-Implicit Diffusion Models for Real-time Gesture Generation from Speech](https://doi.org/10.1609/aaai.v39i3.32248) · [open copy](https://ojs.aaai.org/index.php/AAAI/article/download/32248/34403) · [project](https://cyk990422.github.io/DIDiffGes) | audio, style, seed-motion | full-body, hands | diffusion, gan | monologue |  |
| AAMAS | [Large Language Models for Virtual Human Gesture Selection](https://doi.org/10.65109/fnip6998) · [open copy](https://arxiv.org/abs/2503.14408) | text | hands | llm | monologue | [code](https://github.com/pariesque/SIMA) |
| ACL | [Speaking Beyond Language: A Large-Scale Multimodal Dataset for Learning Nonverbal Cues from Video-Grounded Dialogues](https://aclanthology.org/2025.acl-long.112/) · [open copy](https://arxiv.org/abs/2506.00958) | text | upper-body, hands, face | vq, autoregressive, llm |  | [code](https://github.com/winston1214/nonverbal-conversation) |
| ACM | [Impact of Personality on Generation of Co-speech Nonverbal Behaviors Represented by 3D Skeleton Pose](https://doi.org/10.1145/3765766.3765785)† | audio, text | upper-body |  |  |  |
| ACM | [SemGest: A Multimodal Feature Space Alignment and Fusion Framework for Semantic-aware Co-speech Gesture Generation](https://doi.org/10.1145/3746268.3759433)† | audio, text | full-body | diffusion |  |  |
| ACM | [SemGesture: Synthesizing Semantically Enhanced and Coherent Gestures](https://doi.org/10.1145/3746027.3755753)† |  |  | retrieval, llm |  |  |
| ACM MM | [Contextual Gesture: Co-Speech Gesture Video Generation through Context-aware Gesture Representation](https://doi.org/10.1145/3746027.3755140) · [open copy](https://arxiv.org/abs/2502.07239) · [project](https://andypinxinliu.github.io/Contextual-Gesture/) | audio, text | upper-body, hands, face | vq, masked-modeling | monologue |  |
| ACM MM | [EchoMask: Speech-Queried Attention-based Mask Modeling for Holistic Co-Speech Motion Generation](https://doi.org/10.1145/3746027.3754847) · [open copy](https://arxiv.org/abs/2504.09209) · [project](https://xiangyuezhang.com/EchoMask/) | audio, seed-motion | full-body, hands, face | vq, masked-modeling | monologue | [code](https://github.com/Xiangyue-Zhang/EchoMask) + weights |
| ACM MM | [Versatile Multimodal Controls for Expressive Talking Human Animation](https://doi.org/10.1145/3746027.3755401) · [open copy](https://arxiv.org/abs/2503.08714) · [project](https://digital-avatar.github.io/ai/VersaAnimator/) | audio, text, image | full-body, face | vq, diffusion | monologue |  |
| ACM proceedings | [AnchorTalk: High-Fidelity Upper-Body Talking Human Generation From Speech](https://doi.org/10.1145/3731715.3733276)† | audio | upper-body, face |  |  |  |
| AIP Conference Proceedings | [Translating audio into movement: A semantic gesture generation approach using conditional GANs](https://doi.org/10.1063/5.0263280)‡ |  |  |  |  |  |
| Applied Sciences | [Controllable Speech-Driven Gesture Generation with Selective Activation of Weakly Supervised Controls](https://doi.org/10.3390/app15179467)† · [open copy](https://www.mdpi.com/2076-3417/15/17/9467/pdf?version=1756442434) | audio, emotion |  |  |  |  |
| Biomimetics | [Predicting and Synchronising Co-Speech Gestures for Enhancing Human–Robot Interactions Using Deep Learning Models](https://doi.org/10.3390/biomimetics10120835) · [open copy](https://www.mdpi.com/2313-7673/10/12/835/pdf) · [project](https://huggingface.co/qfrodicio) · [video](https://youtu.be/OxBceJ-G3CI) | text | upper-body | hybrid |  |  |
| CAVW | [A Two‐Stage Controllable Co‐Speech Gesture Generation Method](https://doi.org/10.1002/cav.70077)† | audio, style |  | llm, vq, diffusion |  |  |
| CAVW | [RIDGE: Rule-Infused Deep Learning for Realistic Co-Speech Gesture Generation](https://doi.org/10.1002/cav.70034) · [project](https://www.mrlab.co.kr/research/ridge) | text | upper-body | hybrid, rule-based, retrieval | monologue |  |
| CGF | [EmoDiffGes: Emotion‐Aware Co‐Speech Holistic Gesture Generation with Progressive Synergistic Diffusion](https://doi.org/10.1111/cgf.70261)† |  | full-body | diffusion |  |  |
| Communications in Computer and Information Science | [FastTalker: Co-Speech Gesture Generation via Fast-Order Diffusion ODE Solver](https://doi.org/10.1007/978-981-96-4279-3_6)‡ |  |  |  |  |  |
| Conference | [Generating Half-Body Virtual Avatars of Teachers in E-learning Contexts](https://doi.org/10.1145/3750069.3750298)† | audio, image | upper-body | diffusion |  |  |
| CVM | [VarGes: Improving Variation in Co-Speech 3D Gesture Generation via StyleCLIPS](https://doi.org/10.26599/cvm.2025.9450477) · [open copy](https://arxiv.org/abs/2502.10729) | audio, video, speaker-id | full-body, hands, face | vq, autoregressive | monologue | [code](https://github.com/mookerr/VarGES/) |
| CVPR | [AudCast: Audio-Driven Human Video Generation by Cascaded Diffusion Transformers](https://doi.org/10.1109/cvpr52734.2025.00998) · [open copy](https://arxiv.org/abs/2503.19824) · [project](https://guanjz20.github.io/projects/AudCast) | audio, image | hands, face | diffusion | monologue |  |
| CVPR | [Co-Speech Gesture Video Generation with Implicit Motion-Audio Entanglement](https://doi.org/10.1109/cvpr52734.2025.01063)† | audio |  | diffusion |  |  |
| CVPR | [EchoMimicV2: Towards Striking, Simplified, and Semi-Body Human Animation](https://doi.org/10.1109/cvpr52734.2025.00516) · [open copy](https://arxiv.org/abs/2411.10061) | audio, image | upper-body, hands, face | diffusion | monologue | [code](https://github.com/antgroup/echomimic_v2) |
| CVPR | [HOP: Heterogeneous Topology-based Multimodal Entanglement for Co-Speech Gesture Generation](https://doi.org/10.1109/cvpr52734.2025.00093) · [open copy](https://arxiv.org/abs/2503.01175) · [project](https://star-uu-wang.github.io/HOP/) | text, audio, speaker-id | upper-body, hands | gan | monologue |  |
| CVPR | [Retrieving Semantics from the Deep: an RAG Solution for Gesture Synthesis](https://doi.org/10.1109/cvpr52734.2025.01545) · [open copy](https://arxiv.org/abs/2412.06786) · [project](https://vcai.mpi-inf.mpg.de/projects/RAG-Gesture/) | audio, text, speaker-id | full-body, hands, face | diffusion, retrieval, vae | monologue |  |
| CVPR | [The Language of Motion: Unifying Verbal and Non-verbal Language of 3D Human Motion](https://doi.org/10.1109/cvpr52734.2025.00581) · [open copy](https://arxiv.org/abs/2412.10523) · [project](https://languageofmotion.github.io) | text, audio, seed-motion | full-body, hands, face | llm, vq | monologue |  |
| CVPR | [VLOGGER: Multimodal Diffusion for Embodied Avatar Synthesis](https://doi.org/10.1109/cvpr52734.2025.01482) · [open copy](https://arxiv.org/abs/2403.08764) · [project](https://enriccorona.github.io/vlogger/) | audio, image, text | upper-body, hands, face | diffusion | monologue |  |
| ECCV Workshops | [FastTalker: Jointly Generating Speech and Conversational Gestures from Text](https://doi.org/10.1007/978-3-031-93806-1_14) · [open copy](https://arxiv.org/abs/2409.16404) | text | full-body, hands, face | vq | monologue |  |
| ECTI-CON | [A Study on the Interaction Between Humanoid Robots Equipped with Korean Dataset-Based Gesture Generation AI Models and Korean Users](https://doi.org/10.1109/ecti-con64996.2025.11100804)† |  |  |  |  |  |
| Front. Robot. AI | [Simultaneous text and gesture generation for social robots with small language models](https://doi.org/10.3389/frobt.2025.1581024) · [open copy](https://pmc.ncbi.nlm.nih.gov/articles/12122315) | text | upper-body, face | llm |  |  |
| Frontiers in Artificial Intelligence and Applications | [Toward Realistic Co-Speech Motion via Cross-Modal Spatial-Temporal Attention and Hand Memory Module](https://doi.org/10.3233/faia250794)† | audio | hands, face | diffusion, vq |  |  |
| Frontiers in Robotics and AI | [TED-culture: culturally inclusive co-speech gesture generation for embodied social agents](https://www.frontiersin.org/articles/10.3389/frobt.2025.1546765/full) · [project](https://yixin-shen-1218.github.io/TED_Culture) | audio, seed-motion | upper-body, hands | diffusion | monologue | [code](https://github.com/Yixin-Shen-1218/NAO_Gesture_Generation) |
| GENEA Workshop (ACM ICMI) | [SARGes: Semantically Aligned Reliable Gesture Generation via Intent Chain](https://dl.acm.org/doi/10.1145/3746268.3759436) · [open copy](https://arxiv.org/abs/2503.20202) | text |  | llm |  | [code](https://github.com/gesture-label/ethogram) |
| GRAPP | [Diffusion Transformer Framework for Speech-Driven Stylized Gesture Generation](https://www.scitepress.org/DigitalLibrary/Link.aspx?doi=10.5220/0013318400003912)† | audio, style |  | diffusion |  |  |
| ICASSP | [Identity-Preserving Audio-Driven Holistic Human Motion Video Generation](https://doi.org/10.1109/icassp49660.2025.10890615)† | audio |  |  |  |  |
| ICASSP | [Synthesizing Efficient Trajectory-Controllable Co-Speech Gesture with Latent Consistency Model](https://doi.org/10.1109/icassp49660.2025.10890673)† | audio | upper-body | diffusion |  |  |
| ICASSP | [XDGesture: An xLSTM-based Diffusion Model for Co-speech Gesture Generation](https://doi.org/10.1109/icassp49660.2025.10888507)† |  |  | diffusion |  |  |
| ICCV | [Democratizing High-Fidelity Co-Speech Gesture Video Generation](https://doi.org/10.1109/iccv51701.2025.01325) · [open copy](https://arxiv.org/abs/2507.06812) · [project](https://mpi-lab.github.io/Democratizing-CSG/) | audio, image | full-body, hands, face | diffusion | monologue |  |
| ICCV | [GestureHYDRA: Semantic Co-speech Gesture Synthesis via Hybrid Modality Diffusion Transformer and Cascaded-Synchronized Retrieval-Augmented Generation](https://doi.org/10.1109/iccv51701.2025.01172) · [open copy](https://arxiv.org/abs/2507.22731) · [project](https://mumuwei.github.io/GestureHYDRA/) | audio, style, text | full-body, hands | diffusion, retrieval | monologue |  |
| ICCV | [GestureLSM: Latent Shortcut based Co-Speech Gesture Generation with Spatial-Temporal Modeling](https://doi.org/10.1109/iccv51701.2025.01017) · [open copy](https://arxiv.org/abs/2501.18898) · [project](https://andypinxinliu.github.io/GestureLSM) | audio, text | full-body, hands, face | vq, flow-matching | monologue |  |
| ICCV | [OmniHuman-1: Rethinking the Scaling-Up of One-Stage Conditioned Human Animation Models](https://doi.org/10.1109/iccv51701.2025.01285) · [open copy](https://arxiv.org/abs/2502.01061) · [project](https://omnihuman-lab.github.io/) | audio, image, text | full-body, hands, face | diffusion | monologue |  |
| ICCV | [SemGes: Semantics-aware Co-Speech Gesture Generation using Semantic Coherence and Relevance Learning](https://doi.org/10.1109/iccv51701.2025.01296) · [open copy](https://arxiv.org/abs/2507.19359) · [project](https://semgesture.github.io/) | audio, text, speaker-id | upper-body, hands | vq | monologue |  |
| ICCV | [SemTalk: Holistic Co-speech Motion Generation with Frame-level Semantic Emphasis](https://doi.org/10.1109/iccv51701.2025.01277) · [open copy](https://arxiv.org/abs/2412.16563) · [project](https://xiangyuezhang.com/SemTalk/) | text, audio, seed-motion, speaker-id | full-body, hands, face | vq | monologue | [code](https://github.com/Xiangyue-Zhang/SemTalk) + weights |
| ICLR | [Co$^{3}$Gesture: Towards Coherent Concurrent Co-speech 3D Gesture Generation with Interactive Diffusion](https://arxiv.org/abs/2505.01746) · [project](https://mattie-e.github.io/Co3/) | audio, interlocutor | upper-body, hands | diffusion | dyadic |  |
| ICLR | [CyberHost: Taming Audio-driven Avatar Diffusion Model with Region Codebook Attention](https://arxiv.org/abs/2409.01876) · [project](https://cyberhost.github.io/) | audio, image | upper-body, hands, face | diffusion | monologue |  |
| ICLR | [TANGO: Co-Speech Gesture Video Reenactment with Hierarchical Audio Motion Embedding and Diffusion Interpolation](https://proceedings.iclr.cc/paper_files/paper/2025/file/81a0a519bf7ef7757ff46df2065e7051-Paper-Conference.pdf) · [open copy](https://arxiv.org/abs/2410.04221) · [project](https://pantomatrix.github.io/TANGO/) | audio, video |  | retrieval, diffusion | monologue |  |
| ICME | [Audio-driven Gesture Generation via Deviation Feature in the Latent Space](https://doi.org/10.1109/icme59968.2025.11209432) · [open copy](https://arxiv.org/abs/2503.21616) | audio, image | hands, face | diffusion | monologue |  |
| ICMR | [Inter-Diffusion Generation Model of Speakers and Listeners for Effective Communication](https://doi.org/10.1145/3731715.3733366) · [open copy](https://arxiv.org/abs/2505.04996) | audio, interlocutor | full-body | diffusion, gan | dyadic |  |
| IEEE Access | [Expanding Multilingual Co-Speech Interaction: The Impact of Enhanced Gesture Units in Text-to-Gesture Synthesis for Digital Humans](https://doi.org/10.1109/access.2025.3596328)† · [open copy](https://www.researchsquare.com/article/rs-3350470/latest.pdf) | text |  | retrieval |  |  |
| IEEE CG&A | [SSGesture: Multimodal Gesture Generation Framework for Human Animation Synthesis](https://doi.org/10.1109/mcg.2025.3577477)† |  |  | diffusion |  |  |
| IJCAI | [SyncAnimation: A Real-Time End-to-End Framework for Audio-Driven Human Pose and Talking Head Animation](https://doi.org/10.24963/ijcai.2025/185) · [open copy](https://arxiv.org/abs/2501.14646) · [project](https://syncanimation.github.io) | audio, image | upper-body, face | other | monologue |  |
| IJCB | [Hierarchical Emotion-Guided Masked Transformer for Long-Sequence Co-Speech Gestures with Partial Supervision](https://doi.org/10.1109/ijcb65343.2025.11411217)† | audio, emotion |  | masked-modeling, vq |  |  |
| IJHCS | [Evaluating the effect of co-speech gesture prediction on Human–Robot Interaction](https://doi.org/10.1016/j.ijhcs.2025.103674)† |  |  |  |  |  |
| Information Fusion | [CoCoGesture: Towards coherent co-speech 3D gesture generation in the wild](https://doi.org/10.1016/j.inffus.2025.103613) · [open copy](https://arxiv.org/abs/2405.16874) · [project](https://mattie-e.github.io/GES-X/) | audio | upper-body, hands, face | diffusion | monologue |  |
| ISMAR | [VRtalk: Real-Time Interactive Intelligent Anime Avatars in Virtual Reality](https://doi.org/10.1109/ismar67309.2025.00125)† |  |  |  |  |  |
| Lecture Notes in Networks and Systems | [Generation of Listening Motion of Embodied Conversational Agents Using Speech and Text Information](https://doi.org/10.1007/978-3-032-05994-9_10)‡ |  |  |  |  |  |
| NeurIPS | [Let Them Talk: Audio-Driven Multi-Person Conversational Video Generation](https://doi.org/10.52202/085713-2387) · [open copy](https://arxiv.org/abs/2505.22647) · [project](https://meigen-ai.github.io/multi-talk/) | audio, image, text | upper-body, face | diffusion | multi-party |  |
| NeurIPS | [PyraMotion: Attentional Pyramid-Structured Motion Integration for Co-Speech 3D Gesture Synthesis](https://doi.org/10.52202/085713-4634)† | audio | full-body, hands, face, locomotion | vq |  |  |
| Neurocomputing | [Co-speech video generation via motion transfer based on diffusion models](https://doi.org/10.1016/j.neucom.2025.130833)‡ |  |  |  |  |  |
| Pattern Recognition | [MMoFusion: Multi-modal Co-Speech Motion Generation with Diffusion Model](https://doi.org/10.1016/j.patcog.2025.111774) · [open copy](https://arxiv.org/abs/2403.02905) · [project](https://mmofusion.github.io/) | audio, text, speaker-id, emotion | upper-body, full-body | diffusion | monologue |  |
| PLoS ONE | [Generating interaction gestures in dyadic conversations using a diffusion model](https://doi.org/10.1371/journal.pone.0339579) | audio, interlocutor | upper-body | diffusion | dyadic | [code](https://github.com/animawer/idm/tree/main) |
| RO-MAN | [LLM-Driven Approach for Motion Control in Human-Robot Dialogue for Elevating Engagement](https://doi.org/10.1109/ro-man63969.2025.11217871)† · [open copy](https://naist.repo.nii.ac.jp/record/2001286/files/ROMAN_FinalVersion.pdf) |  |  | llm |  |  |
| SIGGRAPH | [Co-Speech Gesture and Facial Expression Generation for Non-Photorealistic 3D Characters](https://doi.org/10.1145/3721250.3742976) · [open copy](https://arxiv.org/abs/2506.16159) | text, audio | face | retrieval |  |  |
| SIGGRAPH | [Motion-example-controlled Co-speech Gesture Generation Leveraging Large Language Models](https://doi.org/10.1145/3721238.3730611) · [open copy](https://arxiv.org/abs/2507.20220) · [project](https://robinwitch.github.io/MECo-Page) | audio, seed-motion | full-body, hands | llm, vq | monologue |  |
| SIGGRAPH Asia | [Input-Aware Sparse Attention for Real-Time Co-Speech Video Generation](https://doi.org/10.1145/3757377.3763831) · [open copy](https://arxiv.org/abs/2510.02617) · [project](https://beijia11.github.io/IASA) | audio, image | upper-body, hands, face | diffusion, hybrid | monologue |  |
| SIGGRAPH Asia | [Social Agent: Mastering Dyadic Nonverbal Behavior Generation via Conversational LLM Agents](https://doi.org/10.1145/3757377.3763879) · [open copy](https://arxiv.org/abs/2510.04637) · [project](https://pku-mocca.github.io/Social-Agent-Page/) | audio, text, interlocutor, seed-motion | full-body | diffusion, autoregressive, llm | dyadic |  |
| Speech Communication | [TranSTYLer: Multimodal behavioural style transfer for facial and body gestures generation](https://doi.org/10.1016/j.specom.2025.103286) · [open copy](https://hal.science/hal-05222862) | text, audio, style | upper-body, face | other | monologue |  |
| SPIE ICCGV | [LLM Gesticulator: Leveraging Large Language Models for Scalable and Controllable Co-Speech Gesture Synthesis](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/13557/3060395/LLM-Gesticulator--leveraging-large-language-models-for-scalable-and/10.1117/12.3060395.full) · [open copy](https://arxiv.org/abs/2410.10851) | audio, text, speaker-id | full-body, hands | vq, llm, autoregressive | monologue |  |
| Springer proceedings in advanced robotics | [Towards More Expressive Human-Robot Interactions: Combining Latent Representations and Diffusion Models for Co-speech Gesture Generation](https://doi.org/10.1007/978-3-031-81688-8_3)‡ |  |  |  |  |  |
| Springer series in design and innovation | [Speech-Driven Gesture Reenactment Based Human-Computer Interaction Method for Smart Exhibition](https://doi.org/10.1007/978-981-96-8908-8_60)‡ |  |  |  |  |  |
| TCSVT | [fMRI2GES: Co-speech Gesture Reconstruction from fMRI Signal with Dual Brain Decoding Alignment](https://doi.org/10.1109/tcsvt.2025.3558125) · [open copy](https://arxiv.org/abs/2512.01189) |  | upper-body, hands | diffusion |  |  |
| TCSVT | [MMGT: Motion Mask Guided Two-Stage Network for Co-Speech Gesture Video Generation](https://doi.org/10.1109/tcsvt.2025.3604109) · [open copy](https://arxiv.org/abs/2505.23120) | audio, image | upper-body, hands, face | diffusion | monologue | [code](https://github.com/SIA-IDE/MMGT) + weights |
| TIP | [Toward Unified Co-Speech Gesture Generation via Hierarchical Implicit Periodicity Learning](https://doi.org/10.1109/tip.2025.3645572) · [open copy](https://arxiv.org/abs/2512.13131) | audio, text, speaker-id, emotion | upper-body, hands, face | other | monologue |  |
| TPAMI | [Combo: Co-speech holistic 3D human motion generation and efficient customizable adaptation in harmony](https://doi.org/10.1109/tpami.2025.3607711) · [open copy](https://arxiv.org/abs/2408.09397) · [project](https://xc-csc101.github.io/combo/) | audio, speaker-id, emotion | hands, face | diffusion | monologue |  |
| TPAMI | [Stereo-Talker: Audio-driven 3D Human Synthesis with Prior-Guided Mixture-of-Experts](https://doi.org/10.1109/tpami.2025.3596160) · [open copy](https://arxiv.org/abs/2410.23836) | audio, image | upper-body, hands, face | vq, diffusion, llm | monologue |  |
| TVCG | [The Impact of AI-Based Real-Time Gesture Generation and Immersion on the Perception of Others and Interaction Quality in Social XR](https://doi.org/10.1109/tvcg.2025.3616864)† |  |  |  | dyadic |  |
| VRW | [Emotion-Aware Personalized Co-Speech Motion Generation](https://doi.org/10.1109/vrw66409.2025.00327)† | style |  | llm, diffusion, hybrid |  |  |
| WACV | [Conditional GAN for Enhancing Diffusion Models in Efficient and Authentic Global Gesture Generation from Audios](https://doi.org/10.1109/wacv61041.2025.00217) · [open copy](https://arxiv.org/abs/2410.20359) | audio, style, seed-motion | full-body, hands | diffusion, gan | monologue |  |
| WACV | [Joint Co-Speech Gesture and Expressive Talking Face Generation using Diffusion with Adapters](https://doi.org/10.1109/wacv61041.2025.00409) · [open copy](https://arxiv.org/abs/2412.14333) | audio, speaker-id, seed-motion | upper-body, hands, face | diffusion | monologue | [code](https://github.com/Ditzley/joint-gestures-and-face) |

### 2024

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| AAAI | [Chain of Generation: Multi-Modal Gesture Synthesis via Cascaded Conditional Control](https://ojs.aaai.org/index.php/AAAI/article/view/28458) · [open copy](https://arxiv.org/abs/2312.15900) | audio, text, seed-motion | upper-body, hands, face | autoregressive | monologue |  |
| ACL | [LLM Knows Body Language, Too: Translating Speech Voices into Human Gestures](https://aclanthology.org/2024.acl-long.273/) · [open copy](https://aclanthology.org/2024.acl-long.273.pdf) | audio, text | upper-body, hands | vq, llm | monologue |  |
| ACM conference | [A Learning-based Co-Speech Gesture Generation System for Social Robots](https://doi.org/10.1145/3687272.3690915)† |  |  |  |  |  |
| ACM MM | [EGGesture: Entropy-Guided Vector Quantized Variational AutoEncoder for Co-Speech Gesture Generation](https://doi.org/10.1145/3664647.3681392)† |  |  | vq, vae |  |  |
| ACM MM | [Emphasizing Semantic Consistency of Salient Posture for Speech-Driven Gesture Generation](https://doi.org/10.1145/3664647.3680892) · [open copy](https://arxiv.org/abs/2410.13786) | audio | upper-body, hands, face | other | monologue |  |
| ACM MM | [Enabling Synergistic Full-Body Control in Prompt-Based Co-Speech Motion Generation](https://doi.org/10.1145/3664647.3680847) · [open copy](https://arxiv.org/abs/2410.00464) · [project](https://robinwitch.github.io/SynTalker-Page/) | audio, text | full-body, hands | vq, diffusion | monologue | [code](https://github.com/RobinWitch/SynTalker) + weights |
| ACM MM | [MambaGesture: Enhancing Co-Speech Gesture Generation with Mamba and Disentangled Multi-Modality Fusion](https://doi.org/10.1145/3664647.3680625) · [open copy](https://arxiv.org/abs/2407.19976) · [project](https://fcchit.github.io/mambagesture/) | audio, text, style, emotion | full-body, upper-body, hands | diffusion | monologue |  |
| ACM MM | [MDT-A2G: Exploring Masked Diffusion Transformers for Co-Speech Gesture Generation](https://doi.org/10.1145/3664647.3680684) · [open copy](https://arxiv.org/abs/2408.03312) · [project](https://xiaofenmao.github.io/web-project/MDT-A2G/) | audio, text, emotion, speaker-id | upper-body, hands, full-body | diffusion, masked-modeling | monologue |  |
| ACM Multimedia Asia (MMAsia) | [A Unified Editing Method for Co-Speech Gesture Generation via Diffusion Inversion](https://dl.acm.org/doi/10.1145/3696409.3700261) · [open copy](https://arxiv.org/abs/2404.02411) | audio, text, speaker-id, seed-motion | full-body | diffusion | monologue |  |
| AIxVR | [Minimal Latency Speech-Driven Gesture Generation for Continuous Interaction in Social XR](https://doi.org/10.1109/aixvr59861.2024.00038)† · [project](https://nkrome.github.io/FrameCAGE.html) | audio |  |  |  |  |
| Applied Intelligence | [Cospeech body motion generation using a transformer](https://link.springer.com/article/10.1007/s10489-024-05769-4)† | audio |  | vae |  |  |
| CAAI Trans. Intell. Technol. | [Improving diversity of speech‐driven gesture generation with memory networks as dynamic dictionaries](https://doi.org/10.1049/cit2.12321)† | text, audio |  |  |  |  |
| CGF | [LLAniMAtion: LLAMA Driven Gesture Animation](https://doi.org/10.1111/cgf.15167) · [open copy](https://arxiv.org/abs/2405.08042) | text, audio, speaker-id, interlocutor | full-body |  | dyadic |  |
| CVPR | [Co-Speech Gesture Video Generation via Motion-Decoupled Diffusion Model](https://doi.org/10.1109/cvpr52733.2024.00220) · [open copy](https://arxiv.org/abs/2404.01862) | audio, image | upper-body, hands | diffusion | monologue | [code](https://github.com/thuhcsi/S2G-MDDiffusion) |
| CVPR | [ConvoFusion: Multi-Modal Conversational Diffusion for Co-Speech Gesture Synthesis](https://doi.org/10.1109/cvpr52733.2024.00138) · [open copy](https://arxiv.org/abs/2403.17936) · [project](https://vcai.mpi-inf.mpg.de/projects/ConvoFusion/) | audio, text, speaker-id, interlocutor | full-body, hands | diffusion | monologue, dyadic, multi-party |  |
| CVPR | [DiffSHEG: A Diffusion-Based Approach for Real-Time Speech-driven Holistic 3D Expression and Gesture Generation](https://doi.org/10.1109/cvpr52733.2024.00702) · [open copy](https://arxiv.org/abs/2401.04747) · [project](https://jeremycjm.github.io/proj/DiffSHEG) | audio, speaker-id | upper-body, hands, face | diffusion | monologue |  |
| CVPR | [EMAGE: Towards Unified Holistic Co-Speech Gesture Generation via Masked Audio Gesture Modeling](https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_EMAGE_Towards_Unified_Holistic_Co-Speech_Gesture_Generation_via_Expressive_Masked_CVPR_2024_paper.pdf) · [open copy](https://arxiv.org/abs/2401.00374) · [project](https://pantomatrix.github.io/EMAGE/) | audio, seed-motion | full-body, upper-body, hands, face, locomotion | masked-modeling, vq | monologue | [code](https://github.com/PantoMatrix/PantoMatrix) |
| CVPR | [Emotional Speech-Driven 3D Body Animation via Disentangled Latent Diffusion](https://doi.org/10.1109/cvpr52733.2024.00190) · [open copy](https://arxiv.org/abs/2312.04466) · [project](https://amuse.is.tue.mpg.de) | audio | upper-body, hands | diffusion, vae | monologue | [code](https://github.com/kiranchhatre/amuse) |
| CVPR | [From Audio to Photoreal Embodiment: Synthesizing Humans in Conversations](https://doi.org/10.1109/cvpr52733.2024.00101) · [open copy](https://arxiv.org/abs/2401.01885) · [project](https://people.eecs.berkeley.edu/~evonne_ng/projects/audio2photoreal/) | audio, interlocutor | full-body, hands, face | vq, autoregressive, diffusion | dyadic |  |
| CVPR | [Towards Variable and Coordinated Holistic Co-Speech Motion Generation](https://doi.org/10.1109/cvpr52733.2024.00155) · [open copy](https://arxiv.org/abs/2404.00368) · [project](https://feifeifeiliu.github.io/probtalk/) | audio, speaker-id, seed-motion | full-body, face, hands | vq, masked-modeling | monologue |  |
| CVPR | [Weakly-Supervised Emotion Transition Learning for Diverse 3D Co-speech Gesture Generation](https://doi.org/10.1109/cvpr52733.2024.00992) · [open copy](https://arxiv.org/abs/2311.17532) · [project](https://xingqunqi-lab.github.io/Emo-Transition-Gesture/) | audio, seed-motion | upper-body, hands | gan, vae | monologue |  |
| CVPR Workshops | [Fake it to make it: Using synthetic data to remedy the data shortage in joint multimodal speech-and-gesture synthesis](https://doi.org/10.1109/cvprw63382.2024.00201) · [open copy](https://arxiv.org/abs/2404.19622) · [project](https://shivammehta25.github.io/MAGI/) | text, speaker-id | upper-body | flow-matching | monologue |  |
| CVPRW | [DiffTED: One-shot Audio-driven TED Talk Video Generation with Diffusion-based Co-speech Gestures](https://openaccess.thecvf.com/content/CVPR2024W/HuMoGen/papers/Hogue_DiffTED_One-shot_Audio-driven_TED_Talk_Video_Generation_with_Diffusion-based_Co-speech_CVPRW_2024_paper.pdf) · [open copy](https://arxiv.org/abs/2409.07649) | audio, image | upper-body | diffusion | monologue | [code](https://github.com/Ditzley/DiffTED) |
| CVPRW | [Speech2UnifiedExpressions: Synchronous Synthesis of Co-Speech Affective Face and Body Expressions from Affordable Inputs](https://doi.org/10.1109/cvprw63382.2024.00194) · [open copy](https://arxiv.org/abs/2406.18068) | audio, text, speaker-id, seed-motion | upper-body, face | gan | monologue | [code](https://github.com/UttaranB127/speech2unified_expressions) |
| ECCV | [Co-speech Gesture Video Generation with 3D Human Meshes](https://doi.org/10.1007/978-3-031-73024-5_11)† · [open copy](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/12483.pdf) | audio |  | gan |  |  |
| Electronic Research Archive | [Audio2DiffuGesture: Generating a diverse co-speech gesture based on a diffusion model](https://doi.org/10.3934/era.2024250) | audio |  | diffusion | monologue |  |
| Electronics | [DiT-Gesture: A Speech-Only Approach to Stylized Gesture Generation](https://doi.org/10.3390/electronics13091702)† | audio | full-body | diffusion | monologue |  |
| Electronics | [Editable Co-Speech Gesture Synthesis Enhanced with Individual Representative Gestures](https://doi.org/10.3390/electronics13163315)† · [open copy](https://www.mdpi.com/2079-9292/13/16/3315/pdf?version=1724294642) |  |  | regression, vae |  |  |
| Electronics | [TAG2G: A Diffusion-Based Approach to Interlocutor-Aware Co-Speech Gesture Generation](https://doi.org/10.3390/electronics13173364)† · [open copy](https://www.mdpi.com/2079-9292/13/17/3364/pdf?version=1724486119) | text, audio, seed-motion, interlocutor |  | vq, diffusion | dyadic |  |
| ELKOMIKA | [Pengembangan dan Evaluasi Agen Virtual dengan Model Generasi Gestur berbasis Aturan Sederhana](https://doi.org/10.26760/elkomika.v12i4.953) · [open copy](https://ejurnal.itenas.ac.id/index.php/elkomika/article/download/12524/3786) | text |  | rule-based |  |  |
| Frontiers in Robotics and AI | [Evaluation of co-speech gestures grounded in word-distributed representation](https://doi.org/10.3389/frobt.2024.1362463) · [open copy](https://www.frontiersin.org/articles/10.3389/frobt.2024.1362463/pdf?isPublishedV2=False) | text | upper-body | rule-based | monologue |  |
| HAI | [Gesture Generation from Trimodal Context for Humanoid Robots](https://doi.org/10.1145/3687272.3690905) · [open copy](https://arxiv.org/abs/2409.05010) | audio, text, speaker-id | upper-body |  |  |  |
| IALP | [MDG:Multilingual Co-speech Gesture Generation with Low-level Audio Representation and Diffusion Models](https://doi.org/10.1109/ialp63756.2024.10661182)† | audio |  | diffusion |  |  |
| ICASSP | [Conversational Co-Speech Gesture Generation via Modeling Dialog Intention, Emotion, and Context with Diffusion Models](https://doi.org/10.1109/icassp48485.2024.10448208) · [open copy](https://arxiv.org/abs/2312.15567) · [video](https://youtu.be/JHkyoI0qFNA) | audio, text, emotion, interlocutor | hands | diffusion | dyadic |  |
| ICASSP | [Freetalker: Controllable Speech and Text-Driven Gesture Generation Based on Diffusion Models for Enhanced Speaker Naturalness](https://doi.org/10.1109/icassp48485.2024.10447978) · [open copy](https://arxiv.org/abs/2401.03476) · [project](https://youngseng.github.io/FreeTalker/) | audio, text | full-body, hands | diffusion | monologue |  |
| ICASSP | [Gesture Generation Via Diffusion Model with Attention Mechanism](https://doi.org/10.1109/icassp48485.2024.10448118)† | text |  | diffusion |  | [code](https://github.com/LEELLL/GDA-icassp2024) |
| ICASSP | [Unified Speech and Gesture Synthesis Using Flow Matching](https://doi.org/10.1109/icassp48485.2024.10445998) · [open copy](https://arxiv.org/abs/2310.05181) · [project](https://shivammehta25.github.io/Match-TTSG/) | text | upper-body | flow-matching | monologue |  |
| ICCAE | [Generating Interaction Behavior During a Dyadic Conversation Using a Diffusion Model](https://doi.org/10.1109/iccae59995.2024.10569186)† | interlocutor |  | diffusion | dyadic |  |
| ICME | [ExpGest: Expressive Speaker Generation Using Diffusion Model and Hybrid Audio-Text Guidance](https://doi.org/10.1109/icme57554.2024.10687922) · [open copy](https://arxiv.org/abs/2410.09396) | text, audio, emotion | full-body, hands, locomotion | diffusion | monologue | [code](https://github.com/cyk990422/ExpGest/) |
| ICMI | [Towards interpretable co-speech gestures synthesis using STARGATE](https://doi.org/10.1145/3686215.3688819)† · [open copy](https://hal.science/hal-04678537v1/file/Towards_interpretable_co_speech_gestures_synthesis_using_STARGATE_final.pdf) | text, audio |  | autoregressive |  |  |
| ICTC | [SemanticVQVAE for Co-Speech Gesture Quantization with Contrastive Learning](https://doi.org/10.1109/ictc62082.2024.10826672)† |  |  | vq |  |  |
| IFEEA | [EngaGes: An Engagement Fused Co-Speech Gesture Synthesis Model](https://doi.org/10.1109/ifeea64237.2024.10878669)† | audio |  |  |  |  |
| IJCIA | [An Angle-Oriented Approach to Transferring Speech to Gesture for Highly Anthropomorphized Embodied Conversational Agents](https://doi.org/10.1142/s1469026824500068)† | audio | upper-body |  |  | [code](https://github.com/drrobincroft/HARP) |
| IJCV | [Beyond Talking – Generating Holistic 3D Human Dyadic Motion for Communication](https://doi.org/10.1007/s11263-024-02300-7) · [open copy](https://arxiv.org/abs/2403.19467) | audio, text, speaker-id, interlocutor | full-body, hands, face | vq, autoregressive | dyadic |  |
| IJSR | [Dual-Path Transformer-Based GAN for Co-speech Gesture Synthesis](https://doi.org/10.1007/s12369-024-01136-y)† |  |  | gan |  |  |
| Interspeech | [Towards realtime co-speech gestures synthesis using STARGATE](https://doi.org/10.21437/interspeech.2024-302) · [open copy](https://hal.science/hal-04667107/document) | text, audio, seed-motion |  | autoregressive | monologue |  |
| ISMAR-Adjunct | [MuseGesture: A Framework for Gesture Synthesis by Virtual Agents in VR Museum Guides](https://doi.org/10.1109/ismar-adjunct64951.2024.00079)† | text |  | llm, other |  |  |
| IVA | [A Study on Integrating Representational Gestures into Automatically Generated Embodied Explanations](https://doi.org/10.1145/3652988.3673919) · [open copy](https://arxiv.org/abs/2406.12544) | text, audio | upper-body | retrieval, hybrid | monologue |  |
| IVA | [Modifying Gesture Style with Impression Words](https://doi.org/10.1145/3652988.3673931)† | style |  | gan, llm |  |  |
| Lecture Notes in Bioengineering | [Design and Implementation of a Storytelling Robot: Preliminary Evaluation of a GAN-Based Model for Co-Speech Gesture Generation](https://link.springer.com/chapter/10.1007/978-3-031-77318-1_25)† | text, audio |  | gan |  |  |
| Lecture Notes in Computer Science | [Co-speech Gesture Generation with Variational Auto Encoder](https://doi.org/10.1007/978-3-031-53311-2_12)‡ |  |  |  |  |  |
| Lecture Notes in Computer Science | [Optimized Conversational Gesture Generation with Enhanced Motion Feature Extraction and Cascaded Generator](https://doi.org/10.1007/978-981-97-9437-9_29)‡ |  |  |  |  |  |
| Lecture Notes in Computer Science | [PIDM: Personality-Aware Interaction Diffusion Model for Gesture Generation](https://doi.org/10.1007/978-3-031-72356-8_2)‡ |  |  |  |  |  |
| LNCS | [MMIDM: Generating 3D Gesture from Multimodal Inputs with Diffusion Models](https://doi.org/10.1007/978-981-97-8508-7_22)‡ |  |  |  |  |  |
| NeurIPS | [MambaTalk: Efficient Holistic Gesture Synthesis with Selective State Space Models](https://doi.org/10.52202/079017-0633) · [open copy](https://arxiv.org/abs/2403.09471) · [project](https://kkakkkka.github.io/MambaTalk/) | audio, text, speaker-id | face, hands, upper-body, full-body | vq, other | monologue | [code](https://github.com/kkakkkka/MambaTalk) |
| Neurocomputing | [Learning hierarchical discrete prior for co-speech gesture generation](https://doi.org/10.1016/j.neucom.2024.127831)† | audio, text |  | vq |  |  |
| RA-L | [GesGPT: Speech Gesture Synthesis With Text Parsing from ChatGPT](https://doi.org/10.1109/lra.2024.3359544) · [open copy](https://arxiv.org/abs/2303.13013) | text, audio | upper-body | hybrid, llm, retrieval, regression | monologue |  |
| RO-MAN | [Labeling Sentences with Symbolic and Deictic Gestures via Semantic Similarity](https://doi.org/10.1109/ro-man60168.2024.10731402) · [open copy](https://arxiv.org/abs/2407.02151) | text |  | rule-based |  | [code](https://github.com/arielgj95/Gestures_labeling.git) |
| SIGGRAPH Asia | [Body Gesture Generation for Multimodal Conversational Agents](https://doi.org/10.1145/3680528.3687648)† · [project](https://pulsekim.github.io/posts/bodygesture/) |  |  | hybrid |  |  |
| SIGGRAPH Asia | [SIGGesture: Generalized Co-Speech Gesture Synthesis via Semantic Injection with Large-Scale Pre-Training Diffusion Models](https://doi.org/10.1145/3680528.3687677) · [open copy](https://arxiv.org/abs/2405.13336) | audio, text, speaker-id | upper-body | vq, diffusion, llm | monologue |  |
| TAP | [Personality Expression Using Co-Speech Gesture](https://doi.org/10.1145/3694905)† |  |  | hybrid |  |  |
| THMS | [Speech-Driven Gesture Generation Using Transformer-Based Denoising Diffusion Probabilistic Models](https://doi.org/10.1109/thms.2024.3456085)† |  |  | diffusion |  |  |
| TMM | [Cross-Modal Quantization for Co-Speech Gesture Generation](https://doi.org/10.1109/tmm.2024.3405743)† | audio |  | vq, autoregressive |  |  |
| TMM | [EmotionGesture: Audio-Driven Diverse Emotional Co-Speech 3D Gesture Generation](https://doi.org/10.1109/tmm.2024.3407692) · [open copy](https://arxiv.org/abs/2305.18891) · [project](https://xingqunqi-lab.github.io/Emotion-Gesture-Web/) | audio, text, emotion, seed-motion | upper-body, hands | vae | monologue | [code](https://github.com/XingqunQi-lab/EmotionGestures) |
| TOG | [Semantic Gesticulator: Semantics-Aware Co-Speech Gesture Synthesis](https://doi.org/10.1145/3658134) · [open copy](https://arxiv.org/abs/2405.09814) · [project](https://pku-mocca.github.io/Semantic-Gesticulator-Page/) | audio, text | full-body, hands | vq, autoregressive, llm, retrieval | monologue | [code](https://github.com/LuMen-ze/Semantic-Gesticulator-Official) |
| TVCG | [Speech-driven Personalized Gesture Synthetics: Harnessing Automatic Fuzzy Feature Inference](https://arxiv.org/abs/2403.10805) · [project](https://zf223669.github.io/Diffmotion-v2-website/) | audio | full-body, hands, locomotion | diffusion | monologue |  |
| VRIH | [Audio2AB: Audio-driven collaborative generation of virtual character animation](https://doi.org/10.1016/j.vrih.2023.08.006)† | audio, text, emotion | full-body, face | gan |  |  |
| WACV | [DR2: Disentangled Recurrent Representation Learning for Data-efficient Speech Video Synthesis](https://doi.org/10.1109/wacv57701.2024.00609)† | audio | full-body |  |  |  |

### 2023

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| AAMAS | [Real Time Gesturing in Embodied Agents for Dynamic Content Creation](https://dl.acm.org/doi/10.5555/3545946.3599175) · [open copy](https://www.southampton.ac.uk/~eg/AAMAS2023/pdfs/p3068.pdf) · [video](https://youtu.be/j1F0R0SkRL4) | text | upper-body, hands, face | rule-based |  |  |
| ACM MM | [Cultural Self-Adaptive Multimodal Gesture Generation Based on Multiple Culture Gesture Dataset](https://doi.org/10.1145/3581783.3611705)† · [open copy](https://dl.acm.org/doi/pdf/10.1145/3581783.3611705) |  |  |  |  |  |
| ACM MM | [UnifiedGesture: A Unified Gesture Synthesis Model for Multiple Skeletons](https://doi.org/10.1145/3581783.3612503) · [open copy](https://arxiv.org/abs/2309.07051) | audio, style, seed-motion | upper-body | diffusion, other | monologue | [code](https://github.com/YoungSeng/UnifiedGesture) + weights |
| Advanced Robotics | [It takes two, not one: context-aware nonverbal behaviour generation in dyadic interactions](https://doi.org/10.1080/01691864.2023.2279595)† · [open copy](https://eprints.soton.ac.uk/504497/1/It_takes_two_not_one_context-aware_nonverbal_behaviour_generation_in_dyadic_interactions.pdf) | interlocutor |  | gan | dyadic |  |
| CGF | [ZeroEGGS: Zero-shot Example-based Gesture Generation from Speech](https://doi.org/10.1111/cgf.14734) · [open copy](https://arxiv.org/abs/2209.07556) | audio, style | full-body, hands | vae, autoregressive | monologue | [code](https://github.com/ubisoft/ubisoft-laforge-ZeroEGGS) |
| CVPR | [Co-speech Gesture Synthesis by Reinforcement Learning with Contrastive Pretrained Rewards](https://doi.org/10.1109/cvpr52729.2023.00231) | audio, seed-motion | upper-body | vq, autoregressive, other | monologue | [code](https://github.com/RLracer/RACER) |
| CVPR | [Generating Holistic 3D Human Motion from Speech](https://doi.org/10.1109/cvpr52729.2023.00053) · [open copy](https://arxiv.org/abs/2212.04420) · [project](https://talkshow.is.tue.mpg.de/) | audio, speaker-id | hands, face | vq, autoregressive | monologue |  |
| CVPR | [QPGesture: Quantization-Based and Phase-Guided Motion Matching for Natural Speech-Driven Gesture Generation](https://openaccess.thecvf.com/content/CVPR2023/papers/Yang_QPGesture_Quantization-Based_and_Phase-Guided_Motion_Matching_for_Natural_Speech-Driven_Gesture_CVPR_2023_paper.pdf) · [open copy](https://arxiv.org/abs/2305.11094) | audio, text, seed-motion | upper-body | vq, retrieval | monologue | [code](https://github.com/YoungSeng/QPGesture) + weights |
| CVPR | [Taming Diffusion Models for Audio-Driven Co-Speech Gesture Generation](https://doi.org/10.1109/cvpr52729.2023.01016) · [open copy](https://arxiv.org/abs/2303.09119) | audio, seed-motion | upper-body, hands | diffusion | monologue | [code](https://github.com/Advocate99/DiffGesture) |
| FG | [Zero-Shot Style Transfer for Multimodal Data-Driven Gesture Synthesis](http://dx.doi.org/10.1109/fg57933.2023.10042658)† · [open copy](https://hal.science/hal-03972560/document) | audio, text, style | upper-body |  | monologue |  |
| Frontiers in AI | [Zero-shot style transfer for gesture animation driven by text and speech using adversarial disentanglement of multimodal style encoding](https://doi.org/10.3389/frai.2023.1142997) · [open copy](https://www.frontiersin.org/articles/10.3389/frai.2023.1142997/pdf?isPublishedV2=False) | audio, text, style | upper-body | other | monologue |  |
| GENEA Workshop | [UEA Digital Humans The UEA Digital Humans entry to the GENEA Challenge 2023](https://openreview.net/forum?id=bBrebR1YpXe)‡ · [video](https://www.youtube.com/watch?v=u6LXN7ka674) |  |  |  |  | [code](https://github.com/JonathanPWindle/uea-dh-genea23) |
| ICASSP | [MPE4G: Multimodal Pretrained Encoder for Co-Speech Gesture Generation](https://doi.org/10.1109/icassp49357.2023.10095344) · [open copy](https://arxiv.org/abs/2305.15740) | text, audio | full-body, hands | masked-modeling, autoregressive | monologue | [code](https://github.com/GT-KIM/Co-speech_gesture_generation) |
| ICASSP | [Salient Co-Speech Gesture Synthesizing with Discrete Motion Representation](https://doi.org/10.1109/icassp49357.2023.10095304) · [open copy](https://hcsi.cs.tsinghua.edu.cn/Paper/Paper23/ICASSP23_YEZIJIE.pdf) | text, audio, seed-motion |  | vq | monologue |  |
| ICCV | [Continual Learning for Personalized Co-Speech Gesture Generation](https://doi.org/10.1109/iccv51070.2023.01910)† · [project](https://chahuja.com/cdiffgan/) |  |  |  |  |  |
| ICCV | [LivelySpeaker: Towards Semantic-Aware Co-Speech Gesture Generation](https://doi.org/10.1109/iccv51070.2023.01902) · [open copy](https://arxiv.org/abs/2309.09294) | text, audio, speaker-id | upper-body, hands | diffusion, regression | monologue | [code](https://github.com/zyhbili/LivelySpeaker) |
| ICIP | [Learning Torso Prior for Co-Speech Gesture Generation with Better Hand Shape](http://dx.doi.org/10.1109/icip49359.2023.10222259)† | audio | upper-body, hands | gan |  |  |
| ICMI | [AQ-GT: a Temporally Aligned and Quantized GRU-Transformer for Co-Speech Gesture Synthesis](https://dl.acm.org/doi/10.1145/3577190.3614135) · [open copy](https://arxiv.org/abs/2305.01241) | audio, text, speaker-id, seed-motion | full-body, hands | vq, gan, autoregressive | monologue | [code](https://github.com/hvoss-techfak/AQGT) |
| ICMI | [DiffuGesture: Generating Human Gesture From Two-person Dialogue With Diffusion Models](https://doi.org/10.1145/3610661.3616552)† | audio, interlocutor |  | diffusion | dyadic |  |
| ICMI | [DiffuseStyleGesture+ (SF) The DiffuseStyleGesture+ entry to the GENEA Challenge 2023](https://arxiv.org/abs/2308.13879) | audio, text, speaker-id, seed-motion | full-body, hands | diffusion | monologue | [code](https://github.com/YoungSeng/DiffuseStyleGesture/tree/DiffuseStyleGesturePlus/BEAT-TWH-main) |
| ICMI | [Diffusion-Based Co-Speech Gesture Generation Using Joint Text and Audio Representation](https://doi.org/10.1145/3577190.3616117) · [open copy](https://arxiv.org/abs/2309.05455) | audio, text, interlocutor | full-body | diffusion | dyadic | [code](https://github.com/shivammehta25/CLIP/tree/GestCLIP) |
| ICMI | [Discrete Diffusion for Co-Speech Gesture Synthesis](https://doi.org/10.1145/3610661.3616556)† | audio |  | vq, diffusion |  |  |
| ICMI | [FEIN-Z: Autoregressive Behavior Cloning for Speech-Driven Gesture Generation](https://doi.org/10.1145/3577190.3616115)† |  |  | gan |  |  |
| ICMI | [Gesticulating with NAO: Real-time Context-Aware Co-Speech Gesture Generation for Human-Robot Interaction](https://doi.org/10.1145/3610661.3620664)† | interlocutor |  |  | dyadic |  |
| ICMI | [Gesture Generation with Diffusion Models Aided by Speech Activity Information](https://doi.org/10.1145/3610661.3616554)† | audio |  | diffusion |  |  |
| ICMI | [Gesture Motion Graphs for Few-Shot Speech-Driven Gesture Reenactment](https://doi.org/10.1145/3577190.3616118)† | text, audio |  | other |  |  |
| ICMI | [Large language models in textual analysis for gesture selection](https://doi.org/10.1145/3577190.3614158) · [open copy](https://arxiv.org/abs/2310.13705) | text | hands | llm | monologue | [code](https://osf.io/c82tq) |
| ICMI | [The FineMotion entry to the GENEA Challenge 2023: DeepPhase for conversational gestures generation](https://doi.org/10.1145/3577190.3616119)† | text, audio, interlocutor |  | vq | dyadic |  |
| ICMI | [The KCL-SAIR team's entry to the GENEA Challenge 2023 Exploring Role-based Gesture Generation in Dyadic Interactions: Listener vs. Speaker](https://doi.org/10.1145/3610661.3616555)† |  |  |  | dyadic |  |
| ICMI | [The KU-ISPL entry to the GENEA Challenge 2023-A Diffusion Model for Co-speech Gesture generation](https://doi.org/10.1145/3610661.3616551)† | text, audio, seed-motion |  | diffusion |  |  |
| ICMI | [The UEA Digital Humans entry to the GENEA Challenge 2023](https://doi.org/10.1145/3577190.3616116)† · [open copy](https://dl.acm.org/doi/pdf/10.1145/3577190.3616116) | text, audio, speaker-id, interlocutor |  |  | dyadic |  |
| ICMI Companion | [Co-Speech Gesture Generation via Audio and Text Feature Engineering](https://doi.org/10.1145/3610661.3616553)† · [open copy](https://dl.acm.org/doi/pdf/10.1145/3610661.3616553) | text, audio |  |  |  |  |
| ICSR | [GERT: Transformers for Co-speech Gesture Prediction in Social Robots](https://doi.org/10.1007/978-981-99-8715-3_8)‡ |  |  |  |  |  |
| IEEE VRW | [Generating Co-Speech Gestures for Virtual Agents from Multimodal Information Based on Transformer](https://doi.org/10.1109/vrw58643.2023.00286)† | text, audio, speaker-id |  |  |  |  |
| IJCAI | [DiffuseStyleGesture: Stylized Audio-Driven Co-Speech Gesture Generation with Diffusion Models](https://www.ijcai.org/proceedings/2023/0650.pdf) · [open copy](https://arxiv.org/abs/2305.04919) | audio, style, seed-motion | full-body | diffusion | monologue | [code](https://github.com/YoungSeng/DiffuseStyleGesture) + weights |
| IJSR | [Extrovert or Introvert? GAN-Based Humanoid Upper-Body Gesture Generation for Different Impressions](https://doi.org/10.1007/s12369-023-01051-8)† · [open copy](https://link.springer.com/content/pdf/10.1007/s12369-023-01051-8.pdf) |  | upper-body | gan |  |  |
| IROS | [Co-Speech Gesture Synthesis using Discrete Gesture Token Learning](https://doi.org/10.1109/iros55552.2023.10342027) · [open copy](https://arxiv.org/abs/2303.12822) | audio, text | upper-body | vq, autoregressive | monologue |  |
| IVA | [Augmented Co-Speech Gesture Generation](https://doi.org/10.1145/3570945.3607337) · [open copy](https://arxiv.org/abs/2307.09597) | audio, text, speaker-id, seed-motion | upper-body, hands | vq, autoregressive, gan | monologue |  |
| IVA | [How Far ahead Can Model Predict Gesture Pose from Speech and Spoken Text?](https://doi.org/10.1145/3570945.3607336)† · [open copy](https://dl.acm.org/doi/pdf/10.1145/3570945.3607336) | audio, text |  |  |  |  |
| IVA | [Towards Real-time Co-speech Gesture Generation in Online Interaction in Social XR](https://doi.org/10.1145/3570945.3607315)† · [project](https://nkrome.github.io/CAGE.html) | audio |  |  |  |  |
| MMM | [DiffMotion: Speech-Driven Gesture Synthesis Using Denoising Diffusion Model](https://doi.org/10.1007/978-3-031-27077-2_18) · [open copy](https://arxiv.org/abs/2301.10047) · [project](https://zf223669.github.io/DiffMotionWebsite/) | audio, seed-motion | upper-body | diffusion, autoregressive | monologue |  |
| PACM CGIT (SCA) | [ACT2G: Attention-based Contrastive Learning for Text-to-Gesture Generation](https://dl.acm.org/doi/10.1145/3606940) · [open copy](https://arxiv.org/abs/2309.16162) | text | upper-body | retrieval, vae | monologue |  |
| RO-MAN | [Speech-Gesture GAN: Gesture Generation for Robots and Embodied Agents](https://doi.org/10.1109/ro-man57019.2023.10309493) · [open copy](https://arxiv.org/abs/2309.09346) | text, audio | upper-body | gan | monologue |  |
| SSW | [Diff-TTSG: Denoising probabilistic integrated speech and gesture synthesis](https://doi.org/10.21437/ssw.2023-24) · [open copy](https://arxiv.org/abs/2306.09417) · [project](https://shivammehta25.github.io/Diff-TTSG/) | text | upper-body, hands | diffusion | monologue |  |
| TMM | [Implicit Compositional Generative Network for Length-Variable Co-Speech Gesture Synthesis](https://doi.org/10.1109/tmm.2023.3348331)† | audio |  | other |  |  |
| TOG | [Bodyformer: Semantics-guided 3D Body Gesture Synthesis with Transformer](https://doi.org/10.1145/3592456) · [open copy](https://arxiv.org/abs/2310.06851) | audio, text | upper-body, hands, full-body | vae | monologue |  |
| TOG | [GestureDiffuCLIP: Gesture Diffusion Model with CLIP Latents](https://doi.org/10.1145/3592097) · [open copy](https://dl.acm.org/doi/pdf/10.1145/3592097) · [project](https://pku-mocca.github.io/GestureDiffuCLIP-Page/) | audio, text, style | full-body, hands | vq, diffusion | monologue |  |
| TOG | [Listen, Denoise, Action! Audio-Driven Motion Synthesis with Diffusion Models](https://doi.org/10.1145/3592458) · [open copy](https://arxiv.org/abs/2211.09707) · [project](https://www.speech.kth.se/research/listen-denoise-action/) | audio, style | full-body, locomotion | diffusion | monologue |  |
| TVCG | [Audio2Gestures: Generating Diverse Gestures from Audio](https://doi.org/10.1109/tvcg.2023.3276973) · [open copy](https://arxiv.org/abs/2301.06690) · [project](https://jingli513.github.io/audio2gestures) | audio | upper-body, hands | vae | monologue |  |

### 2022

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| AAMAS | [Multimodal analysis of the predictability of hand-gesture properties](https://doi.org/10.65109/habv5810) · [open copy](https://arxiv.org/abs/2108.05762) · [project](https://svito-zar.github.io/speech2properties2gestures) | text, audio | hands | other | monologue |  |
| ACM MM | [DisCo: Disentangled Implicit Content and Rhythm Learning for Diverse Co-Speech Gestures Synthesis](https://doi.org/10.1145/3503161.3548400)† · [open copy](https://dl.acm.org/doi/pdf/10.1145/3503161.3548400) · [project](https://pantomatrix.github.io/DisCo/) | audio, seed-motion |  |  | monologue | [code](https://github.com/PantoMatrix/PantoMatrix/blob/main/train_disco_audio.py) |
| ACM Poster | [Improving Co-speech gesture rule-map generation via wild pose matching with gesture units.](https://doi.org/10.1145/3550082.3564185)† · [video](https://youtu.be/QBtGdGE1Wgk) | text |  | hybrid |  |  |
| COST | [Generating Diverse Gestures from Speech Using Memory Networks as Dynamic Dictionaries](https://doi.org/10.1109/cost57098.2022.00042)† | audio, text, seed-motion |  |  |  |  |
| CVPR | [Audio-driven Neural Gesture Reenactment with Video Motion Graphs](https://openaccess.thecvf.com/content/CVPR2022/html/Zhou_Audio-Driven_Neural_Gesture_Reenactment_With_Video_Motion_Graphs_CVPR_2022_paper.html) · [open copy](https://arxiv.org/abs/2207.11524) · [project](https://yzhou359.github.io/video_reenact) | audio, video | upper-body, hands | retrieval | monologue | [code](https://github.com/yzhou359/vid-reenact) |
| CVPR | [Learning Hierarchical Cross-Modal Association for Co-Speech Gesture Generation](https://doi.org/10.1109/cvpr52688.2022.01021) · [open copy](https://arxiv.org/abs/2203.13161) · [project](https://alvinliu0.github.io/projects/HA2G) | audio, speaker-id | upper-body, hands | regression | monologue | [code](https://github.com/alvinliu0/HA2G) |
| CVPR | [Low-Resource Adaptation for Personalized Co-Speech Gesture Generation](https://doi.org/10.1109/cvpr52688.2022.01991)† · [project](https://chahuja.com/diffgan) |  |  |  |  |  |
| CVPR | [SEEG: Semantic Energized Co-speech Gesture Generation](https://doi.org/10.1109/cvpr52688.2022.01022)† |  |  |  |  | [code](https://github.com/akira-l/SEEG) |
| ECCV | [Audio-Driven Stylized Gesture Generation with Flow-Based Model](https://doi.org/10.1007/978-3-031-20065-6_41)‡ |  |  |  |  |  |
| HAI | [VISTURE: A System for Video-Based Gesture and Speech Generation by Robots](https://doi.org/10.1145/3527188.3561931)† | video |  |  |  |  |
| ICMI | [Exemplar-based Stylized Gesture Generation from Speech: An Entry to the GENEA Challenge 2022](https://doi.org/10.1145/3536221.3558068)† | audio, style | full-body | vae |  |  |
| ICMI | [GestureMaster: Graph-based Speech-driven Gesture Generation](https://doi.org/10.1145/3536221.3558063)† | audio, text |  |  |  |  |
| ICMI | [Hybrid Seq2Seq Architecture for 3D Co-Speech Gesture Generation](https://doi.org/10.1145/3536221.3558064)† |  |  |  |  |  |
| ICMI | [ReCell: replicating recurrent cell for auto-regressive pose generation](https://doi.org/10.1145/3536220.3558801)† |  |  | autoregressive |  |  |
| ICMI | [ReprGesture: The ReprGesture entry to the GENEA Challenge 2022](https://dl.acm.org/doi/10.1145/3536221.3558066) · [open copy](https://arxiv.org/abs/2208.12133) · [video](https://www.youtube.com/watch?v=KJJYEqyOq5U) | audio, text, seed-motion | upper-body | gan | monologue | [code](https://github.com/YoungSeng/ReprGesture) + weights |
| ICMI | [The DeepMotion entry to the GENEA Challenge 2022](https://dl.acm.org/doi/abs/10.1145/3536221.3558059)† · [open copy](https://dl.acm.org/doi/pdf/10.1145/3536221.3558059) |  |  | vq, autoregressive |  |  |
| ICMI | [The IVI Lab entry to the GENEA Challenge 2022 – A Tacotron2 Based Method for Co-Speech Gesture Generation With Locality-Constraint Attention Mechanism](https://doi.org/10.1145/3536221.3558060)† | text, audio, speaker-id | full-body, upper-body |  |  |  |
| ICMI | [TransGesture: Autoregressive Gesture Generation with RNN-Transducer](https://doi.org/10.1145/3536221.3558061)† |  |  | autoregressive |  |  |
| ICMI | [UEA Digital Humans entry to the GENEA Challenge 2022](https://doi.org/10.1145/3536221.3558065)† | audio, text |  | regression |  |  |
| ICRA | [Context-Aware Body Gesture Generation for Social Robots](https://kclpure.kcl.ac.uk/portal/en/publications/context-aware-body-gesture-generation-for-social-robots)† |  |  | gan | dyadic |  |
| IJCAI | [Text/Speech-Driven Full-Body Animation](https://doi.org/10.24963/ijcai.2022/863) · [open copy](https://arxiv.org/abs/2205.15573) | text, audio | full-body, face | retrieval, other | monologue |  |
| IJSR | [Towards Culture-Aware Co-Speech Gestures for Social Robots](https://doi.org/10.1007/s12369-022-00893-y)† · [open copy](https://link.springer.com/content/pdf/10.1007/s12369-022-00893-y.pdf) | audio |  | gan |  |  |
| IROS | [Controlling the Impression of Robots via GAN-based Gesture Generation](https://doi.org/10.1109/iros47612.2022.9981535)† |  |  | gan |  |  |
| IROS | [Deep Gesture Generation for Social Robots Using Type-Specific Libraries](https://doi.org/10.1109/iros47612.2022.9981734) · [open copy](https://arxiv.org/abs/2210.06790) | text | upper-body | hybrid, retrieval |  |  |
| IROS | [Gesture2Vec: Clustering Gestures using Representation Learning Methods for Co-speech Gesture Generation](https://doi.org/10.1109/iros47612.2022.9981117)† | text |  | vq, vae |  | [code](https://github.com/pjyazdian/Gesture2Vec) |
| LNCS | [Towards a Framework for Social Robot Co-speech Gesture Generation with Semantic Expression](https://doi.org/10.1007/978-3-031-24667-8_10)‡ · [open copy](https://ensta-paris.hal.science/hal-03832923) |  |  |  |  |  |
| MIG | [A Tool for Extracting 3D Avatar-Ready Gesture Animations from Monocular Videos](https://dl.acm.org/doi/pdf/10.1145/3561975.3562953)† | video |  |  |  |  |
| MIG | [S2M-Net: Speech Driven Three-party Conversational Motion Synthesis Networks](https://dl.acm.org/doi/fullHtml/10.1145/3561975.3562954)† | audio |  | gan | multi-party |  |
| Neural Networks | [Evaluation of text-to-gesture generation model using convolutional neural network](https://doi.org/10.1016/j.neunet.2022.03.041)† | text |  |  |  |  |
| NeurIPS | [Audio-Driven Co-Speech Gesture Video Generation](https://doi.org/10.52202/068431-1554) · [open copy](https://arxiv.org/abs/2212.02350) · [project](https://alvinliu0.github.io/projects/ANGIE) | audio, image | upper-body | vq, autoregressive | monologue |  |
| NicoInt | [Motion Generation Of Conversational Character From Labeled Script](https://doi.org/10.1109/nicoint55861.2022.00029)† |  |  |  |  |  |
| RO-MAN | [Agree or Disagree? Generating Body Gestures from Affective Contextual Cues during Dyadic Interactions](https://doi.org/10.1109/ro-man53752.2022.9900760)† | audio, interlocutor |  | gan | dyadic |  |
| RO-MAN | [Towards an automatic generation of natural gestures for a storyteller robot](https://doi.org/10.1109/ro-man53752.2022.9900532)† | text |  | hybrid, gan |  |  |
| Robotics and Autonomous Systems | [Generation of co-speech gestures of robot based on morphemic analysis](https://doi.org/10.1016/j.robot.2022.104154)† | text |  | retrieval |  |  |
| SIGGRAPH | [A Motion Matching-based Framework for Controllable Gesture Synthesis from Speech](https://doi.org/10.1145/3528233.3530750) · [open copy](https://www.cs.ucdavis.edu/~neff/papers/MotionMatchingGesture_SIGGRAPH22.pdf) · [project](https://vcai.mpi-inf.mpg.de/projects/SpeechGestureMatching/) | audio, seed-motion | upper-body, hands | retrieval, gan, hybrid | monologue |  |
| SIGGRAPH Asia | [ASAP: Auto-generating Storyboard and Previz](https://doi.org/10.1145/3550453.3570124)† · [open copy](https://dl.acm.org/doi/pdf/10.1145/3550453.3570124) | text |  |  |  |  |
| SII | [Integration of Gesture Generation System Using Gesture Library with DIY Robot Design Kit](https://doi.org/10.1109/sii52469.2022.9708837)† |  |  |  |  |  |
| SII | [Labeling the Phrases of a Conversational Agent with a Unique Personalized Vocabulary](https://doi.org/10.1109/sii52469.2022.9708605)† · [open copy](https://arxiv.org/abs/2010.06194) | text |  |  |  |  |
| TOG | [Rhythmic Gesticulator: Rhythm-Aware Co-Speech Gesture Synthesis with Hierarchical Neural Embeddings](https://doi.org/10.1145/3550454.3555435) · [open copy](https://arxiv.org/abs/2210.01448) · [project](https://pku-mocca.github.io/Rhythmic-Gesticulator-Page/) | audio, text, speaker-id | upper-body, hands | vq, autoregressive | monologue |  |

### 2021

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| AAMAS | [A Framework for Integrating Gesture Generation Models into Interactive Conversational Agents](https://arxiv.org/abs/2102.12302) · [project](https://nagyrajmund.github.io/project/gesturebot/) · [video](https://www.youtube.com/watch?v=jhgUBS0125A) | text, audio | upper-body | autoregressive | monologue | [code](https://github.com/nagyrajmund/gesturebot) |
| AAMAS | [CMCF: An Architecture for Realtime Gesture Generation by Clustering Gestures by Motion and Communicative Function](https://doi.org/10.65109/thwr5489) · [open copy](http://eprints.gla.ac.uk/253967/1/253967.pdf) | text, audio | hands | retrieval, hybrid | monologue |  |
| AAMAS | [It's A Match! Gesture Generation Using Expressive Parameter Matching](https://doi.org/10.65109/poxn8780)† · [open copy](https://arxiv.org/abs/2103.03130) | audio |  | retrieval | monologue |  |
| ACM MM | [Speech2AffectiveGestures: Synthesizing Co-Speech Gestures with Generative Adversarial Affective Expression Learning](https://doi.org/10.1145/3474085.3475223) · [open copy](https://arxiv.org/abs/2108.00262) · [project](https://gamma.umd.edu/s2ag) | audio, text, speaker-id, seed-motion | upper-body | gan | monologue |  |
| Applied Sciences | [Expressing Robot Personality through Talking Body Language](https://doi.org/10.3390/app11104639)† |  |  |  |  |  |
| ARSO | [A GAN-based Approach to Communicative Gesture Generation for Social Robots](https://doi.org/10.1109/arso51874.2021.9542828) · [open copy](https://dspace.jaist.ac.jp/dspace/bitstream/10119/17573/1/ARSO21_0048_FI.pdf) | text | upper-body | gan | monologue |  |
| CAVW | [ExpressGesture: Expressive gesture generation from speech through database matching](https://onlinelibrary.wiley.com/doi/full/10.1002/cav.2016)† · [video](https://www.youtube.com/watch?v=9opZK-usETY) | audio |  | retrieval |  |  |
| CHI | [Real-time Gesture Animation Generation from Speech for Virtual Human Interaction](https://doi.org/10.1145/3411763.3451554) · [open copy](https://arxiv.org/abs/2208.03244) | audio | upper-body, hands | gan | monologue | [code](https://github.com/mrebol/Gestures-From-Speech) |
| CVMP | [Speech-Driven Conversational Agents using Conditional Flow-VAEs](https://doi.org/10.1145/3485441.3485647)† | audio | upper-body | vae, normalizing-flow |  |  |
| Dialogue | [Audio and Text-Driven approach for Conversational Gestures Generation](https://doi.org/10.28995/2075-7182-2021-20-425-432)† | text, audio |  |  |  |  |
| ECTI-CON | [Speech Gesture Generation from Acoustic and Textual Information using LSTMs](https://doi.org/10.1109/ecti-con51831.2021.9454931)† | audio, text | upper-body | regression | monologue |  |
| Electronics | [Modeling the Conditional Distribution of Co-Speech Upper Body Gesture Jointly Using Conditional-GAN and Unrolled-GAN](https://www.mdpi.com/2079-9292/10/3/228)† | audio | upper-body | gan |  | [code](https://github.com/wubowen416/co-speech-gesture-generation-using-CGAN) |
| FG | [The Importance of Qualitative Elements in Subjective Evaluation of Semantic Gestures](https://doi.org/10.1109/fg52635.2021.9667023)† | text |  | retrieval |  |  |
| GENEA Workshop | [Crossmodal Clustered Contrastive Learning: Grounding of Spoken Language to Gesture](https://dl.acm.org/doi/abs/10.1145/3461615.3485408)† · [video](https://www.youtube.com/watch?v=L5dHXTpCkeI) | text |  |  |  | [code](https://github.com/dondongwon/CC_NCE_GENEA) |
| HCII | [Sequence-to-Sequence Predictive Model: From Prosody to Communicative Gestures](https://doi.org/10.1007/978-3-030-77817-0_25) · [open copy](https://arxiv.org/abs/2008.07643) | audio |  | other | monologue |  |
| HRI | [Toward a One-interaction Data-driven Guide: Putting Co-speech Gesture Evidence to Work for Ambiguous Route Instructions](https://doi.org/10.1145/3434074.3447223)† · [open copy](https://dl.acm.org/doi/pdf/10.1145/3434074.3447223) |  |  |  |  |  |
| ICASSP | [Double-DCCCAE: Estimation of Body Gestures From Speech Waveform](https://doi.org/10.1109/icassp39728.2021.9414660)† · [open copy](https://www.research.ed.ac.uk/en/publications/485da7e9-bae3-43dc-a697-5023f97d109f) | audio |  | other |  |  |
| ICCV | [Audio2Gestures: Generating Diverse Gestures from Speech Audio with Conditional Variational Autoencoders](https://doi.org/10.1109/iccv48922.2021.01110) · [open copy](https://arxiv.org/abs/2108.06720) · [project](https://jingli513.github.io/audio2gestures) | audio | upper-body, hands | vae | monologue |  |
| ICCV | [Speech Drives Templates: Co-Speech Gesture Synthesis with Learned Templates](https://openaccess.thecvf.com/content/ICCV2021/html/Qian_Speech_Drives_Templates_Co-Speech_Gesture_Synthesis_With_Learned_Templates_ICCV_2021_paper.html) · [open copy](https://arxiv.org/abs/2108.08020) | audio | upper-body, hands | other | monologue | [code](https://github.com/shenhanqian/speechdrivestemplates) |
| ICMI | [Integrated Speech and Gesture Synthesis](https://doi.org/10.1145/3462244.3479914) · [open copy](https://arxiv.org/abs/2108.11436) · [project](https://swatsw.github.io/isg_icmi21/) | text | upper-body | autoregressive, normalizing-flow | monologue |  |
| ICMI | [Probabilistic Human-like Gesture Synthesis from Speech using GRU-based WGAN](https://dl.acm.org/doi/abs/10.1145/3461615.3485407)† · [video](https://www.youtube.com/watch?v=PMhjX6cdIPE) | audio | upper-body | autoregressive, gan |  | [code](https://github.com/wubowen416/gesture-generation) |
| IEEE VR | [Passing a Non-verbal Turing Test: Evaluating Gesture Animations Generated from Speech](https://doi.org/10.1109/vr50410.2021.00082) · [open copy](https://arxiv.org/abs/2107.00712) | audio | upper-body | gan | monologue | [code](https://github.com/mrebol/Gestures-From-Speech) |
| IEEE VR | [Text2Gestures: A Transformer-Based Network for Generating Emotive Body Gestures for Virtual Agents](https://arxiv.org/abs/2101.11101) · [project](https://gamma.umd.edu/t2g) | text, emotion | full-body | other | monologue |  |
| IJHCI | [Moving Fast and Slow: Analysis of Representations and Post-Processing in Speech-Driven Automatic Gesture Generation](https://www.tandfonline.com/doi/full/10.1080/10447318.2021.1883883) · [open copy](https://arxiv.org/abs/2007.09170) | audio | upper-body, full-body | regression | monologue | [code](https://github.com/GestureGeneration/Speech_driven_gesture_generation_with_autoencoder) |
| International Journal of Computers and Communications | [TTS-driven Embodied Conversation Avatar for UMB-SmartTV](https://doi.org/10.46300/91013.2021.15.1) | text | upper-body, hands, face | rule-based | monologue |  |
| ISMAR-Adjunct | [ASAP: Auto-generating Storyboard And Previz with Virtual Humans](https://doi.org/10.1109/ismar-adjunct54149.2021.00071)† | text |  | hybrid |  |  |
| IVA | [Learning Speech-driven 3D Conversational Gestures from Video](https://dl.acm.org/doi/abs/10.1145/3472306.3478335) · [open copy](https://arxiv.org/abs/2102.06837) | audio | upper-body, hands, face | gan | monologue |  |
| IVA | [Speech2Properties2Gestures: Gesture-Property Prediction as a Tool for Generating Representational Gestures from Speech](https://doi.org/10.1145/3472306.3478333) · [open copy](https://arxiv.org/abs/2106.14736) · [project](https://svito-zar.github.io/speech2properties2gestures/) | text, audio |  | normalizing-flow | monologue |  |
| JIP | [Methods for Efficiently Constructing Text-dialogue-agent System using Existing Anime Characters](https://doi.org/10.2197/ipsjjip.29.30) · [open copy](https://www.jstage.jst.go.jp/article/ipsjjip/29/0/29_30/_pdf) | text | upper-body, hands | hybrid | monologue |  |
| Lecture Notes in Networks and Systems | [Towards Synchronous Model of Non-emotional Conversational Gesture Generation in Humanoids](https://doi.org/10.1007/978-3-030-80119-9_47)‡ |  |  |  |  |  |
| Multimed. Tools Appl. | [Modeling and evaluating beat gestures for social robots](https://doi.org/10.1007/s11042-021-11289-x)† · [open copy](https://link.springer.com/content/pdf/10.1007/s11042-021-11289-x.pdf) |  |  | gan |  |  |
| UIST | [SGToolkit: An Interactive Gesture Authoring Toolkit for Embodied Conversational Agents](https://doi.org/10.1145/3472749.3474789) · [open copy](https://arxiv.org/abs/2108.04636) | audio, text, speaker-id, style | upper-body | gan | monologue | [code](https://github.com/ai4r/SGToolkit) |

### 2020

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| ACCV | [Speech2Video Synthesis with 3D Skeleton Regularization and Expressive Body Poses](https://doi.org/10.1007/978-3-030-69541-5_19) · [open copy](https://arxiv.org/abs/2007.09198) · [video](https://youtu.be/MUlRtgbGeUs) | audio, text | full-body, hands, face | regression, gan | monologue |  |
| CAVW | [Automatic text‐to‐gesture rule generation for embodied conversational agents](https://onlinelibrary.wiley.com/doi/abs/10.1002/cav.1944)† · [video](https://www.youtube.com/watch?v=GIxaI9yTmMc) | text |  | rule-based |  |  |
| CGF | [Statistics-based Motion Synthesis for Social Conversations](https://doi.org/10.1111/cgf.14114)† | audio |  | retrieval | dyadic |  |
| CGF | [Style-Controllable Speech-Driven Gesture Synthesis Using Normalising Flows](https://doi.org/10.1111/cgf.13946)† · [open copy](http://urn.kb.se/resolve?urn=urn:nbn:se:kth:diva-279231) | audio, style | upper-body, full-body | normalizing-flow |  |  |
| Complexity | [Realistic Speech-Driven Talking Video Generation with Personalized Pose](https://doi.org/10.1155/2020/6629634)† · [open copy](https://downloads.hindawi.com/journals/complexity/2020/6629634.pdf) | audio | face |  | monologue |  |
| Computers & Graphics | [Adversarial gesture generation with realistic gesture phasing](https://doi.org/10.1016/j.cag.2020.04.007)† |  |  | gan |  |  |
| Dialogue | [FineMotion - Audio and Text-Driven approach for Conversational Gestures Generation](https://www.dialog-21.ru/media/5526/korzunvaplusdimovinpluszharkovaa031.pdf)‡ |  |  |  |  | [code](https://github.com/FineMotion/GENEA_2020) |
| ECCV | [Style Transfer for Co-Speech Gesture Animation: A Multi-Speaker Conditional-Mixture Approach](https://doi.org/10.1007/978-3-030-58523-5_15) · [open copy](https://arxiv.org/abs/2007.12553) · [project](https://chahuja.com/mix-stage) | audio, style | upper-body | gan | monologue | [code](https://github.com/chahuja/pats) |
| EMNLP Findings | [No Gestures Left Behind: Learning Relationships between Spoken Language and Freeform Gestures](https://aclanthology.org/2020.findings-emnlp.170) | text, audio | upper-body, hands | gan | monologue | [code](https://github.com/chahuja/aisle) |
| ICARCV | [SRG3: Speech-driven Robot Gesture Generation with GAN](https://doi.org/10.1109/icarcv50220.2020.9305330)† · [open copy](https://hal.science/hal-03047565) | audio |  | gan |  |  |
| ICMI | [Gesticulator: A framework for semantically-aware speech-driven gesture generation](https://doi.org/10.1145/3382507.3418815) · [open copy](https://arxiv.org/abs/2001.09326) · [project](https://svito-zar.github.io/gesticulator/) | text, audio | upper-body | autoregressive | monologue | [code](https://github.com/Svito-zar/gesticulator) |
| IVA | [Generating coherent spontaneous speech and gesture from text](https://doi.org/10.1145/3383652.3423874) · [open copy](https://arxiv.org/abs/2101.05684) · [project](https://simonalexanderson.github.io/IVA2020/) · [video](https://www.youtube.com/watch?v=4_Gq9rU_yWg) | text | full-body, hands, locomotion | normalizing-flow, autoregressive | monologue |  |
| IVA | [Impact of Personality on Nonverbal Behavior Generation](https://doi.org/10.1145/3383652.3423908)† | text |  |  |  |  |
| IVA | [Understanding the Predictability of Gesture Parameters from Speech and their Perceptual Importance](https://doi.org/10.1145/3383652.3423882) · [open copy](https://arxiv.org/abs/2010.00995) · [video](https://youtu.be/aw6-_5kmLjY) | audio | hands | regression | monologue |  |
| PRESENCE | [A Live Speech-Driven Avatar-Mediated Three-Party Telepresence System: Design and Evaluation](https://doi.org/10.1162/pres_a_00358)† | audio | upper-body, hands, face |  | multi-party |  |
| RO-MAN | [Conditional Generative Adversarial Network for Generating Communicative Robot Gestures](https://doi.org/10.1109/ro-man47096.2020.9223498) · [open copy](https://dspace.jaist.ac.jp/dspace/bitstream/10119/16930/1/3336.pdf) | text | upper-body | gan |  |  |
| Speech Communication | [Affective synthesis and animation of arm gestures from speech prosody](https://doi.org/10.1016/j.specom.2020.02.005)† | audio, emotion | upper-body | other | monologue |  |
| TCYB | [Audio-Driven Robot Upper-Body Motion Synthesis](https://doi.org/10.1109/tcyb.2020.2966730) · [open copy](https://www.repository.cam.ac.uk/handle/1810/301038) | audio | upper-body | regression | monologue | [code](https://github.com/jancio/Audio-driven-upper-body-motion-synthesis) |
| TOG | [Speech Gesture Generation from the Trimodal Context of Text, Audio, and Speaker Identity](https://doi.org/10.1145/3414685.3417838) · [open copy](https://arxiv.org/abs/2009.02119) | text, audio, speaker-id | upper-body | gan | monologue | [code](https://github.com/ai4r/Gesture-Generation-from-Trimodal-Context) |
| UR | [Learning from Humans to Generate Communicative Gestures for Social Robots](https://doi.org/10.1109/ur49135.2020.9144985) · [open copy](https://dspace.jaist.ac.jp/dspace/bitstream/10119/16711/1/C1_UR20_0013_FI.pdf) | text | upper-body | gan |  |  |

### 2019

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| AAMAS | [On the Importance of Representations for Speech-Driven Gesture Generation](https://www.ifaamas.org/Proceedings/aamas2019/pdfs/p2072.pdf) · [open copy](http://urn.kb.se/resolve?urn=urn:nbn:se:kth:diva-251460) | audio | upper-body | regression | monologue | [code](https://github.com/GestureGeneration/Speech_driven_gesture_generation_with_autoencoder) |
| CVPR | [Learning Individual Styles of Conversational Gesture](https://arxiv.org/abs/1906.04160) · [project](http://people.eecs.berkeley.edu/~shiry/speech2gesture) | audio | upper-body, hands | regression, gan | monologue | [code](https://github.com/amirbar/speech2gesture) |
| Humanoids | [Online processing for speech-driven gesture motion generation in android robots](https://doi.org/10.1109/humanoids43949.2019.9035066)† | audio |  |  |  |  |
| ICMI | [Coalescing Narrative and Dialogue for Grounded Pose Forecasting](https://doi.org/10.1145/3340555.3356090)† |  |  |  |  |  |
| ICMI | [Determining Iconic Gesture Forms based on Entity Image Representation](https://doi.org/10.1145/3340555.3353736)† · [open copy](https://dl.acm.org/doi/pdf/10.1145/3340555.3353736) | image |  |  |  |  |
| ICMI | [To React or not to React: End-to-End Visual Pose Forecasting for Personalized Avatar during Dyadic Conversations](https://doi.org/10.1145/3340555.3353725)† · [open copy](https://dl.acm.org/doi/pdf/10.1145/3340555.3353725) | audio, interlocutor |  |  | dyadic |  |
| ICRA | [Robots Learn Social Skills: End-to-End Learning of Co-Speech Gesture Generation for Humanoid Robots](https://doi.org/10.1109/icra.2019.8793720)† · [open copy](https://arxiv.org/abs/1810.12541) · [project](https://sites.google.com/view/youngwoo-yoon/projects/co-speech-gesture-generation) | text |  |  |  |  |
| ICSR | [Learning to gesticulate by observation using a deep generative approach](https://doi.org/10.1007/978-3-030-35888-4_62) · [open copy](https://arxiv.org/abs/1909.01768) |  | upper-body, hands | gan |  |  |
| IEEE TLT | [Automatic Deictic Gestures for Animated Pedagogical Agents](https://doi.org/10.1109/tlt.2019.2922134)† | text, audio |  | rule-based |  |  |
| IROS | [Towards More Realistic Human-Robot Conversation: A Seq2Seq-based Body Gesture Interaction System](https://doi.org/10.1109/iros40897.2019.8968038) · [open copy](https://arxiv.org/abs/1905.01641) | text, interlocutor | upper-body | autoregressive | dyadic |  |
| IVA | [Analyzing Input and Output Representations for Speech-Driven Gesture Generation](https://arxiv.org/abs/1903.03369) · [project](https://svito-zar.github.io/audio2gestures/) | audio | upper-body, hands | regression | monologue | [code](https://github.com/GestureGeneration/Speech_driven_gesture_generation_with_autoencoder) |
| IVA | [Gesture Class Prediction by Recurrent Neural Network and Attention Mechanism](https://doi.org/10.1145/3308532.3329458)† · [open copy](https://hal.science/hal-02382428) | audio |  |  |  |  |
| J Intell Robot Syst | [Part-of-Speech and Prosody-based Approaches for Robot Speech and Gesture Synchronization](https://doi.org/10.1007/s10846-019-01100-3)‡ |  |  |  |  |  |
| MIG | [Multi-objective adversarial gesture generation](https://dl.acm.org/doi/abs/10.1145/3359566.3360053)† | audio |  | gan |  |  |
| RAS | [Spontaneous talking gestures using Generative Adversarial Networks](https://doi.org/10.1016/j.robot.2018.11.024)† · [open copy](http://hdl.handle.net/10810/71576) |  | upper-body | gan |  |  |
| RO-MAN | [Automatic Speech-Gesture Mapping and Engagement Evaluation in Human Robot Interaction](https://doi.org/10.1109/ro-man46459.2019.8956462) · [open copy](https://arxiv.org/abs/1812.03484) · [video](https://youtu.be/Ws3G2M6aLto) | audio, text | upper-body, hands | other | monologue |  |
| Speech Communication | [Speech-driven Animation with Meaningful Behaviors](https://doi.org/10.1016/j.specom.2019.04.005) · [open copy](https://arxiv.org/abs/1708.01640) | audio | upper-body | other | monologue |  |
| TJSAI | [Speech-to-Gesture Generation Using Bi-Directional LSTM Network](https://doi.org/10.1527/tjsai.c-j41)† · [open copy](https://www.jstage.jst.go.jp/article/tjsai/34/6/34_C-J41/_pdf) | audio |  | regression |  |  |

### 2018

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| AAMAS | [Automatic Nonverbal Behavior Generation from Image Schemas](https://ifaamas.org/Proceedings/aamas2018/pdfs/p1667.pdf)† · [open copy](https://telecom-paris.hal.science/hal-02287759) |  |  |  |  |  |
| Frontiers in Psychology | [Automating the Production of Communicative Gestures in Embodied Characters](https://doi.org/10.3389/fpsyg.2018.01144) · [open copy](https://www.frontiersin.org/articles/10.3389/fpsyg.2018.01144/pdf) | text |  | rule-based |  |  |
| ICMI | [Data Driven Non-Verbal Behavior Generation for Humanoid Robots](https://dl.acm.org/doi/10.1145/3242969.3264970)† |  |  |  |  |  |
| IVA | [Automatic Generation System of Virtual Agent's Motion using Natural Language](https://doi.org/10.1145/3267851.3267869)† | text | upper-body, hands, face |  |  |  |
| IVA | [Evaluation of Speech-to-Gesture Generation Using Bi-Directional LSTM Network](https://dl.acm.org/doi/abs/10.1145/3267851.3267878)† | audio |  | regression |  |  |
| IVA | [Generating Body Motions using Spoken Language in Dialogue](https://doi.org/10.1145/3267851.3267866)† | text | upper-body, hands, face |  |  |  |
| IVA | [Investigating the use of recurrent motion modelling for speech gesture generation](https://doi.org/10.1145/3267851.3267898)† | audio |  |  |  |  |
| RA-L | [A Speech-Driven Hand Gesture Generation Method and Evaluation in Android Robots](https://doi.org/10.1109/lra.2018.2856281)† | text, audio | hands |  |  |  |
| RO-MAN | [Generation of Gestures During Presentation for Humanoid Robots](https://doi.org/10.1109/roman.2018.8525621)† | audio |  | regression | monologue |  |
| WSEAS Trans. Environ. Dev. | [A Novel Realizer of Conversational Behavior for Affective and Personalized Human Machine Interaction - EVA U-Realizer](https://www.wseas.org/multimedia/journals/environment/2018/a185915-aal.pdf)† |  |  |  |  |  |

### 2017

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| HAI | [Speech-to-Gesture Generation](https://doi.org/10.1145/3125739.3132594)† | audio |  | regression |  |  |
| International Journal of Computers | [A Novel Unity-based Realizer for the Realization of Conversational Behavior on Embodied Conversational Agents](https://www.iaras.org/iaras/home/cijc/a-novel-unity-based-realizer-for-the-realization-of-conversational-behavior-on-embodied-conversational-agents)† |  |  |  |  |  |
| Max Planck Digital Library | [Automatic Gesture Generation for Virtual Humans with Deep and Temporal Learning](https://hdl.handle.net/21.11116/0000-0000-C574-F)† |  |  |  |  |  |
| TAC | [A Methodology for the Automatic Extraction and Generation of Non-Verbal Signals Sequences Conveying Interpersonal Attitudes](https://doi.org/10.1109/taffc.2017.2753777)† · [open copy](http://eprints.gla.ac.uk/269794/) |  |  |  |  |  |

### 2016

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| CAVW | [Walk the talk: coordinating gesture with locomotion for conversational characters](https://doi.org/10.1002/cav.1703)† | seed-motion | full-body, locomotion |  | dyadic |  |
| CogSci | [From embodied metaphors to metaphoric gestures.](https://escholarship.org/uc/item/4w03x8cs)† |  |  |  |  |  |
| Eng. Appl. Artif. Intell. | [The TTS-driven affective embodied conversational agent EVA, based on a novel conversational-behavior generation algorithm](https://doi.org/10.1016/j.engappai.2016.10.006)‡ |  |  |  |  |  |
| HRI | [Generating iconic gestures based on graphic data analysis and clustering](https://doi.org/10.1109/hri.2016.7451799)† | text | hands |  |  |  |
| IROS | [Motion generation in android robots during laughing speech](https://doi.org/10.1109/iros.2016.7759512)† | audio | upper-body, face |  |  |  |
| SIU | [Real-time speech driven gesture animation](https://doi.org/10.1109/siu.2016.7496140)† | audio |  |  |  |  |
| Speech Communication | [Multimodal analysis of speech and arm motion for prosody-driven synthesis of beat gestures](https://doi.org/10.1016/j.specom.2016.10.004)‡ |  |  |  |  |  |

### 2015

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| AAAI | [Cerebella: Automatic Generation of Nonverbal Behavior for Virtual Humans](https://ojs.aaai.org/index.php/AAAI/article/view/9778) | text, audio | upper-body, hands, face | rule-based | monologue |  |
| AAMAS | [Greta: an Interactive Expressive Embodied Conversational Agent](http://www.ifaamas.org/Proceedings/aamas2015/aamas/p5.pdf)† |  |  |  |  |  |
| ACII | [Effects of a robotic storyteller's moody gestures on storytelling perception](https://doi.org/10.1109/acii.2015.7344609)† |  |  |  |  |  |
| Autonomous Robots | [Towards an intelligent system for generating an adapted verbal and nonverbal combined behavior in human–robot interaction](https://doi.org/10.1007/s10514-015-9444-1)‡ · [open copy](https://hal.science/hal-01203658) |  |  |  |  |  |
| ICME | [Affect-expressive hand gestures synthesis and animation](https://doi.org/10.1109/icme.2015.7177478)† | audio | hands | other | monologue |  |
| ICMI | [Retrieving Target Gestures Toward Speech Driven Animation with Meaningful Behaviors](https://doi.org/10.1145/2818346.2820750)† | audio |  | retrieval, other |  |  |
| IROS | [Multimodal adapted robot behavior synthesis within a narrative human-robot interaction](https://doi.org/10.1109/iros.2015.7353789)† · [open copy](https://hal.science/hal-01203696) |  | upper-body, face |  |  |  |
| IVA | [Predicting Co-verbal Gestures: A Deep and Temporal Modeling Approach](https://doi.org/10.1007/978-3-319-21996-7_17)† | text, audio |  | other |  |  |
| Lecture Notes in Computer Science | [Developing Embodied Agents for Education Applications with Accurate Synchronization of Gesture and Speech](https://doi.org/10.1007/978-3-319-27543-7_1)‡ |  |  |  |  |  |

### 2014

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| AAMAS | [Gesture generation with low-dimensional embeddings](https://dl.acm.org/citation.cfm?id=2615857)† | audio | hands |  |  |  |
| ACM | [Data-Driven Model of Nonverbal Behavior for Socially Assistive Human-Robot Interactions](https://doi.org/10.1145/2663204.2663263)† |  |  |  |  |  |
| Applied Artificial Intelligence | [Describing and Animating Complex Communicative Verbal and Nonverbal Behavior Using Eva-Framework](https://doi.org/10.1080/08839514.2014.905819)† |  |  | rule-based |  |  |
| HRI | [Learning-based modeling of multimodal behaviors for humanlike robots](https://doi.org/10.1145/2559636.2559668)† |  |  | other |  |  |
| ICMI | [Authoring Communicative Behaviors for Situated, Embodied Characters](https://doi.org/10.1145/2663204.2667576)† |  | upper-body, hands | hybrid |  |  |
| IVA | [Compound Gesture Generation: A Model Based on Ideational Units](https://doi.org/10.1007/978-3-319-09767-1_58)‡ |  |  |  |  |  |
| SCITEPRESS | [Accurate Synchronization of Gesture and Speech for Conversational Agents using Motion Graphs](https://doi.org/10.5220/0004748400050014)† |  |  |  |  |  |
| URAI | [Robotic gesture generation based on a cognitive basis for non-verbal communication](https://doi.org/10.1109/urai.2014.7057497)† |  |  |  |  |  |

### 2013

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| Book chapter | [Co-speech Gesture Generation for Embodied Agents and its Effects on User Evaluation](https://doi.org/10.1201/b15477-10)‡ |  |  |  |  |  |
| CRC Press | [TTS-Driven Synthetic Behavior Generation Model for Embodied Conversational Agents](https://doi.org/10.1201/b15477-14)‡ |  |  |  |  |  |
| HRI | [A model for synthesizing a combined verbal and nonverbal behavior based on personality traits in human-robot interaction](https://doi.org/10.1109/hri.2013.6483606)† · [open copy](https://hal.science/hal-01284708) | text |  | rule-based |  |  |
| HRI | [Generating finely synchronized gesture and speech for humanoid robots: a closed-loop approach](https://dl.acm.org/doi/10.5555/2447556.2447646)† |  |  |  |  |  |
| ICAR | [Prosody-based adaptive metaphoric head and arm gestures synthesis in human robot interaction](https://doi.org/10.1109/icar.2013.6766507)† · [open copy](https://hal.science/hal-01180239) | audio | upper-body | other |  |  |
| ICASSP | [Multimodal analysis of speech prosody and upper body gestures using hidden semi-Markov models](https://doi.org/10.1109/icassp.2013.6638339)† | audio | upper-body |  |  |  |
| ICASSP | [Toward body language generation in dyadic interaction settings from interlocutor multimodal cues](https://doi.org/10.1109/icassp.2013.6638361)† | audio, interlocutor |  | regression | dyadic |  |
| ICMI | [Designing effective multimodal behaviors for robots](https://doi.org/10.1145/2522848.2532189)† |  |  | other |  |  |
| ICSR | [Closing the Loop: Towards Tightly Synchronized Robot Gesture and Speech](https://doi.org/10.1007/978-3-319-02675-6_38)‡ |  |  |  |  |  |
| IJARS | [TTS-Driven Synthetic Behaviour-Generation Model for Artificial Bodies](https://doi.org/10.5772/56870)† | text |  |  |  |  |
| IVA | [Modeling the Semantic Coordination of Speech and Gesture under Cognitive and Linguistic Constraints](https://doi.org/10.1007/978-3-642-40415-3_18)‡ · [open copy](https://pub.uni-bielefeld.de/record/2610719) |  |  |  |  |  |
| RSS | [Modeling and Evaluating Narrative Gestures for Humanlike Robots](https://doi.org/10.15607/rss.2013.ix.026)† |  |  |  |  |  |
| SCA | [Virtual character performance from speech](https://doi.org/10.1145/2485895.2485900)† | audio, text |  | rule-based |  |  |
| SIU | [Speech rhythm-driven gesture animation](https://doi.org/10.1109/siu.2013.6531352)† | audio |  |  |  |  |
| Speech Communication | [Gesture synthesis adapted to speech emphasis](https://doi.org/10.1016/j.specom.2013.06.005)‡ |  |  |  |  |  |

### 2012

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| CCIS | [Multimodal emotion estimation and emotional synthesize for interaction virtual agent](https://doi.org/10.1109/ccis.2012.6664394)† |  |  | rule-based, retrieval |  |  |
| CogInfoCom | [Integration of gestures and speech in human-robot interaction](https://doi.org/10.1109/coginfocom.2012.6421936)† |  | upper-body, hands |  |  |  |
| HRI | [Prosody-driven robot ARM gestures generation in human-robot interaction](https://doi.org/10.1145/2157689.2157783)† · [open copy](https://hal.science/hal-01265938) | audio | upper-body | other |  |  |
| ICAI | [Recreation of spontaneous non-verbal behavior on a synthetic agent EVA](http://dl.acm.org/citation.cfm?id=2183105)† | text | upper-body, hands, face | retrieval |  |  |
| ICMI | [A Common Gesture and Speech Production Framework for Virtual and Physical Agents](https://www.semanticscholar.org/paper/A-Common-Gesture-and-Speech-Production-Framework-L%C3%AA-Huang/6e4fc97e4ac99de2fdab755befc675f54970b9bb)‡ |  |  |  |  |  |
| IFAC | [An Integrated Model of Speech to Arm Gestures Mapping in Human-Robot Interaction](https://doi.org/10.3182/20120523-3-ro-2023.00364)† · [open copy](https://ensta.hal.science/hal-01169980) | audio | upper-body | other |  |  |
| IJSR | [Generation and Evaluation of Communicative Robot Gesture](https://doi.org/10.1007/s12369-011-0124-9)‡ · [open copy](https://pub.uni-bielefeld.de/record/2301142) |  |  |  |  |  |
| Industrial Robot | [Gesture encoding and reproduction for human‐robot interaction in text‐to‐gesture systems](https://doi.org/10.1108/01439911211268705)† | text |  | rule-based |  |  |
| LNCS | [Generating Co-speech Gestures for the Humanoid Robot NAO through BML](https://doi.org/10.1007/978-3-642-34182-3_21)‡ · [open copy](https://imt.hal.science/hal-01113951) |  |  |  |  |  |
| RO-MAN | [Modeling and composing gestures for human-robot interaction](https://doi.org/10.1109/roman.2012.6343739)† | text |  |  |  |  |
| SII | [Automated robot speech gesture generation system based on dialog sentence punctuation mark extraction](https://doi.org/10.1109/sii.2012.6427293)† | text, audio |  | rule-based |  |  |
| Studies in Computational Intelligence | [Individualized Gesture Production in Embodied Conversational Agents](https://doi.org/10.1007/978-3-642-25691-2_12)‡ |  |  |  |  |  |
| TOG | [Data-driven finger motion synthesis for gesturing characters](https://doi.org/10.1145/2366145.2366208)† |  | hands | retrieval |  |  |

### 2011

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| ACM | [Cross-media agent platform](https://doi.org/10.1145/2010425.2010428)† |  |  |  |  |  |
| ALTA Workshop | [ENGAGE: Automated Gestures for Animated Characters](https://aclanthology.org/U11-1021/)† | text |  | rule-based |  |  |
| Gesture Workshop | [A Multimodal Scheduler for Synchronized Humanoid Robot Gesture and Speech](https://pub.uni-bielefeld.de/record/2301145)† |  | upper-body, hands |  |  |  |
| Humanoids | [Converting emotional voice to motion for robot telepresence](https://doi.org/10.1109/humanoids.2011.6100891)† | audio, emotion |  |  |  |  |
| Humanoids | [Design and implementation of an expressive gesture model for a humanoid robot](https://doi.org/10.1109/humanoids.2011.6100857)† · [open copy](https://hal.science/hal-00730800) | text | upper-body | rule-based, retrieval |  |  |
| Int. J. Mathematics and Computers in Simulation | [EVA: expressive multipart virtual agent performing gestures and emotions](https://dk.um.si/IzpisGradiva.php?id=27297)† |  |  |  |  |  |
| IVA | [How to Train Your Avatar: A Data Driven Approach to Gesture Generation](https://doi.org/10.1007/978-3-642-23974-8_14)‡ |  |  |  |  |  |
| LNCS | [Expressive Gesture Model for Humanoid Robot](https://doi.org/10.1007/978-3-642-24571-8_24)‡ |  |  |  |  |  |
| SIGDIAL | [Regulating Dialogue with Gestures - Towards an Empirically Grounded Simulation with Conversational Agents](https://pub.uni-bielefeld.de/record/2097157)† |  |  |  |  |  |

### 2010

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| AAMAS | [Adaptive expressiveness: virtual conversational agents that can align to their interaction partner](https://doi.org/10.5555/1838206.1838219)† · [open copy](https://pub.uni-bielefeld.de/download/1901698/2315033) |  |  |  |  |  |
| Applied Artificial Intelligence | [Modeling the Production of Coverbal Iconic Gestures by Learning Bayesian Decision Networks](https://doi.org/10.1080/08839514.2010.492162)† |  |  | other |  |  |
| Applied Artificial Intelligence | [REAL-TIME ANIMATION OF INTERACTIVE AGENTS: SPECIFICATION AND REALIZATION](https://doi.org/10.1080/08839514.2010.492161)† · [open copy](https://www.tandfonline.com/doi/pdf/10.1080/08839514.2010.492161?needAccess=true&role=button) |  |  |  |  |  |
| ICAIR | [Generating multi-modal robot behavior based on a virtual agent framework](https://pub.uni-bielefeld.de/record/1991216)† | text |  | rule-based |  |  |
| IROS | [Easy development of communicative behaviors in social robots](https://doi.org/10.1109/iros.2010.5650128)† | text |  | rule-based |  |  |
| IROS | [Generating robot gesture using a virtual agent framework](https://doi.org/10.1109/iros.2010.5650572)† |  |  |  |  |  |
| IROS | [Synchronized gesture and speech production for humanoid robots](https://doi.org/10.1109/iros.2010.5654322)† | text |  | rule-based |  |  |
| IVA | [Generating Culture-Specific Gestures for Virtual Agent Dialogs](https://doi.org/10.1007/978-3-642-15892-6_34) · [open copy](https://vbn.aau.dk/ws/files/42310627/Endrass_et_al_2010_Generating_culture_specific_gesturs_for_virtual_agent_dialogs.pdf) | text | upper-body | rule-based | dyadic |  |
| JMUI | [Elckerlyc - A BML Realizer for continuous, multimodal interaction with a Virtual Human](https://doi.org/10.1007/s12193-010-0051-3)† · [open copy](https://link.springer.com/content/pdf/10.1007/s12193-010-0051-3.pdf) |  |  | hybrid |  |  |
| MTAP | [Multimodal behavior realization for embodied conversational agents](https://doi.org/10.1007/s11042-010-0530-2)‡ |  |  |  |  |  |
| RO-MAN | [Towards an integrated model of speech and gesture production for multi-modal robot behavior](https://doi.org/10.1109/roman.2010.5598665)† |  |  |  |  |  |
| TOG | [Gesture controllers](https://doi.org/10.1145/1778765.1778861)† | audio |  | retrieval |  |  |

### 2009

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| AAMAS | [Increasing the expressiveness of virtual agents: autonomous generation of speech and gesture for spatial description tasks](https://doi.org/10.65109/vtam7538)† · [open copy](https://www.ifaamas.org/Proceedings/aamas09/pdf/01_Full%20Papers/05a_11_62_FP_0551.pdf) |  |  |  |  |  |
| Cognitive Systems Monographs | [Towards Meaningful Robot Gesture](https://doi.org/10.1007/978-3-642-10403-9_18)‡ |  |  |  |  |  |
| CogSci | [The Multimodal Nature of Embodied Conversational Agents](https://escholarship.org/uc/item/6078d8kn) |  |  | rule-based | dyadic |  |
| Gesture Workshop | [Systematicity and Idiosyncrasy in Iconic Gesture Use: Empirical Analysis and Computational Modeling](https://doi.org/10.1007/978-3-642-12553-9_16)‡ |  |  |  |  |  |
| HRI | [Providing route directions](https://doi.org/10.1145/1514095.1514108)† |  |  |  |  |  |
| IVA | [Augmenting Gesture Animation with Motion Capture Data to Provide Full-Body Engagement](https://doi.org/10.1007/978-3-642-04380-2_44)‡ |  |  |  |  |  |
| IVA | [GNetIc – Using Bayesian Decision Networks for Iconic Gesture Generation](https://doi.org/10.1007/978-3-642-04380-2_12)‡ |  |  |  |  |  |
| LNCS | [Automatic Generation of Non-verbal Behavior for Agents in Virtual Worlds: A System for Supporting Multimodal Conversations of Bots and Avatars](https://doi.org/10.1007/978-3-642-02774-1_17)‡ |  |  |  |  |  |
| LNCS | [RealActor: Character Animation and Multimodal Behavior Realization System](https://doi.org/10.1007/978-3-642-04380-2_55)‡ |  |  |  |  |  |
| Oxford University Press | [Knowledge Representation for Generating Locating Gestures in Route Directions](https://doi.org/10.1093/acprof:oso/9780199554201.003.0011)† |  |  |  |  |  |
| RO-MAN | [Beat gesture generation rules for human-robot interaction](https://doi.org/10.1109/roman.2009.5326136)† · [open copy](https://uwe-repository.worktribe.com/output/11628114) |  |  | rule-based |  |  |
| Speech Communication | [Studies on gesture expressivity for a virtual agent](https://doi.org/10.1016/j.specom.2008.04.009)† |  |  |  |  |  |
| TOG | [Real-time prosody-driven synthesis of body language](https://doi.org/10.1145/1618452.1618518)† | audio |  | retrieval |  |  |

### 2008

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| AAMAS | [SmartBody: behavior realization for embodied conversational agents](https://doi.org/10.5555/1402383.1402409)† · [open copy](http://graphics.ucmerced.edu/publications/2008_AAMAS_Thiebaux.pdf) |  |  | rule-based |  |  |
| Bielefeld University | [Multimodal Content Representation for Speech and Gesture Production](https://pub.uni-bielefeld.de/record/1857839)† |  |  |  |  |  |
| BNAIC | [Multimodal Interaction with a Virtual Guide](https://research.utwente.nl/en/publications/33f29040-8b9f-4fd3-b5f3-89390f90d8f4)† · [open copy](https://ris.utwente.nl/ws/files/5320053/bnaic08-Hofs-Theune-Akker.pdf) |  |  |  |  |  |
| IJSC | [Automatic generation of gaze and gestures for dialogues between embodied conversational agents](https://doi.org/10.1142/s1793351x0800035x)† | text |  |  |  |  |
| IJSC | [MULTIMODAL COMMUNICATION FROM MULTIMODAL THINKING — TOWARDS AN INTEGRATED MODEL OF SPEECH AND GESTURE PRODUCTION](https://doi.org/10.1142/s1793351x08000361)† · [open copy](https://pub.uni-bielefeld.de/record/2001891) |  |  |  |  |  |
| IJSC | [THE ROLE OF GESTURE IN DOCUMENT EXPLANATION BY EMBODIED CONVERSATIONAL AGENTS](https://doi.org/10.1142/s1793351x08000348)† |  | hands |  |  |  |
| MOG | [How Do I Address You? Modelling addressing behavior based on an analysis of a multi-modal corpora of conversational discourse](https://wwwhome.ewi.utwente.nl/~theune/PUBS/mog2008_addressing.pdf)† |  |  |  | multi-party |  |
| Studies in Computational Intelligence | [Modeling Gesticulation Expression in Virtual Humans](https://doi.org/10.1007/978-3-540-79868-2_5)‡ |  |  |  |  |  |
| TOG | [Gesture modeling and animation based on a probabilistic re-creation of speaker style](https://doi.org/10.1145/1330511.1330516)† | text | full-body |  |  |  |

### 2007

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| ACM | [Automated generation of non-verbal behavior for virtual embodied characters](https://doi.org/10.1145/1322192.1322247)† | text |  |  | dyadic |  |
| Interspeech | [The virtual guide: a direction giving embodied conversational agent](https://doi.org/10.21437/interspeech.2007-598)† · [open copy](https://research.utwente.nl/en/publications/2227363b-d1e3-4b9f-81c8-99ac83f3a6d3) |  |  |  |  |  |
| IVA | [The Behavior Markup Language: Recent Developments and Challenges](https://doi.org/10.1007/978-3-540-74997-4_10)† · [open copy](https://research.utwente.nl/en/publications/ad10f522-6273-4500-b758-0814e59540e6) |  |  |  |  |  |
| IVA | [Towards an Architecture for Aligned Speech and Gesture Production](https://doi.org/10.1007/978-3-540-74997-4_53)‡ |  |  |  |  |  |
| IVA | [Towards Natural Gesture Synthesis: Evaluating Gesture Units in a Data-Driven Approach to Gesture Synthesis](https://doi.org/10.1007/978-3-540-74997-4_2)‡ |  |  |  |  |  |
| RO-MAN | [Automatic Generation of Conversational Robot Gestures for Human-friendly Steward Robot](https://doi.org/10.1109/roman.2007.4415254)† | text | upper-body | rule-based |  |  |
| Systems and Computers in Japan | [Composite conversation gesture synthesis using layered planning](https://doi.org/10.1002/scj.20532)† | text |  |  |  |  |
| Wiley | [Trading Spaces: How Humans and Humanoids Use Speech and Gesture to Give Directions](https://doi.org/10.1002/9780470512470.ch8)‡ |  |  |  |  |  |

### 2006

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| Gesture Workshop | [Implementing Expressive Gesture Synthesis for Embodied Conversational Agents](https://doi.org/10.1007/11678816_22)‡ |  |  |  |  |  |
| ICME | [Combined Gesture-Speech Analysis and Speech Driven Gesture Synthesis](https://doi.org/10.1109/icme.2006.262663)† | audio |  |  |  |  |
| IJHR | [MULTIMODAL COMPLEX EMOTIONS: GESTURE EXPRESSIVITY AND BLENDED FACIAL EXPRESSIONS](https://doi.org/10.1142/s0219843606000825)† · [open copy](https://hal.science/hal-00787584/document) |  |  |  |  |  |
| IV | [Real Time Multimodal Interaction with Animated Virtual Human](https://doi.org/10.1109/iv.2006.88)† | text |  | hybrid |  |  |
| IVA | [Nonverbal Behavior Generator for Embodied Conversational Agents](https://doi.org/10.1007/11821830_20)† | text, emotion |  | rule-based |  |  |
| IVA | [Towards a Common Framework for Multimodal Generation: The Behavior Markup Language](https://doi.org/10.1007/11821830_17)‡ |  |  |  |  |  |
| Lecture Notes in Computer Science | [Automated Gesturing for Embodied Agents](https://doi.org/10.1007/11780496_42)‡ |  |  |  |  |  |
| Lecture notes in computer science | [Gesture Expressivity Modulations in an ECA Application](https://doi.org/10.1007/11821830_15)† |  |  |  |  |  |
| LNCS | [Creativity Meets Automation: Combining Nonverbal Action Authoring with Rules and Machine Learning](https://doi.org/10.1007/11821830_19)‡ |  |  |  |  |  |
| Revue d'intelligence artificielle | [Conception et évaluation d'un modèle d'expressivité pour les gestes des agents conversationnels](https://doi.org/10.3166/ria.20.621-638)† |  |  |  |  |  |

### 2005

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| AAMAS | [Design and evaluation of expressive gesture synthesis for embodied conversational agents](https://dl.acm.org/doi/10.1145/1082473.1082640)† |  |  |  |  |  |
| ACM MM | [Multimodal expressive embodied conversational agents](https://doi.org/10.1145/1101149.1101301)† |  |  |  |  |  |
| ENLG | [Incremental Generation of Multimodal Deixis Referring to Objects](https://pub.uni-bielefeld.de/record/2610742)† |  |  |  |  |  |
| eNTERFACE | [Combined Gesture-Speech Analysis and Synthesis](http://www.enterface.net/enterface05/docs/results/reports/project1.pdf)† | audio |  |  |  |  |
| HICSS | [Augmenting Online Conversation through Automated Discourse Tagging](https://doi.org/10.1109/hicss.2005.109)† | text |  |  |  |  |
| IJHCS | [Variations in gesturing and speech by GESTYLE](https://doi.org/10.1016/j.ijhcs.2004.11.007)† | text, style | hands, face |  |  |  |
| IUI | [Animating an interactive conversational character for an educational game system](https://doi.org/10.1145/1040830.1040872)† |  |  |  |  |  |

### 2004

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| AAMAS | [Content in Context: Generating Language and Iconic Gestures without a Gestionary](https://pub.uni-bielefeld.de/record/1857798) · [open copy](http://www.justinecassell.com/publications/AAMAS04.Tepper%20et%20al.pdf) |  | hands | rule-based |  |  |
| ACL | [Converting text into agent animations](https://doi.org/10.3115/1613984.1614023)† | text |  |  |  |  |
| CAVW | [Synthesizing multimodal utterances for conversational agents](https://doi.org/10.1002/cav.6)† |  | hands, face |  |  |  |
| ICMI | [Towards integrated microplanning of language and iconic gesture for multimodal output](https://doi.org/10.1145/1027933.1027952)† |  | hands |  |  |  |
| INLG | [Situated generation of multimodal deixis in task-oriented dialogue](https://pub.uni-bielefeld.de/record/2611049) · [open copy](http://www.techfak.uni-bielefeld.de/ags/wbski/veroeffentlichungen/download/INLG04_abstract.pdf) | text | hands | rule-based | dyadic |  |
| SCA | [Graceful Degradation of Hand Gestures](https://research.utwente.nl/en/publications/0e441751-9102-4a00-903f-11d2d750150a) · [open copy](https://ris.utwente.nl/ws/files/26331096/Graceful_Degradation_of_Hand_Gestures.pdf) | text | hands | rule-based |  |  |
| TOG | [Speaking with hands](https://doi.org/10.1145/1015706.1015753)† |  |  |  |  |  |

### 2003

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| JSAI | [Gestures Realization for Embodied Conversational Agents](https://ci.nii.ac.jp/naid/130004653274)‡ |  |  |  |  |  |
| KI | [Max - A multimodal assistant in virtual reality construction](https://pub.uni-bielefeld.de/record/2001896)† |  |  |  |  |  |

### 2002

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| Bielefeld PUB | [MURML: A Multimodal Utterance Representation Markup Language for Conversational Agents](https://pub.uni-bielefeld.de/record/1857788)† |  |  |  |  |  |
| CA | [Formational parameters and adaptive prototype instantiation for MPEG-4 compliant gesture synthesis](https://doi.org/10.1109/ca.2002.1017516)† | text | upper-body, hands | rule-based |  |  |
| CA | [Model-based animation of co-verbal gesture](https://doi.org/10.1109/ca.2002.1017547)† |  | upper-body, hands | rule-based |  |  |
| Eurographics Workshop on Virtual Environments | [Avatar Markup Language](https://diglib.eg.org/items/73cc35d6-df6a-401e-8703-c466a6ecf7e0)† |  |  |  |  |  |
| GW | [Lifelike Gesture Synthesis and Timing for Conversational Agents](https://doi.org/10.1007/3-540-47873-6_13)† | text | upper-body, hands | rule-based |  |  |
| KONVENS | [Generation of multi-modal dialogue for a net environment](https://oro.open.ac.uk/3189/1/konvens2002_final.pdf)† |  |  |  |  |  |
| PCCGA | [Gesticulation behaviors for virtual humans](https://doi.org/10.1109/pccga.1998.732100)† · [open copy](https://repository.upenn.edu/hms/21) |  |  | rule-based |  |  |

### 2001

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| ACL | [Non-verbal cues for discourse structure](https://doi.org/10.3115/1073012.1073028)† · [open copy](https://dl.acm.org/doi/pdf/10.3115/1073012.1073028) |  |  |  |  |  |
| eScholarship | [Timing and Rhythm in Multimodal Communication for Conversational Agents](https://escholarship.org/uc/item/91h8h0vn)† | text | upper-body, hands | rule-based |  |  |
| JASA | [Gesture-speech interaction in the SmartKom project](https://doi.org/10.1121/1.4777335)† | text |  | rule-based |  |  |
| Life-like characters | [BEAT](https://doi.org/10.1145/383259.383315)† | text |  | rule-based |  |  |
| Workshop | [From Human Gesture to Synthetic Action](http://michaelkipp.de/publication/Kipp2001.pdf)† |  |  |  |  |  |

### 2000

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| CA | [Planning and motion control in lifelike gesture: a refined approach](https://doi.org/10.1109/ca.2000.889051)† |  |  | rule-based |  |  |
| CGA | [Design of a virtual human presenter](https://doi.org/10.1109/38.851755)† · [open copy](https://kyutech.repo.nii.ac.jp/records/741) | text |  |  |  |  |
| CGI | [To gesture or not to gesture: what is the question?](https://doi.org/10.1109/cgi.2000.852314)† · [open copy](https://repository.upenn.edu/hms/5) |  |  |  |  |  |
| ECAI | [A knowledge-based approach for lifelike gesture animation](https://pub.uni-bielefeld.de/record/2611273)† |  |  | rule-based |  |  |
| INLG | [Coordination and context-dependence in the generation of embodied conversation](https://doi.org/10.3115/1118253.1118277)† · [open copy](https://dl.acm.org/doi/pdf/10.3115/1118253.1118277) |  |  | rule-based |  |  |

### 1999

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| AAAI Fall Symposium | [Living Hand to Mouth: Psychological Theories about Speech and Gesture in Interactive Dialogue Systems](http://athos.rutgers.edu/~mdstone/pubs/aaaifs99.pdf)† |  |  |  |  |  |
| Applied Artificial Intelligence | [Deictic believability: Coordinated gesture, locomotion, and speech in lifelike pedagogical agents](https://doi.org/10.1080/088395199117324)† |  |  |  |  |  |
| CHI | [Embodiment in conversational interfaces](https://doi.org/10.1145/302979.303150)† |  |  |  |  |  |
| Oxford University Press | [Embodied conversational agents: a new paradigm for the study of gesture and for human—computer interface](https://doi.org/10.1093/acprof:oso/9780198524519.003.0011)‡ |  |  |  |  |  |

### 1998

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| AAAI Workshop | [Task-Oriented Dialogs with Animated Agents in Virtual Reality](https://www.aaai.org/Papers/Workshops/1998/WS-98-09/WS98-09-014.pdf)† |  |  |  |  |  |
| Computer Vision for Human-Machine Interaction | [A Framework for Gesture Generation and Interpretation](https://doi.org/10.1017/cbo9780511569937.013)† |  | hands, face | rule-based |  |  |
| MIT Media Lab | [Embodied Conversation: Integrating Face and Gesture into Automatic Spoken Dialogue Systems](https://www.media.mit.edu/gnl/discint99/papers/cassell_toappear.pdf)† |  | hands, face |  |  |  |

### 1997

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| AVSP | [Animation of Talking Agents](https://www.diva-portal.org/smash/record.jsf?pid=diva2:318253)† |  |  |  |  |  |
| CA | [Layered modular action control for communicative humanoids](https://doi.org/10.1109/ca.1997.601055)† |  |  |  |  |  |
| VSMM | [Animated interactive fiction: Storytelling by a conversational virtual actor](https://doi.org/10.1109/vsmm.1997.622336)† | text |  |  |  |  |

### 1996

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| NEC Research & Development | [A human-like computer character user interface by creating communicational gestures](http://pascal-francis.inist.fr/vibad/index.php?action=getRecordDetail&idt=3179122)† |  |  |  |  |  |

### 1995

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| Advances in Human Factors/Ergonomics | [A human-computer dialogue agent with body gestures, hand motion, and speech](https://doi.org/10.1016/s0921-2647(06)80005-5)‡ |  |  |  |  |  |

### 1994

| Venue | Paper | Input | Output | Approach | Setting | Code |
|---|---|---|---|---|---|---|
| SIGGRAPH | [Animated conversation](https://doi.org/10.1145/192161.192272)† |  |  |  |  |  |
<!-- END:papers -->

## Surveys, challenges and evaluation studies

<!-- BEGIN:surveys -->
| Year | Venue | Kind | Paper | Summary |
|---|---|---|---|---|
| 2026 | ACM | evaluation | [A Preliminary Analysis of Situation and Personality in LLM-Generated Gesture Representations for Virtual Agents](https://doi.org/10.1145/3806774.3832786)† |  |
| 2026 | CVIDL | survey | [A Review of Data-Driven Co-Speech Gesture Generation: Methods, Datasets, and Challenges](https://doi.org/10.1109/cvidl70130.2026.11637684)† | Reviews data-driven co-speech gesture generation methods from statistical and recurrent models to diffusion frameworks, compares benchmark datasets, and discusses open challenges. |
| 2026 | CVPR | evaluation | [Towards Reliable Human Evaluations in Gesture Generation: Insights from a Community-Driven State-of-the-Art Benchmark](https://arxiv.org/abs/2511.01233) · [project](https://genea-workshop.github.io/leaderboard/) | Reviews human evaluation practice in speech-driven 3D gesture generation and proposes a standardised protocol on BEAT2, used in a crowdsourced ranking of six models. |
| 2026 | DOAJ | survey | [Recent Advances in Speech-Driven Gesture Generation](https://doaj.org/article/a0866c81e0cb4f1ab41fa53819f364b4)† | Survey of speech-driven gesture generation covering GAN, VAE and diffusion methods, controllability, face-and-gesture co-generation, datasets and metrics. |
| 2026 | SIGGRAPH | evaluation | [Reality Check: How Avatar and Face Representation Affect the Perceptual Evaluation of Synthesized Gestures](https://doi.org/10.1145/3799902.3811161) · [open copy](https://arxiv.org/abs/2605.06063) | Runs controlled perceptual studies comparing mocap and generated co-speech gestures across seven avatar renderings and face presentations to measure their effect on motion judgments. |
| 2025 | ACM | evaluation | [Evaluating Automatic Hand-Gesture Generation Using Multimodal Corpus Annotations: The Benefits of a Multidisciplinary Approach](https://doi.org/10.1145/3746268.3759430)† · [open copy](https://hal.science/hal-05330689) | Compares expert annotations of natural and synthetic hand gestures on a small dataset to derive indicators of communicative efficiency and movement dynamics for evaluating gesture synthesis. |
| 2025 | CSTE | survey | [A Review of Digital Human Gesture Generation Technology and Its Teaching Application Thinking](https://doi.org/10.1109/cste64638.2025.11091914)† | Reviews co-speech gesture generation methods and datasets and discusses applications of the technology in education. |
| 2025 | Frontiers in Computer Science | evaluation | [Evaluation of Generative Models for Emotional 3D Animation Generation in VR](https://doi.org/10.3389/fcomp.2025.1598099) · [open copy](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1598099/pdf) · [project](https://emotional3dhumans.github.io) | Compares three speech-driven 3D animation methods (EMAGE, TalkSHOW, AMUSE with FaceFormer) and a video-reconstruction baseline in a VR human-agent scenario with a 48-participant study of emotion and animation quality. |
| 2025 | GENEA Workshop | evaluation | [From Embeddings to Language Models: A Comparative Analysis of Feature Extractors for Text-Only and Multimodal Gesture Generation](https://doi.org/10.1145/3746268.3759431)† | Compares seven diffusion-based gesture generation pipelines that use different audio (WavLM, Whisper) and text (Word2Vec, Llama-3.2-3B-Instruct) feature extractors. |
| 2025 | ICMI | evaluation | [Multimodal Quantitative Measures for Multiparty Behavior Evaluation](https://doi.org/10.1145/3716553.3750752) · [open copy](https://arxiv.org/abs/2508.10916) | Proposes objective measures for multiparty skeletal behaviour (cross-recurrence synchrony, multiscale beat consistency, soft-DTW similarity) and tests their sensitivity with perturbations of group interaction data. |
| 2025 | IJHCI | evaluation | [Advancing Objective Evaluation of Speech-Driven Gesture Generation for Embodied Conversational Agents](https://doi.org/10.1080/10447318.2025.2531286)† | Proposes neural feature extractors for similarity-based objective evaluation and compares 56 combinations of extractors and distance measures by their correlation with GENEA 2022 and 2023 subjective results. |
| 2025 | IVA | evaluation | [Synthetically Expressive: Evaluating gesture and voice for emotion and empathy in VR and 2D scenarios](https://doi.org/10.1145/3717511.3747074) · [open copy](https://arxiv.org/abs/2506.23777) · [video](https://youtu.be/WMfjIB1X-dc) | A user study with 219 participants compares real and synthetic (AMUSE) gestures and voices in VR and 2D displays across emotional contexts. |
| 2025 | VCIP | evaluation | [Ges-QA: A Multidimensional Quality Assessment Dataset for Audio-to-3D Gesture Generation](https://doi.org/10.1109/vcip67698.2025.11396818) · [open copy](https://arxiv.org/abs/2508.12020) | Builds a dataset of 1,400 generated 3D gesture samples with human ratings of gesture quality and audio-gesture consistency and trains a three-branch (video, audio, skeleton) network to predict them. |
| 2024 | Applied Sciences | evaluation | [Exploring the Effectiveness of Evaluation Practices for Computer-Generated Nonverbal Behaviour](https://doi.org/10.3390/app14041460)† · [open copy](https://www.mdpi.com/2076-3417/14/4/1460/pdf?version=1707630406) | Compares two direct rating methods and a new questionnaire for evaluating generated gesturing and listening motion in six user studies, using output of two generative models and recorded human motion. |
| 2024 | Communications in Computer and Information Science | evaluation | [Comparative Analysis on Speech Driven Gesture Generation](https://doi.org/10.1007/978-3-031-68617-7_12)‡ |  |
| 2024 | GENEA Workshop | evaluation | [Gesture Area Coverage to Assess Gesture Expressiveness and Human-Likeness](https://doi.org/10.1145/3686215.3688822)† | Proposes metrics based on the spatial area covered by gestures in a motion sequence and compares them with human-likeness ratings from the GENEA Challenge 2023. |
| 2024 | ICMI | evaluation | [Benchmarking Speech-Driven Gesture Generation Models for Generalization to Unseen Voices and Noisy Environments](https://doi.org/10.1145/3686215.3688823)† | Evaluates speech-driven gesture models on unseen voices produced by voice conversion and on synthetic noisy audio, applied to DiffuseStyleGesture+. |
| 2024 | ICMI | challenge | [GENEA Workshop 2024: The 5th Workshop on Generation and Evaluation of Non-verbal Behaviour for Embodied Agents](https://doi.org/10.1145/3678957.3688818)† | Workshop overview on generation and evaluation of non-verbal behaviour for embodied agents, aiming to unite the community around standardized benchmarking. |
| 2024 | ICMI | evaluation | [Gesture Evaluation in Virtual Reality](https://doi.org/10.1145/3686215.3688821) · [open copy](https://arxiv.org/abs/2509.12816) | Compares ratings of gestures from three GENEA 2023 Challenge systems viewed in virtual reality against standard 2D video in a user study. |
| 2024 | IVA | evaluation | [2D or not 2D: How Does the Dimensionality of Gesture Representation Affect 3D Co-Speech Gesture Generation?](https://doi.org/10.1145/3652988.3673934) · [open copy](https://arxiv.org/abs/2409.10357) · [project](https://sites.google.com/view/iva-2d-or-not-2d) | Compares training speech-to-gesture models (DiffGesture and Trimodal) on 2D versus 3D joint coordinates, lifting 2D outputs to 3D for evaluation. |
| 2024 | TOG | challenge | [Evaluating Gesture Generation in a Large-scale Open Challenge: The GENEA Challenge 2022](https://doi.org/10.1145/3656374) · [open copy](https://arxiv.org/abs/2303.08737) · [project](https://youngwoo-yoon.github.io/GENEAchallenge2022/) | Reports the GENEA Challenge 2022, in which teams built gesture generators on shared data and were compared in large crowdsourced human-likeness and appropriateness studies. |
| 2024 | WACAI | evaluation | [Investigating the impact of 2D gesture representation on co-speech gesture generation](https://arxiv.org/abs/2406.15111) | Compares training a diffusion-based speech-to-gesture model on 2D joint coordinates and lifting the output to 3D against training directly on 3D coordinates. |
| 2023 | CGF | survey | [A Comprehensive Review of Data-Driven Co-Speech Gesture Generation](https://doi.org/10.1111/cgf.14776) · [open copy](https://arxiv.org/abs/2301.05339) | Review of co-speech gesture generation research with a focus on deep generative models, organized by input modality, together with training datasets and open challenges. |
| 2023 | GENEA Workshop | evaluation | [A Methodology for Evaluating Multimodal Referring Expression Generation for Embodied Virtual Agents](https://doi.org/10.1145/3610661.3616548)† | Proposes a methodology and embodied platform for evaluating how well a virtual agent generates multimodal referring expressions with language, gesture and facial expressions, compared against human references. |
| 2023 | ICMI | challenge | [GENEA Workshop 2023: The 4th Workshop on Generation and Evaluation of Non-verbal Behaviour for Embodied Agents](https://doi.org/10.1145/3577190.3616856)† · [open copy](https://dl.acm.org/doi/pdf/10.1145/3577190.3616856) | Workshop proposal for bringing the community together on generating and evaluating non-verbal behaviour for embodied agents and on benchmarking practice. |
| 2023 | ICMI | challenge | [The GENEA Challenge 2023: A large-scale evaluation of gesture generation models in monadic and dyadic settings](https://doi.org/10.1145/3577190.3616120) · [open copy](https://dl.acm.org/doi/pdf/10.1145/3577190.3616120) · [project](https://svito-zar.github.io/GENEAchallenge2023/) | Reports the GENEA Challenge 2023, in which teams generated full-body motion from an agent's speech and its interlocutor's speech and motion, evaluated in large user studies. |
| 2023 | ICMI | evaluation | [“Am I listening?”, Evaluating the Quality of Generated Data-driven Listening Motion](https://doi.org/10.1145/3610661.3617160) · [open copy](https://dl.acm.org/doi/pdf/10.1145/3610661.3617160) | Tests in several user studies whether two gesture-generation models from recent challenges, one using both sides of the conversation and one only the character's own speech, produce motion perceived as listening. |
| 2023 | THRI | survey | [Data-driven Communicative Behaviour Generation: A Survey](https://doi.org/10.1145/3609235)† · [open copy](https://dl.acm.org/doi/pdf/10.1145/3609235) | Survey of deep-learning-based co-speech behaviour generation models for human-agent and human-robot interaction, with an outlook on future research. |
| 2022 | ICMI | challenge | [The GENEA Challenge 2022: A large evaluation of data-driven co-speech gesture generation](https://doi.org/10.1145/3536221.3558058) · [open copy](https://arxiv.org/abs/2208.10441) · [project](https://youngwoo-yoon.github.io/GENEAchallenge2022/) | Reports the second GENEA Challenge, in which ten teams built gesture generators on a shared 18-hour dyadic mocap dataset, compared in crowdsourced human-likeness and appropriateness studies. |
| 2022 | IEEE VR | evaluation | [Investigating how speech and animation realism influence the perceived personality of virtual characters and agents](https://doi.org/10.1109/vr51125.2022.00018)† · [open copy](https://arrow.tudublin.ie/creaart/155) | A perceptual study comparing performance-captured characters with characters driven by generated gestures and synthesized speech on perceived Big Five personality. |
| 2022 | IJCGT | evaluation | [Automatic Quality Assessment of Speech-Driven Synthesized Gestures](https://doi.org/10.1155/2022/1828293)† · [open copy](https://downloads.hindawi.com/journals/ijcgt/2022/1828293.pdf) | A Bi-LSTM model with an adjusted attention mechanism gives an automatic quantitative quality assessment of synthesized gesture video. |
| 2022 | IVA | evaluation | [Evaluating data-driven co-speech gestures of embodied conversational agents through real-time interaction](https://doi.org/10.1145/3514197.3549697) · [open copy](https://arxiv.org/abs/2210.06974) · [video](http://www.yaeh.io/research/hci/presentingbot) | Evaluates a Gesticulator-driven agent against a non-gesturing agent in a live within-subjects interaction study using questionnaires and gaze tracking. |
| 2022 | Speech Communication | evaluation | [Arm motion symmetry in conversation](https://doi.org/10.1016/j.specom.2022.08.001)† · [open copy](https://ueaeprints.uea.ac.uk/id/eprint/87977/1/1_s2.0_S0167639322001054_main.pdf) | Analyses left-right arm symmetry of 36 speakers in dyadic conversation and tests with a speech-to-gesture model whether mirroring is valid as data augmentation. |
| 2022 | THMS | survey | [A Review of Evaluation Practices of Gesture Generation in Embodied Conversational Agents](https://doi.org/10.1109/thms.2022.3149173) · [open copy](https://arxiv.org/abs/2101.03769) | A systematic review of 22 studies of co-speech gesture generation for embodied conversational agents that examines how they were evaluated and proposes evaluation recommendations and a reporting checklist. |
| 2022 | THRI | survey | [The Design and Observed Effects of Robot-performed Manual Gestures: A Systematic Review](https://doi.org/10.1145/3549530)† · [open copy](https://dl.acm.org/doi/pdf/10.1145/3549530) | Systematic review of social robots that use manual gestures, covering the gesture production process (design and planning) and the effects of robot-performed gestures on human-robot interaction. |
| 2021 | Autonomous Robots | evaluation | [Quantitative analysis of robot gesticulation behavior](https://doi.org/10.1007/s10514-020-09958-1) · [open copy](https://arxiv.org/abs/2010.11614) | Compares two GAN-based gesture generators for a Pepper robot using principal coordinate analysis, procrustes statistics and a Fréchet Gesture Distance adapted from FID. |
| 2021 | HAI | survey | [Speech-based Gesture Generation for Robots and Embodied Agents: A Scoping Review](https://doi.org/10.1145/3472307.3484167)† | Scoping review of methods, datasets and objective and subjective evaluation measures for co-speech gesture generation for embodied agents and robots, collected by a Scopus term search. |
| 2021 | Handbook on Socially Interactive Agents | survey | [Gesture Generation](https://doi.org/10.1145/3477322.3477330)‡ |  |
| 2021 | ICMI | challenge | [GENEA Workshop 2021: The 2nd Workshop on Generation and Evaluation of Non-verbal Behaviour for Embodied Agents](https://dl.acm.org/doi/10.1145/3462244.3480983)† · [project](https://genea-workshop.github.io/2021/) | Workshop overview that brings the community together to discuss benchmarking and evaluation of non-verbal behaviour generation for embodied agents. |
| 2021 | ICMI | evaluation | [HEMVIP: Human Evaluation of Multiple Videos in Parallel](https://doi.org/10.1145/3462244.3479957) · [open copy](https://arxiv.org/abs/2101.11898) | A framework for granular parallel rating of multiple video stimuli, validated against prior pairwise-comparison results on gesture generation videos. |
| 2021 | ICMI | evaluation | [To Rate or Not To Rate: Investigating Evaluation Methods for Generated Co-Speech Gestures](https://doi.org/10.1145/3462244.3479889) · [open copy](https://arxiv.org/abs/2108.05709) · [project](http://svito-zar.github.io/gesticulator/) | Compares rating-based and pairwise-comparison crowdsourced evaluation of co-speech gestures generated by three models, in terms of ranking quality, reliability and effort. |
| 2021 | ICRA | evaluation | [Which gesture generator performs better?](https://doi.org/10.1109/icra48506.2021.9561075)† | Compares two generative gesture methods with quantitative measures and shows the results correlate with subjective ratings from a sizable group of people. |
| 2021 | IJHCI | survey | [Examining the Use of Nonverbal Communication in Virtual Agents](https://doi.org/10.1080/10447318.2021.1898851)† | Survey of the uses, outcomes and development of nonverbal communication in virtual agents. |
| 2021 | IUI | challenge | [A Large, Crowdsourced Evaluation of Gesture Generation Systems on Common Data: The GENEA Challenge 2020](https://doi.org/10.1145/3397481.3450692) · [open copy](https://arxiv.org/abs/2102.11617) · [project](https://svito-zar.github.io/GENEAchallenge2020/) | A gesture-generation challenge in which teams built systems on a common speech-gesture dataset and all systems were compared in two parallel crowdsourced user studies using one rendering pipeline. |
| 2021 | IVA | evaluation | [Human or Robot?](https://doi.org/10.1145/3472306.3478338)† · [open copy](https://dl.acm.org/doi/pdf/10.1145/3472306.3478338) | Two perceptual studies assess how realism of synthetic voice, gesture motion and visual appearance affects perceived speech-gesture match, likability and human-likeness of virtual agents. |
| 2021 | RO-MAN | evaluation | [Factor exploration of gestural stroke choice in the context of ambiguous instruction utterances: challenges to synthesizing semantic gesture from speech alone](https://doi.org/10.1109/ro-man50785.2021.9515416)† | Analyses three challenge factors for speech-driven gesture synthesis: ambiguous utterances, choice of f-formation for spatial gestures, and readability of retargeted human motion under kinematic constraints. |
| 2021 | The Handbook on Socially Interactive Agents | survey | [Multimodal Behavior Modeling for Socially Interactive Agents](https://doi.org/10.1145/3477322.3477331)‡ · [open copy](https://hal.science/hal-03999516) |  |
| 2020 | IVA | evaluation | [Can we trust online crowdworkers?: Comparing online and offline participants in a preference test of virtual agents](https://doi.org/10.1145/3383652.3423860) · [open copy](https://arxiv.org/abs/2009.10760) | Replicates a human-likeness preference test of two speech-driven gesture generation models with in-lab, Prolific and Amazon Mechanical Turk participants and finds no difference between the pools. |
| 2019 | Ghent University Academic Bibliography | evaluation | [Should Beat Gestures Be Learned Or Designed? : A Benchmarking User Study](http://hdl.handle.net/1854/LU-8622805)† | User study comparing beat gestures from a speech-to-pose machine learning model with three hand-coded beat gesture methods on a humanoid agent, ranked by paired comparisons. |
| 2017 | Gesture Studies | survey | [Computational gesture research](https://doi.org/10.1075/gs.7.13kop)† | Book chapter reviewing approaches to synthesizing co-speech gestures for virtual characters and robots and experiments on the effects of such synthetic gesturing on human addressees. |
| 2017 | Social Signal Processing | survey | [Body Movements Generation for Virtual Characters and Social Robots](https://doi.org/10.1017/9781316676202.020)† | Book chapter reviewing body language generation (postures, gestures, proxemics) for virtual humans and social robots, including synchronisation with speech. |
| 2017 | TOG | evaluation | [Understanding the impact of animated gesture performance on personality perceptions](https://doi.org/10.1145/3072959.3073697)† | Perceptual studies of how edits to gesture motion properties change the perceived personality of an animated character, including with accompanying speech. |
| 2013 | IVA | evaluation | [The Influence of Prosody on the Requirements for Gesture-Text Alignment](https://doi.org/10.1007/978-3-642-40415-3_16)‡ |  |
| 2011 | Eurographics | survey | [Believable Virtual Characters in Human-Computer Dialogs](https://doi.org/10.2312/eg2011/stars/075-100)† | A state-of-the-art report on virtual characters in multimodal dialogs, going from communication models to animation and rendering of nonverbal behaviour such as facial expressions and gestures. |
| 2011 | Humanoids | evaluation | [The effects of robot-performed co-verbal gesture on listener behaviour](https://doi.org/10.1109/humanoids.2011.6100810)† | Two user studies test whether a humanoid robot performing co-verbal gestures holds listener attention longer and improves memory of accompanied facts. |
| 2011 | RO-MAN | evaluation | [A friendly gesture: Investigating the effect of multimodal robot behavior in human-robot interaction](https://doi.org/10.1109/roman.2011.6005285)† | Two experimental studies with the Honda humanoid robot on how speech-accompanying hand and arm gestures affect human evaluation of the interaction and the robot. |
| 2010 | AAAI | evaluation | [The Role of Embodiment and Perspective in Direction-Giving Systems](http://arakilab.media.eng.hokudai.ac.jp/~araki/2010/2010-A-13.pdf)† | Compares a robot, an embodied conversational agent and a GPS giving directions with speaker-perspective, listener-perspective or no gestures. |
| 2010 | IVA | evaluation | [Evaluating the Effect of Gesture and Language on Personality Perception in Conversational Agents](https://doi.org/10.1007/978-3-642-15892-6_24)‡ |  |
| 2010 | IVA | evaluation | [Individualized Gesturing Outperforms Average Gesturing – Evaluating Gesture Production in Virtual Humans](https://doi.org/10.1007/978-3-642-15892-6_11)‡ |  |
| 2007 | Interacting with Computers | evaluation | [The effects of speech–gesture cooperation in animated agents’ behavior in multimedia presentations](https://doi.org/10.1016/j.intcom.2007.04.002)† · [open copy](https://hal.science/hal-00786343v1/file/LCPI_IWC_2007_BUISINE.pdf) | Compares redundant, complementary and non-semantic speech-gesture cooperation strategies in animated agents in a user study measuring recall and subjective evaluation. |
| 2005 | AISB | evaluation | [Reference and Gestures in Dialogue Generation: Three Studies with Embodied Conversational Agents](https://oro.open.ac.uk/12137/1/aisb05.pdf)† | Reports evaluation studies of the gestures generated by the NECA system, covering their effect on perceived speech quality and information retention, alongside a referring-expression study. |
| 1999 | Applied Artificial Intelligence | evaluation | [The power of a nod and a glance: Envelope vs. emotional feedback in animated conversational agents](https://doi.org/10.1080/088395199117360)† | A user experiment comparing three autonomous conversational humanoid agents that give content-only, content plus envelope (gaze, beat gesture, head movement) or content plus emotional feedback. |
<!-- END:surveys -->

## Dataset papers

Papers whose main contribution is a dataset. The datasets themselves are compared in the next section.

<!-- BEGIN:dataset-papers -->
| Year | Venue | Kind | Paper | Summary |
|---|---|---|---|---|
| 2026 | Scientific Data | dataset | [Multi-TPC: A Multimodal Dataset for Three-Party Conversations with Speech, Motion, and Gaze](https://doi.org/10.1038/s41597-026-06819-x) | A motion-capture dataset of three-party conversations with synchronized speech, full-body motion and gaze, with statistical analysis of gesture correlations. |
| 2025 | ICCV 2025 Workshop MMFM4 | dataset | [Preview WB-DH: Towards Whole Body Digital Human Bench for the Generation of Whole-body Talking Avatar Videos](https://arxiv.org/abs/2508.08891) | An open benchmark of whole-body talking avatar videos with multi-modal annotations and a 12-metric evaluation framework covering video generation and co-speech quality. |
| 2025 | NeurIPS 2025 (Datasets and Benchmarks) | dataset | [TalkCuts: A Large-Scale Dataset for Multi-Shot Human Speech Video Generation](https://openreview.net/forum?id=4a0w7AkrY7) · [open copy](https://arxiv.org/abs/2510.07249) · [project](https://talkcuts.github.io/) | Dataset of 164k speech video clips (over 500 hours) with text descriptions, 2D keypoints and SMPL-X annotations, with an LLM-directed multi-shot video generation baseline (Orator). |
| 2025 | Scientific Data | dataset | [A richly annotated dataset of co-speech hand gestures across diverse speaker contexts](https://doi.org/10.1038/s41597-025-06020-6) · [open copy](https://www.nature.com/articles/s41597-025-06020-6.pdf) | A dataset of 2373 manually annotated co-speech hand gestures from nine English-speaking lecturers, politicians and psychotherapists, with gesture types, physical properties, lexemes and MediaPipe 3D pose tracking. |
| 2024 | IVA | dataset | [GeSTICS: A Multimodal Corpus for Studying Gesture Synthesis in Two-party Interactions with Contextualized Speech](https://doi.org/10.1145/3652988.3673917) · [open copy](https://pmc.ncbi.nlm.nih.gov/articles/PMC12747799/) · [project](https://gkebe.github.io/gestics/) | Corpus of 147 NBA post-game interviewees with transcripts, acoustic and lexical features, MediaPipe body, hand and face keypoints, and metadata on speaker and situational factors, covering both listening and answering phases. |
| 2024 | IVA | dataset | [Incorporating Spatial Awareness in Data-Driven Gesture Generation for Virtual Agents](https://doi.org/10.1145/3652988.3673936) · [open copy](https://arxiv.org/abs/2408.04127) · [project](https://huggingface.co/spaces/annadeichler/spatial-gesture) | Introduces a synthetic motion-capture gesture dataset of pointing and beat gestures to train speech-driven models that take scene information into account. |
| 2023 | Electronics | dataset | [DGU-HAU: A Dataset for 3D Human Action Analysis on Utterances](https://doi.org/10.3390/electronics12234793)† · [open copy](https://www.mdpi.com/2079-9292/12/23/4793/pdf?version=1701077506) | Introduces DGU-HAU, a multi-modal dataset of 3D human actions occurring during utterances, validated with the Action2Motion action generation model. |
| 2023 | HRI | dataset | [A Multimodal Dataset for Robot Learning to Imitate Social Human-Human Interaction](https://doi.org/10.1145/3568294.3580080) · [open copy](https://kclpure.kcl.ac.uk/ws/files/196446512/LISI_HHI_Dataset_LBR_Camera_Ready_.pdf) | Introduces LISI-HHI, 8.3 hours of dyadic conversations by 64 participants recorded with 120 fps Vicon motion capture (39 joints), RGB-D cameras, eye trackers and a microphone across five interaction scenarios. |
| 2022 | ECCV | dataset | [BEAT: A Large-Scale Semantic and Emotional Multi-Modal Dataset for Conversational Gestures Synthesis](https://doi.org/10.1007/978-3-031-20071-7_36) · [open copy](https://arxiv.org/abs/2203.05297) · [project](https://pantomatrix.github.io/BEAT/) | Releases a 76-hour motion capture dataset of 30 speakers with emotion and semantic annotations, plus a cascaded baseline (CaMN) and the SRGR metric. |
| 2022 | Journal of Digital Contents Society | dataset | [KLSG : Korean-based Large-scale Co-Speech Gesture Dataset](https://doi.org/10.9728/dcs.2022.23.11.2269)‡ |  |
| 2021 | Hokkai-Gakuen Univ. Eng. Res. Rep. | dataset | [Extending a Japanese Speech−to−Gesture Dataset Towards Building a Pedagogical Agent for Second Language Learning](https://hokuga.repo.nii.ac.jp/records/2003686)† | Extends a Japanese speech and motion-capture gesture dataset with seven gesture-phase annotations on 240 sentences and tests Bi-directional LSTM gesture phase estimation to extend the annotations. |
| 2021 | SPIE | dataset | [Automatic dataset collection for speech-driven gesture generation](https://doi.org/10.1117/12.2591375)† | Automatic method that extracts paired utterance and gesture data from online speech videos to build a co-speech gesture dataset, checked by training a speech-driven gesture network on it. |
| 2019 | CVPR | dataset | [Towards Social Artificial Intelligence: Nonverbal Social Signal Prediction in a Triadic Interaction](https://doi.org/10.1109/cvpr.2019.01113) · [open copy](https://arxiv.org/abs/1906.04158) · [project](http://domedb.perception.cs.cmu.edu/ssp) | Introduces the social signal prediction task and a triadic haggling motion capture dataset, with convolutional baselines that predict a person's body gestures, speaking status and social formation from the other participants' signals. |
| 2019 | ICCV | dataset | [Talking With Hands 16.2M: A Large-Scale Dataset of Synchronized Body-Finger Motion and Audio for Conversational Motion Analysis and Synthesis](https://personalrobotics.cs.washington.edu/publications/lee2019handmotiondataset.pdf)‡ |  |
| 2019 | Lecture Notes in Electrical Engineering | dataset | [Development of a Repository of Virtual 3D Conversational Gestures and Expressions](https://doi.org/10.1007/978-3-030-21507-1_16)‡ |  |
| 2018 | LREC | dataset | [A Corpus of Natural Multimodal Spatial Scene Descriptions](http://www.lrec-conf.org/proceedings/lrec2018/pdf/296.pdf)† | A corpus of speech and hand-motion data from participants giving spatial scene descriptions with abstract deictic and iconic gestures, intended for modelling multimodal descriptions and generating them. |
| 2017 | CCIS | dataset | [Creating a Gesture-Speech Dataset for Speech-Based Automatic Gesture Generation](https://doi.org/10.1007/978-3-319-58750-9_28)‡ |  |
| 2017 | International Journal of Computers | dataset | [A Corpus for Analyzing Linguistic and Paralinguistic Features in Multi-Speaker Spontaneous Conversations – EVA Corpus](https://www.iaras.org/iaras/home/cijc/a-corpus-for-analyzing-linguistic-and-paralinguistic-features-in-multi-speaker-spontaneous-conversations-eva-corpus)† | An annotated corpus of multi-speaker spontaneous conversations with linguistic, prosodic and co-verbal behavior annotation (hand gestures, head, gaze, emotion) for synthesizing co-verbal behavior in conversational agents. |
| 2017 | WSEAS Transactions on Information Science and Applications | dataset | [A Corpus for Investigating the Multimodal Nature of Multi-Speaker Spontaneous Conversations – EVA Corpus](https://www.wseas.org/multimedia/journals/information/2017/a465909-076.pdf)† | An annotated corpus of spontaneous multi-speaker conversations linking linguistic and prosodic features to co-verbal behavior such as hand gestures, head movement and gaze, to support co-verbal behavior synthesis for agents. |
| 2016 | LREC | dataset | [A Corpus of Gesture-Annotated Dialogues for Monologue-to-Dialogue Generation from Personal Narratives](https://www.aclweb.org/anthology/L16-1550.pdf)† | Presents the Story Dialogue with Gestures corpus of 50 personal narratives regenerated as dialogues with annotated gesture placement and gesture forms, plus gesture video clips and story intention graph annotations. |
| 2016 | LREC | dataset | [A Multimodal Motion-Captured Corpus of Matched and Mismatched Extravert-Introvert Conversational Pairs](https://doi.org/10.63317/3b6bvobctc5u)† | Personality Dyads Corpus of three conversations in each of three extravert and introvert pairs, with optical body mocap, data-glove hands, transcripts and ANVIL gesture annotations released as BVH. |
| 2015 | ACM | dataset | [The University of Edinburgh Speaker Personality and MoCap Dataset](https://doi.org/10.1145/2813852.2813860)† | A dialogue dataset with head and body motion capture of introverted and extroverted speaker personality styles, intended for synthesizing personality-based nonverbal behaviour from speech. |
| 2015 | FG | dataset | [MSP-AVATAR corpus: Motion capture recordings to study the role of discourse functions in the design of intelligent virtual agents](https://doi.org/10.1109/fg.2015.7284885)† | A multimedia corpus of motion capture (upper-body skeleton and face), video and audio from four actors in dyadic improvised interactions, designed around discourse functions. |
| 2012 | JMUI | dataset | [Data-based analysis of speech and gesture: the Bielefeld Speech and Gesture Alignment corpus (SaGA) and its applications](https://doi.org/10.1007/s12193-012-0106-8)‡ · [open copy](https://pub.uni-bielefeld.de/record/2522299) |  |
| 2012 | LNCS | dataset | [Collection and Analysis of Multimodal Interaction in Direction-Giving Dialogues: Towards an Automatic Gesture Selection Mechanism for Metaverse Avatars](https://doi.org/10.1007/978-3-642-32326-3_6)‡ |  |
| 2012 | LNCS | dataset | [Form-Oriented Annotation for Building a Functionally Independent Dictionary of Synthetic Movement](https://doi.org/10.1007/978-3-642-34584-5_21)† · [open copy](https://dk.um.si/IzpisGradiva.php?id=50219) | Presents a form-oriented annotation scheme for multi-speaker dialogue corpora that turns annotated movement into templates an embodied conversational agent can reproduce. |
| 2010 | LREC Workshop on Multimodal Corpora | dataset | [The Bielefeld Speech and Gesture Alignment Corpus (SaGA)](https://doi.org/10.13140/2.1.4216.1922)‡ · [open copy](https://pub.uni-bielefeld.de/record/2001935) |  |
<!-- END:dataset-papers -->

## Theses

Doctoral and master's theses on gesture generation and on gesture theory. They are examined rather than peer reviewed, so they are listed apart from the papers.

<!-- BEGIN:theses -->
| Year | Thesis | Institution | Kind | Summary |
|---|---|---|---|---|
| 2026 | [AI-Based Gesture Generation for Humanoid Robots from Speech Transcriptions](https://etd.adm.unipi.it/theses/available/etd-05072026-144420/)† | University of Pisa | method | Generates co-speech gestures for a humanoid robot from text transcriptions using a discrete gesture vocabulary built with VQ-VAE and GRU or Transformer models with a latent-space Kalman filter. |
| 2026 | [More Than Just Natural. Contextually Relevant and Semantically Meaningful Gesture Generation](https://doi.org/10.4119/unibi/3016358)† · [open copy](https://nbn-resolving.org/urn:nbn:de:0070-pub-30163585) | Bielefeld University | method | A thesis proposing context-driven gesture generation, covering AQ-GT and AQ-GT-A for beat and annotation-guided gestures, the TF-JAX-IK inverse kinematics solver, and the ImaGGen semantic planning framework driven by visual input. |
| 2026 | [Reinforcement Learning and Virtual Human Animation: A novel approach to data-driven animation, portraying dynamic, flexible human-like behaviours](https://doi.org/10.21427/aw1h-3j07)† · [open copy](https://arrow.tudublin.ie/scschcomdis/286) | TU Dublin | method | Model-based reinforcement learning framework (RLAnimate) with latent state space models that generates frame-by-frame upper-body behaviours including speech-driven beat gestures. |
| 2026 | [Spatially Grounded Communication in Embodied Agents : From Gesture Generation to Referential Understanding](http://urn.kb.se/resolve?urn=urn:nbn:se:kth:diva-382200)† | KTH | method | Thesis on semantic and spatial co-speech gesture generation using contrastive speech-motion pretraining, reinforcement learning with adversarial motion priors for pointing, and flow matching, plus referential grounding datasets. |
| 2026 | [Synthesizing Speech and Gesture for Embodied Conversational Agents](http://urn.kb.se/resolve?urn=urn:nbn:se:kth:diva-388651)† | KTH | method | Thesis on spontaneous text-to-speech, joint generation of speech and co-speech gesture in one Tacotron2-based model (ISG), and a layered evaluation protocol for conversational synthesis. |
| 2026 | [Towards Coherent Co-speech Gesture Generation: Multimodal Approaches for Emotional, Generalized, and Interactive Modeling](https://doi.org/10.14711/thesis-hdl172486)† | HKUST | method | Thesis on 3D co-speech gesture generation covering emotional transitions, in-the-wild speech (CoCoGesture, GES-X) and two-person conversation (Co3Gesture, GES-Inter). |
| 2026 | [Vers une approche interdisciplinaire fondée sur les données pour l’analyse multimodale et la modélisation computationnelle du geste co-verbal](https://hal.science/tel-05630737v1)† | HAL | evaluation | Thesis re-annotating part of the BEAT corpus (reBeat-14), analysing STARGATE-generated gestures with movement criteria, and proposing automatic gesture annotation and a CNN-GRU segmentation model (COSMOS). |
| 2025 | [Co-speech gesture synthesis : Towards a controllable and interpretable model using a graph deterministic approach](https://doi.org/10.70675/4b4d1808z33d7z4b7bz830bz71052e2093c2)† | PhD thesis | method | STARGATE generates gestures autoregressively using CNN encoders for audio and text, an ST-GCN encoding the gesture history and a biRNN decoder, with a speaker embedding for style personalisation. |
| 2025 | [EchoActor: Audio-Driven Upper Body Speech Video Generation](https://doi.org/10.82419/173)† | MBZUAI iRep | method | Generates upper-body speech videos from a reference image and audio, using a partial key-point sequence from an audio-to-gesture model to control motion and the audio to control facial expression, with an ID-Fusion reference network for the face. |
| 2025 | [Understanding and Generating Multi-Modalities: Advancing Efficient, Generalized, and Interactive Human-Centered AI](https://doi.org/10.14711/thesis-hdl167741)† | HKUST | method | Doctoral thesis whose generation part presents a diffusion-based model producing synchronized, arbitrary-length holistic 3D facial expressions and body gestures from speech. |
| 2024 | [Parallel-marking particles and co-speech gestures in Japanese](http://www.nusl.cz/ntk/nusl-622777)† | Digital Repository (National Repository of Grey Literature) | theory |  |
| 2024 | [Speech-driven expressive gesture generation for virtual agents](https://doi.org/10.47749/t/unicamp.2024.1499174)‡ | UNICAMP | method |  |
| 2024 | [The effects of learning sign language on co-speech gesture](http://www.nusl.cz/ntk/nusl-622671)† | Digital Repository (National Repository of Grey Literature) | theory |  |
| 2023 | [Multimodal Expressive Gesturing With Style](https://doi.org/10.70675/a1375d8dzd155z4b3ezb79azc121e1ceecad)† | Thesis | method | Thesis proposing zero-shot style-controlled upper-body and facial gesture synthesis from a speaker's speech content (ZS-MSTM) for embodied conversational agents. |
| 2022 | [Une analyse temporelle et pragmatique de l'association geste-parole : une approche basée sur un corpus utilisant le nouveau système d'annotation MultiModal MultiDimensionnel (M3D)](https://theses.hal.science/tel-03994053)† | HAL (Le Centre pour la Communication Scientifique Directe) | theory |  |
| 2021 | [An ERP Study of the Effects of Iconic and Nonsense Gestures on Memory Formation](https://doi.org/10.31390/gradschool_theses.5439)† | Unknown venue | theory |  |
| 2021 | [Gesture Resolution and Definiteness](https://doi.org/10.5281/zenodo.5812035)† | Zenodo (CERN European Organization for Nuclear Research) | theory |  |
| 2021 | [Génération du Comportement du Robot et Compréhension du Comportement Humain dans L'interaction Naturelle Humain-Robot](https://hal.science/tel-03313805v1)† · [open copy](http://www.theses.fr/2021IPPAE009/document) | theses.fr | method | Thesis that includes a temporal GAN mapping acoustic speech to humanoid robot gestures, trained on an audio-visual database with 3D poses extracted from RGB video, plus speech-driven face action synthesis. |
| 2021 | [Machine Learning For Plausible Gesture Generation From Speech For Virtual Humans](https://doi.org/10.2312/diss.20212633145)† · [open copy](http://hdl.handle.net/2262/96795) | Trinity College Dublin | method | Thesis exploring transfer learning, adversarial training and expressive gesture parameters for speech-to-gesture learning, presenting two speech and motion datasets and a system combining machine learning with database sampling. |
| 2021 | [Prediction of Gesture Timing and Study About Image Schema for Metaphoric Gestures](https://hal.science/tel-03589420v1)† | HAL | method | Dissertation on gesture generation for embodied conversational agents covering an attention-based RNN that predicts gesture timing, improved image-schema-based metaphoric gesture selection and vector representations of image schemas. |
| 2021 | [Structural Transformation, Culture, and Women's Labor Force Participation in Turkey](https://doi.org/10.7275/7430513.0)† | Scholarworks (University of Massachusetts Amherst) | theory |  |
| 2020 | [Language in the body: Multimodality in grammar and discourse](https://doi.org/10.7939/r3-1nhm-5c89)† | ERA: Education and Research Archive (University of Alberta) | theory |  |
| 2020 | [Modeling Visual Minutiae: Gestures, Styles, and Temporal Patterns](https://escholarship.org/uc/item/3ws1647q)† | eScholarship | method | Doctoral dissertation whose first part models conversational gestures from multi-modal correlations between audio and motion learned from video without human annotations. |
| 2020 | [Pragmatic analysis of hand gestures: a case study of co-speech gestures in two different genres of videos](https://repozitorij.ffzg.unizg.hr/islandora/object/ffzg:3412)† | ODRAZ (University of Zagreb Faculty of Humanities and SocialSciences) | theory |  |
| 2020 | [Temporal integration of gesture and speech in narrative discourse: an insight into the development of co-speech gesture use](https://repositori.upf.edu/handle/10230/46884)‡ | Unknown venue | theory |  |
| 2019 | [An Experimental Pragmatic Investigation of Depictive Co-Speech Gestures](http://nrs.harvard.edu/urn-3:HUL.InstRepos:42013043)† | Digital Access to Scholarship at Harvard (DASH) (Harvard University) | theory |  |
| 2019 | [Generating Socio‐emotional Behaviors](https://doi.org/10.1002/9781119649403.ch5)† | Wiley book chapter | method | Chapter on generating prosody and co-verbal gestures for an embodied conversational agent from verbal and prosodic content, building on corpus analysis. |
| 2019 | [Time gestures](https://doi.org/10.17635/lancaster/thesis/567)† | Lancaster EPrints (Lancaster University) | theory |  |
| 2018 | [Co-speech gesture integration in hippocampal amnesia](https://doi.org/10.17077/etd.89r2mell)† | Unknown venue | theory |  |
| 2018 | [Generating Audio-driven Emotional Gestures using Motion Graphs](https://dspace.library.uu.nl:8080/handle/1874/363578)† | Utrecht University | method | Builds a motion graph from segmented mocap and selects segments online using prosody features of live speech and a specified conversational attitude. |
| 2018 | [How gesture and speech interact during production and comprehension](http://etheses.bham.ac.uk/8084/1/Fritz18PhD.pdf)† | University of Birmingham Institutional Research Archive (University of Birmingham) | theory |  |
| 2018 | [Preschoolers' pragmatic development: how prosody and gesture lend a helping hand](http://hdl.handle.net/10803/593503)† | LA Referencia (Red Federada de Repositorios Institucionales de Publicaciones Científicas) | theory |  |
| 2017 | [An exploration of the integration of speech with co-speech gesture with non-invasive brain stimulation](https://hull-repository.worktribe.com/file/4220574/1/Thesis)† | Repository@Hull (Worktribe) (University of Hull) | theory |  |
| 2017 | [Cognition in action C-i-A: Rethinking gesture in neuro-atypical young people: A conceptual framework for embodied, embedded, extended and enacted intentionality](https://openaccess.city.ac.uk/id/eprint/15292/1/Panayi%2C%20Marilyn.pdf)† | City Research Online (City University London) | theory |  |
| 2017 | [O sistema de referenciação multimodal de crianças com síndrome de down em engajamento conjunto](https://repositorio.ufpb.br/jspui/handle/123456789/12051)† | Americanae (AECID Library) | theory |  |
| 2017 | [The use of gestures in the conversations of people with aphasia](https://openaccess.city.ac.uk/id/eprint/18031/1/Kistner%2C%20Judith_Redacted.pdf)† | City Research Online (City University London) | theory |  |
| 2016 | [Aphasia and dialogue: What eye movements reveal about the processing of cospeech gestures and the prediction of turn transitions](https://doi.org/10.7892/boris.85149)† | BORIS (University Library Bern) | theory |  |
| 2016 | [Autonomous animation of humanoid robots](https://doi.org/10.32657/10356/69279)† · [open copy](https://figshare.com/articles/thesis/Autonomous_Animation_of_Humanoid_Robots/6714932) | PhD thesis | method | Animates a NAO humanoid robot from a speech or music signal by labelling parameterized motions with meanings, selecting and synchronizing motion sequences, and checking their stability. |
| 2016 | [Investigation on whether co-verbal gesture use can facilitate lexical retrieval in connected speech in normal speakers and speakers with aphasia](https://hub.hku.hk/handle/10722/272653)‡ | Unknown venue | theory |  |
| 2016 | [What co-speech gestures do:investigating the communicative role ofvisual behaviour accompanyinglanguage use during reference ininteraction](https://etheses.whiterose.ac.uk/17319/)† | Unknown venue | theory |  |
| 2015 | [Animation and Interaction of Responsive, Expressive, and Tangible 3D Virtual Characters](https://dialnet.unirioja.es/servlet/tesis?codigo=73783)† | TDX | system | Thesis that relates gesture and pitch intensity to select gestures from a gesture motion graph for speech input, and presents BodySpeech, which generates gestures and facial animation from a speech signal. |
| 2015 | [Effects of individual differences and task demand on co-speech gesture](https://doi.org/10.17077/etd.p3eh1usp)† | Unknown venue | theory |  |
| 2015 | [Towards a theory of gesture form analysis : imaginary forms as part of gesture conceptualisation, with empirical support from motion-capture data](https://publications.rwth-aachen.de/search?p=id:%22RWTH-2016-04020%22)† | RWTH Publications (RWTH Aachen) | theory |  |
| 2014 | [151. Body movements in robotics](https://doi.org/10.1515/9783110302028.1943)† | Handbook chapter | survey | Overview chapter on body movements in robotics, covering communicative gesture, off-line and on-line motion generation, and transfer of multimodal motion scheduling from virtual agents to humanoid robots. |
| 2014 | [An integrative approach to understanding factors that influence monolingual and bilingual children's use of iconic co-speech gestures](https://doi.org/10.82308/53093)† | eScholarship@McGill (McGill) | theory |  |
| 2014 | [Generating gestures from speech for virtual humans using machine learning approaches](https://doi.org/10.25549/usctheses-c3-447274)† | USC | method | Learns a gesture generator from dyadic interview speech and motion capture by splitting the task into speech to gesture class and gesture class to gesture motion. |
| 2014 | [Towards an Interactive Human-Robot Relationship: Developing a Customized Robot Behavior to Human Profile.](https://pastel.archives-ouvertes.fr/tel-01128923)† | HAL | method | Generates head-arm metaphoric gestures for a robot from prosodic cues of human speech using Coupled Hidden Markov Models, within a personality- and emotion-adaptive multimodal behaviour system. |
| 2013 | [Alignment of Speech and Co-speech Gesture in a Constraint-based Grammar](https://era.ed.ac.uk/bitstream/1842/7623/1/Saint-Amand2013.pdf)† | Unknown venue | theory |  |
| 2013 | [An Analysis of Occupational Therapists� Listening Behaviors During Treatment Sessions](https://doi.org/10.33015/dominican.edu/2013.ot.09)† | Unknown venue | theory |  |
| 2013 | [Conceptual Motorics - Generation and Evaluation of Communicative Robot Gesture](https://pub.uni-bielefeld.de/record/2519214)† | Bielefeld University | method | A framework lets a humanoid robot produce synthetic speech and co-verbal hand and arm gestures at run-time, synchronised by a multimodal scheduler, and tests how humans evaluate such gestures in two studies. |
| 2013 | [Construction of Reconfigurable Motion Database for Real-Time Human-Robot Interaction](https://naist.repo.nii.ac.jp/records/10705)† | NAIST | method | Generates an android's body gestures in real time by reconfiguring a large motion-capture database, classified by bag-of-words and dynamic programming matching. |
| 2013 | [Modèles de gestes expressifs](https://hal.science/tel-01181000v1)† · [open copy](https://pastel.hal.science/tel-01181000/document) | HAL (Le Centre pour la Communication Scientifique Directe) | method | Computational model that encodes communicative gestures by hand shape, wrist position and trajectory, schedules them to speech and renders them with expressivity parameters on the Greta agent and the Nao robot. |
| 2013 | [What can people with aphasia communicate with their hands?: A study of representation techniques in pantomime and co-speech gesture](https://research.tilburguniversity.edu/en/publications/753fb803-f80d-4077-84a6-dcd5a33f98dd)‡ | Data Archiving and Networked Services (DANS) | theory |  |
| 2012 | [Chinese hands of time. The effects of language and culture on temporal gestures and spatio-temporal reasoning](https://research.tilburguniversity.edu/en/publications/9cddcc1b-26d1-48a2-a8f2-3d211cf9eb09)† | Data Archiving and Networked Services (DANS) | theory |  |
| 2012 | [Modeling nonverbal behaviors for virtual agents](http://dl.acm.org/citation.cfm?id=2518573)† | Thesis | method | Derives models that generate virtual agent nonverbal behaviour such as head nods, eyebrow movements and arm gestures, using literature-based rules and probabilistic models learned from speaker behaviour. |
| 2012 | [The Production of Co-Speech Iconic Gestures: Empirical Study and Computational Simulation with Virtual Agents](https://pub.uni-bielefeld.de/record/2460005)† | Bielefeld University | method | Develops GNetIc, a network model combining data-driven learning and rule-based decisions to generate speaker-specific iconic gestures for a virtual agent's speech. |
| 2011 | [Behavior generation for interpersonal coordination with virtual humans : on specifying, scheduling and realizing multimodal virtual human behavior](https://doi.org/10.3990/1.9789036532334)† · [open copy](https://ris.utwente.nl/ws/files/6035043/thesis_H_van_Welbergen.pdf) | Thesis | system |  |
| 2011 | [Co-ordination of speech and gesture in sequence and time : phonetic and non-verbal detail in face-to-face interaction](http://etheses.whiterose.ac.uk/1778/1/ReinSikvelandPhDThesis_2011.pdf)† | White Rose eTheses Online (University of Leeds, The University of Sheffield, University of York) | theory |  |
| 2011 | [Co-Speech Gesture in Communication and Cognition](http://hdl.handle.net/1794/12145)† | Scholars' Bank (University of Oregon) | theory |  |
| 2011 | [Generating Engagement Behaviors in Human-Robot Interaction](https://digitalcommons.wpi.edu/etd-theses/328)† | WPI | system | A ROS module adds gaze and pointing gestures to referring phrases and other connection events for a humanoid robot, plus an event-driven BML realizer for robots. |
| 2011 | [Nonverbal communication among Pointe Coupee Creoles](https://doi.org/10.31390/gradschool_dissertations.78)† | Unknown venue | theory |  |
| 2011 | [Prominence in gesture and speech in American English and Italian](https://docs.lib.purdue.edu/dissertations/AAI1510256)† | Purdue e-Pubs (Purdue University System) | theory |  |
| 2011 | [Reference in action : links between pointing and language](https://escholarship.org/uc/item/52g063b5)† | eScholarship (California Digital Library) | theory |  |
| 2011 | [Robotic gesture-speech synchronization](http://hdl.handle.net/10356/44964)† | DR-NTU | system | A text-to-speech-to-gesture engine that plans gestures, blends motions, generates beat gestures at run time and synchronises them with speech timings on the Olivia 2.1 robot. |
| 2011 | [The Talking Hands?: The Relation between Gesture and Language in Aphasic Patients](https://doi.org/10.15168/11572_368910)† | Unitn-eprints PhD (University of Trento) | theory |  |
| 2010 | [A comparative study of the development of multimodal narratives in french and zulu children and adults](http://hdl.handle.net/10068/856387)† | OpenGrey (Institut de l'Information Scientifique et Technique) | theory |  |
| 2010 | [Children's Gestures from 18 to 30 Months](https://lup.lub.lu.se/record/1700528)† | Lund University Publications (Lund University) | theory |  |
| 2010 | [Gesturing Through Time: Holds and Intermodal Timing in the Stream of Speech](http://pqdtopen.proquest.com/#viewpdf?dispub=3449059)† | ProQuest Demo Repository | theory |  |
| 2010 | [Space and Time in Our Hands](https://dspace.library.uu.nl/handle/1874/179364)† | Utrecht University Repository (Utrecht University) | theory |  |
| 2007 | ["Look at what I am saying": Multimodal science teaching](http://hdl.handle.net/1828/212)† | UVic’s Research and Learning Repository (University of Victoria) | theory |  |
| 2007 | [Crosslinguistic influence in first and second languages: Convergence in speech and gesture](http://edoc.mpg.de/328104)† | Max Planck Institute for Plasma Physics | theory |  |
| 2007 | [Links between language, gesture, and motor skill : a longitudinal study of communication recovery in adults with Broca's aphasia](https://doi.org/10.32469/10355/4656)† | Unknown venue | theory |  |
| 2006 | [Coordinated minds : how iconic co- speech gestures mediate communication](https://escholarship.org/uc/item/4ff658th)† | eScholarship (California Digital Library) | theory |  |
| 2006 | [Disfluency: Interrupting speech and gesture](https://doi.org/10.17617/2.59337)† | Radboud Repository (Radboud University) | theory |  |
| 2006 | [Gestures of a virtual guide](http://hmi.ewi.utwente.nl/verslagen/afstudeer/KesselMarcovanFinalThesis.pdf)† | University of Twente | system | Integrates existing dialogue, multimodal interface and agent software into a virtual guide that gives route descriptions in sentences and deictic pointing gestures. |
| 2003 | [Feedback Gesture Generation for Embodied Conversational Agents](https://www.nada.kth.se/utbildning/grukth/exjobb/rapportlistor/2003/rapporter03/bergenstrahle_malin_03133.pdf)† | KTH | method | Develops and implements an algorithm that generates feedback gestures for the non-speaking characters in multimodal dialogues produced by the NECA system, and evaluates their effect on viewers. |
| 2003 | [Gesture generation by imitation : from human behavior to computer character animation](https://doi.org/10.22028/d291-25852)† | Saarland University | method | Generates conversational gestures for an animated agent from annotated text by applying heuristic placement rules and filtering gestures with statistical gesture profiles of an individual speaker built from annotated TV talk show recordings. |
| 2002 | [Automatic extraction of spatial location for gesture generation](https://dspace.mit.edu/handle/1721.1/87236)‡ | MIT | method |  |
| 2001 | [Synthesis and acquisition of laban movement analysis qualitative parameters for communicative gestures](https://repository.upenn.edu/dissertations/AAI3015399)† · [open copy](https://repository.upenn.edu/cgi/viewcontent.cgi?article=1118&context=cis_reports) | University of Pennsylvania | method | The EMOTE system procedurally synthesizes communicative gestures from key poses and timing plus Laban Effort and Shape qualities, and extracts these qualities from motion capture or video. |
| 2000 | [Paired speech and gesture generation in embodied conversational agents](http://hdl.handle.net/1721.1/70733)† | MIT | method |  |
| 1998 | [Gesture in foreigner talk](https://repository.upenn.edu/dissertations/AAI9829850)† | Scholarly Commons (University of Pennsylvania) | theory |  |
| 1998 | [Producing semantically appropriate gestures in embodied language generation](http://hdl.handle.net/1721.1/62627)† · [open copy](https://dspace.mit.edu/bitstreams/c3c24bb6-7a36-47b7-9c77-49d6c57e4840/download) | MIT | method | Proposes hypotheses on distributing semantic information across speech and gesture and on realizing it in gestural forms, and builds a rule-based prototype to explore them. |
<!-- END:theses -->

## Datasets

<!-- BEGIN:datasets -->
| Dataset | Year | Modalities | Capture | Hours | Languages | Setting | Access | Papers here using it |
|---|---|---|---|---|---|---|---|---|
| [BEAT (Body-Expression-Audio-Text)](https://arxiv.org/abs/2203.05297) | 2022 | audio, text, body-motion, hand-motion, face-motion, annotations | mocap | 76 | en, zh, es, ja | monologue, dyadic | open | 37 |
| [BEAT2 (BEAT-SMPLX-FLAME)](https://arxiv.org/abs/2401.00374) | 2024 | audio, text, body-motion, hand-motion, face-motion | mocap | 60 |  | monologue, dyadic | open | 36 |
| [Trinity Speech-Gesture Dataset](http://www.tara.tcd.ie/handle/2262/91094) | 2018 | audio, body-motion, hand-motion | mocap | 4.07 | en | monologue | on-request | 23 |
| [SHOW (TalkSHOW dataset)](https://arxiv.org/abs/2212.04420) | 2023 | audio, body-motion, hand-motion, face-motion | pose-estimation | 26.9 |  |  | open | 21 |
| [TED Gesture Dataset](https://arxiv.org/abs/2009.02119) | 2020 | audio, text, body-motion | pose-estimation | 97 |  | monologue | open | 19 |
| [GENEA Challenge 2023 dataset](https://arxiv.org/abs/2308.12646) | 2023 | audio, text, body-motion, hand-motion | mocap | 18 | en | dyadic | open | 16 |
| [PATS (Pose, Audio, Transcript, Style)](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123630239.pdf) | 2020 | audio, text, body-motion | pose-estimation | 251 |  | monologue | open | 14 |
| [ZEGGS dataset (ZeroEGGS)](https://onlinelibrary.wiley.com/doi/10.1111/cgf.14734) | 2022 | audio, body-motion, hand-motion | mocap | 2.24 | en | monologue | open | 14 |
| [GENEA Challenge 2022 dataset](https://arxiv.org/abs/2208.10441) | 2022 | audio, text, body-motion, hand-motion | mocap | 19.3 | en | dyadic | open | 11 |
| [Talking With Hands 16.2M](https://openaccess.thecvf.com/content_ICCV_2019/papers/Lee_Talking_With_Hands_16.2M_A_Large-Scale_Dataset_of_Synchronized_Body-Finger_ICCV_2019_paper.pdf) | 2019 | audio, body-motion, hand-motion | mocap | 50 |  | dyadic | open | 9 |
| [TED-Expressive](https://arxiv.org/abs/2203.13161) | 2022 | audio, text, video, body-motion, hand-motion | pose-estimation | 100.8 |  | monologue | open | 9 |
| [Speech2Gesture dataset](https://arxiv.org/abs/1906.04160) | 2019 | audio, video, body-motion, hand-motion | pose-estimation | 144 |  | monologue | open | 8 |
| [HumanML3D](https://openaccess.thecvf.com/content/CVPR2022/papers/Guo_Generating_Diverse_and_Natural_3D_Human_Motions_From_Text_CVPR_2022_paper.pdf) | 2022 | text, body-motion | mocap | 28.59 |  |  | open | 7 |
| AMASS (Archive of Motion Capture As Surface Shapes) | 2019 | body-motion | mocap | 40 |  |  | on-request | 5 |
| [GENEA Challenge 2020 dataset](https://arxiv.org/abs/2102.11617) | 2020 | audio, text, body-motion | mocap | 4.07 | en | monologue | on-request | 4 |
| [SaGA (Bielefeld Speech and Gesture Alignment Corpus)](https://link.springer.com/article/10.1007/s12193-012-0106-8) | 2014 | audio, video, annotations |  | 1.13 | de | dyadic | on-request | 4 |
| [HDTF (High-Definition Talking Face)](https://openaccess.thecvf.com/content/CVPR2021/papers/Zhang_Flow-Guided_One-Shot_Talking_Face_Generation_With_a_High-Resolution_Audio-Visual_Dataset_CVPR_2021_paper.pdf) | 2021 | audio, video |  | 15.8 |  | monologue | open | 3 |
| Trinity Speech-Gesture Dataset II (TSGD2) |  | audio, body-motion, hand-motion, annotations | mocap | 6 | en | monologue | open | 3 |
| [Audio2Photoreal conversations dataset](https://arxiv.org/abs/2401.01885) | 2024 | audio, video, body-motion, face-motion | mocap | 8 |  | dyadic | open | 2 |
| [DnD Group Gesture Dataset](https://openaccess.thecvf.com/content/CVPR2024/html/Mughal_ConvoFusion_Multi-Modal_Conversational_Diffusion_for_Co-Speech_Gesture_Synthesis_CVPR_2024_paper.html) | 2024 | audio, text, video, body-motion, hand-motion, annotations | mocap | 6 | en | multi-party | open | 2 |
| [EVA Corpus (Multimodal corpus EVA 1.0)](https://doi.org/10.1007/s10579-022-09627-y) | 2020 | audio, video, text, annotations |  | 0.95 | sl | multi-party | open | 2 |
| [AIST++](https://arxiv.org/abs/2101.08779) | 2021 | video, audio, body-motion | pose-estimation | 5.2 |  |  | open | 1 |
| [AVSpeech](https://arxiv.org/abs/1804.03619) | 2018 | audio, video |  | 4700 |  | monologue | open | 1 |
| [BiGe](https://dl.acm.org/doi/pdf/10.1145/3577190.3614135) | 2023 | audio, text, body-motion, hand-motion | pose-estimation | 260.6 |  | monologue | open | 1 |
| [CelebV-HQ](https://arxiv.org/abs/2207.12393) | 2022 | video, annotations |  | 65 |  |  | open | 1 |
| [CMU Panoptic Studio Haggling dataset](https://arxiv.org/abs/1906.04158) | 2019 | audio, video, body-motion, hand-motion, face-motion, annotations | mocap | 3 |  | multi-party | open | 1 |
| [CSG-405](https://arxiv.org/abs/2507.06812) | 2025 | video, audio, body-motion, hand-motion, face-motion | pose-estimation | 405 |  |  |  | 1 |
| [Embody 3D](https://arxiv.org/abs/2510.16258) | 2025 | audio, text, body-motion, hand-motion, annotations | pose-estimation | 500 |  | dyadic, multi-party | on-request | 1 |
| [GES-Inter](https://arxiv.org/abs/2505.01746) | 2025 | audio, text, body-motion, hand-motion, face-motion, annotations | pose-estimation | 70 | en | dyadic | open | 1 |
| GES-X |  |  |  |  |  |  |  | 1 |
| Gest-IS (Multi-lingual Corpus of Gesture and Information Structure) | 2018 | audio, video, annotations |  | 0.83 | en | dyadic |  | 1 |
| [HoCo](https://arxiv.org/abs/2403.19467) | 2024 | video, audio, text, body-motion, hand-motion, face-motion, annotations | pose-estimation | 45 |  | dyadic |  | 1 |
| [InterAct](https://arxiv.org/abs/2509.05747) | 2025 | audio, text, body-motion, hand-motion, face-motion, annotations | mocap | 10 | en | dyadic | open | 1 |
| [JESTKOD database](https://doi.org/10.1007/s10579-016-9377-0) | 2015 | audio, video, body-motion, annotations | mocap |  | tr | dyadic |  | 1 |
| KIT Motion-Language Dataset |  |  |  |  |  |  |  | 1 |
| LecGesture |  |  |  |  |  |  |  | 1 |
| LISI-HHI |  |  |  |  |  |  |  | 1 |
| [MENTOR](https://arxiv.org/abs/2403.08764) | 2024 | video, audio, body-motion, hand-motion, face-motion | pose-estimation | 2320 | en | monologue |  | 1 |
| MSP-AVATAR corpus |  |  |  |  |  |  |  | 1 |
| MSR-VTT subset with 3D upper-body actions and text descriptions (as used in the paper) |  |  |  |  |  |  |  | 1 |
| [Multi-TPC](https://www.nature.com/articles/s41597-026-06819-x) | 2025 | audio, text, body-motion, annotations | mocap | 5.3 |  | multi-party | open | 1 |
| [Multiple Culture Gesture Dataset (MCGD)](https://dl.acm.org/doi/10.1145/3581783.3611705) | 2023 |  |  |  |  | monologue |  | 1 |
| [RoboGesture dataset](https://arxiv.org/abs/2608.28693) | 2026 | audio, text, body-motion, hand-motion, annotations | mixed | 1000 |  |  |  | 1 |
| [SAMP dataset](https://openaccess.thecvf.com/content/ICCV2021/html/Hassan_Stochastic_Scene-Aware_Motion_Prediction_ICCV_2021_paper.html) | 2021 | body-motion | mocap | 1.7 |  |  | on-request | 1 |
| [Seamless Interaction Dataset](https://arxiv.org/abs/2506.22554) | 2025 | audio, text, video, body-motion, hand-motion, face-motion, annotations | pose-estimation | 4000 |  | dyadic | open | 1 |
| [SeG (Semantic Gesture dataset)](https://arxiv.org/abs/2405.09814) | 2024 | body-motion, hand-motion, annotations | mocap |  |  |  | open | 1 |
| [TalkingHead-1KH](https://arxiv.org/abs/2011.15126) | 2021 | video |  | 1000 |  |  | open | 1 |
| [TED Emotion](https://arxiv.org/abs/2305.18891) | 2023 | audio, body-motion, annotations | pose-estimation |  |  | monologue | open | 1 |
| [TED-Culture Dataset](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1546765/full) | 2024 | audio, text, body-motion, hand-motion | pose-estimation | 17.5 | id, ja, de, it, fr, tr | monologue | open | 1 |
| [TED4C-L](https://arxiv.org/abs/2606.30001) | 2026 | audio, text, body-motion | pose-estimation | 106.45 | hi, it, ja, tr | monologue | open | 1 |
| [TFHP (Talking Face with Head Poses)](https://arxiv.org/abs/2310.00434) | 2024 | video, audio, face-motion | pose-estimation | 26.5 |  |  | on-request | 1 |
| [USC CreativeIT database](https://sail.usc.edu/publications/files/creativeit_database_mmc2010.pdf) | 2010 | audio, text, video, body-motion, annotations | mocap |  |  | dyadic | on-request | 1 |
| [VENUS](https://aclanthology.org/2025.acl-long.112/) | 2025 | text, body-motion, hand-motion, face-motion | pose-estimation | 14910 | en | dyadic | open | 1 |
| [WB-DH (Whole Body Digital Human Bench)](https://arxiv.org/abs/2508.08891) | 2025 | video, text, annotations |  |  |  |  | on-request | 1 |
| [AffectMoCap](https://arxiv.org/abs/2609.33311) | 2026 | audio, text, body-motion, hand-motion, annotations | mocap | 4 |  | monologue | unavailable | 0 |
| [Allo-AVA](https://arxiv.org/abs/2410.16503) | 2024 | video, audio, text, body-motion, face-motion, annotations | pose-estimation | 1250 | en | monologue, dyadic, multi-party | open | 0 |
| [Chinese News Anchor Speech Dataset (CNAS)](https://arxiv.org/abs/2505.03603) | 2025 | audio, video, body-motion, hand-motion | pose-estimation | 10.2 | zh | monologue | unavailable | 0 |
| [Embody 3D](https://arxiv.org/abs/2510.16258) | 2025 | audio, text, body-motion, hand-motion, annotations | pose-estimation | 500 |  | monologue, multi-party | on-request | 0 |
| [FineDance](https://arxiv.org/abs/2212.03741) | 2023 | audio, body-motion, hand-motion, annotations | mocap | 14.6 |  |  | open | 0 |
| IEMOCAP (Interactive Emotional Dyadic Motion Capture database) | 2008 | audio, video, text, face-motion, hand-motion, annotations | mocap | 12 | en | dyadic | on-request | 0 |
| [MM-Conv](https://arxiv.org/abs/2410.00253) | 2024 | audio, text, body-motion, hand-motion, face-motion | mocap | 6.7 |  | dyadic | open | 0 |
| [Motion-X](https://arxiv.org/abs/2307.00818) | 2023 | text, body-motion, hand-motion, face-motion, annotations | mixed |  |  |  | on-request | 0 |
| [ReactMotionNet](https://arxiv.org/abs/2603.15083) | 2026 | audio, text, body-motion, annotations | mixed |  | en | dyadic | open | 0 |
| [SceneGes](https://arxiv.org/abs/2609.00369) | 2026 | body-motion, hand-motion, face-motion | synthetic | 0.47 |  |  | unavailable | 0 |
| [Semantix](https://arxiv.org/abs/2605.30608) | 2026 | body-motion, hand-motion, text, annotations | mixed |  |  |  |  | 0 |
| [SIG-Chat](https://arxiv.org/abs/2509.23852) | 2025 | audio, text, body-motion, hand-motion, annotations | mocap | 9 | zh, en | dyadic |  | 0 |
| [Streamer](https://arxiv.org/abs/2507.22731) | 2025 | audio, body-motion, hand-motion | pose-estimation | 58 | zh | monologue | open | 0 |
| [ViCo](https://arxiv.org/abs/2112.13548) | 2022 | audio, video, face-motion, annotations | pose-estimation | 1.6 |  | dyadic | open | 0 |
| [YouTube Gesture Dataset](https://arxiv.org/abs/1810.12541) | 2019 | text, body-motion, hand-motion, face-motion | pose-estimation | 106.1 | en | monologue | open | 0 |
<!-- END:datasets -->

## Evaluation metrics

Objective metrics reported by the papers above. Human evaluation is recorded per paper in the `user_study` field.

<!-- BEGIN:metrics -->
| Metric | Also written | Measures | Better | What it computes | Papers here using it |
|---|---|---|---|---|---|
| Fréchet Gesture Distance | FGD | realism | lower | Computes the Fréchet distance between Gaussians fitted to latent features of real and generated gesture sequences, using the encoder of a pose-sequence autoencoder as the feature extractor. | 108 |
| Beat Alignment / Beat Consistency | BeatAlign, BA, BC, Beat Consistency Score, Beat Alignment Score | synchrony | higher | Detects motion beats (kinematic or bone-angle-change extrema) and audio beats (onsets) and averages a Gaussian-weighted distance between each beat and its nearest beat in the other stream. | 84 |
| Diversity (average feature or pose distance between generated clips) | Div | diversity | higher | Encodes generated gesture clips with the same feature extractor used for FGD and averages the feature distance over randomly paired clips. | 81 |
| Joint position or rotation error against ground truth | MAE, APE, MPJPE, L1, MSE | accuracy | lower | Averages the distance (L1, L2 or squared) between generated and ground-truth joint positions or rotations over joints and frames. | 33 |
| Fréchet Inception Distance (on motion or image features) | FID | realism | lower | Fits Gaussians to deep features of real and generated samples and computes the Fréchet distance between them from their means and covariances. | 31 |
| Acceleration and jerk statistics | MAJE, MAD, Jerk, Average jerk, Average acceleration | smoothness | closer-to-reference | Averages the magnitude of the second and third time derivatives of joint positions (acceleration and jerk) over generated motion, for comparison with the same statistics of natural motion. | 27 |
| Frame-level image quality | PSNR, SSIM, LPIPS | accuracy |  | Compares generated video frames to ground-truth frames with pixel error (PSNR), structural similarity (SSIM) or distance between deep network features (LPIPS). | 21 |
| Fréchet Video Distance | FVD | realism | lower | Computes the Fréchet distance between distributions of real and generated videos embedded with an I3D network pretrained on action recognition. | 21 |
| Face vertex or blendshape error | LVD, LVE, Lip Vertex Error, MSE (face), vertex MSE | accuracy | lower | Measures geometric error of generated face meshes against ground truth, typically the maximal L2 error over lip vertices per frame averaged over all test frames. | 19 |
| Lip synchronisation confidence or distance | Sync-C, Sync-D, LSE-C, LSE-D | synchrony |  | Feeds generated mouth crops and audio to a pretrained SyncNet and reports the average audio-visual embedding distance (LSE-D, lower is better) and the average sync confidence (LSE-C, higher is better). | 17 |
| L1 Diversity | L1div, L1 Div. | diversity | higher | Splits generated motion into equal-length clips and averages the L1 distance between joint positions of every pair of clips. | 14 |
| Semantic-Relevant Gesture Recall | SRGR, Semantic Relevance Gesture Recall | semantics | higher | Computes PCK against ground truth with each frame weighted by its annotated semantic-relevance score, so semantically relevant gestures count more. | 13 |
| Gesture label prediction F1, precision, recall or accuracy | F1, macro F1, F-measure, F-score, precision, recall, classification accuracy, label accuracy, prediction accuracy | accuracy | higher | Compares predicted gesture labels (such as gesture type, property or timing) with annotated reference labels and reports F1, precision, recall or accuracy. | 8 |
| Percentage of Correct Keypoints | PCK | accuracy | higher | Counts a predicted keypoint as correct when it lies within alpha times the larger side of the person bounding box from the ground-truth keypoint and reports the fraction of correct keypoints. | 8 |
| Canonical Correlation Analysis against ground truth | CCA | accuracy | higher | Projects generated and reference poses onto a joint subspace with linear transformations chosen to maximise the Pearson correlation between them, and reports that correlation. | 6 |
| Facial identity similarity | CSIM, identity similarity, identity cosine similarity, facial identity similarity | accuracy | higher |  | 6 |
| Hand Keypoint Confidence | HKC, Hand-C, keypoint confidence | realism | higher |  | 6 |
| Velocity histogram distance (Hellinger distance) | HD, Hellinger distance, speed histogram distance | realism | lower | Builds histograms of joint speed for generated and natural motion and computes the Hellinger distance between them. | 6 |
| Hand Keypoint Variance | HKV, Hand-V, hand keypoint variance | diversity | higher |  | 5 |
| Multimodality (variation for the same input) | MM | diversity |  | Averages the feature distance between several motions generated from the same input, measuring how varied the outputs are for one condition. | 5 |
| Fréchet Motion Distance | FMD | realism | lower | Computes the Fréchet distance between latent feature distributions of real and generated holistic motion (expression plus gesture), extending FGD from body gestures to the whole motion. | 4 |
| No-reference image or video quality and aesthetic scores | IQA, ASE, Q-Align, VQAA, VQAT, aesthetic quality, imaging quality | realism | higher |  | 4 |
| Retrieval precision of motion from text or speech | R-Precision, R-Prec, Top-1, Top-2, Top-3 | semantics | higher | Ranks the true condition among 31 mismatched ones by feature distance to each generated motion and reports how often it lands in the top 1, 2 or 3. | 4 |
| Emotion recognition accuracy | EA, emotion accuracy, emotion classification accuracy, gesture emotion accuracy | other | higher |  | 3 |
| Expression FID | E-FID, EFID | realism | lower |  | 3 |
| Multimodal Distance | MM-Dist, MM-Distance, multi-modal distance | semantics | lower |  | 3 |
| Cosine similarity to ground-truth motion | cosine similarity | accuracy | higher |  | 2 |
| Word Error Rate of synthesised speech | WER, word error rate, character error rate, CER | other | lower |  | 2 |
| Foot sliding (skating) | foot sliding, Skate, skating, skating velocity, contact sliding | realism | lower |  | 1 |
| Gesture Cluster Affinity | GCA |  | higher | A cluster-based score introduced with the RIDGE system that rates how well generated gestures fit the gesture clusters of the reference data, on which ground truth scores 0.90. | 1 |
| Mean Velocity Difference (MVD) |  |  |  |  | 1 |
| Salient Motion Similarity (SMS) |  |  |  |  | 1 |
| Style recognition accuracy | SRA, Style Recognition Accuracy, style identification accuracy, ExtStyle Top-1 | other | higher |  | 1 |
| Retrieval Recall@K (R@1, R@5, R@10) | R@K, Recall@K | semantics | higher | Embeds speech (or text) and motion with a contrastively trained model and reports the percentage of queries whose matching clip is among the top K retrieved results. | 0 |
| Smooth Beat Consistency (Smooth-BC) | Smooth-BC | synchrony | higher | A beat consistency score whose motion beats are velocity minima that also satisfy a slope constraint, so jitter is not counted as rhythmic pauses aligned to audio beats. | 0 |
| Workspace Violation |  | other | lower | Measures the maximum distance by which either wrist moves outside its prescribed workspace box, averaged over the test set. | 0 |
<!-- END:metrics -->

## Contributing

Add one record to `data/papers/<year>.yaml` following [docs/SCHEMA.md](docs/SCHEMA.md) and open a pull request. Inclusion rule: the work must be peer reviewed (journal, conference, workshop or book chapter) or an examined thesis, publicly identifiable (DOI or proceedings page) and inside the scope above. The validator rejects `type: preprint`.

Check your record and regenerate the tables before opening the pull request:

```bash
pip install -r requirements.txt
python scripts/validate.py
python scripts/build_readme.py
```

## License

List content (the data, the README tables and the documentation): CC0 1.0, see [LICENSE-DATA](LICENSE-DATA). Scripts: MIT, see [LICENSE](LICENSE).
