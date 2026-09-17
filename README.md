<div align="center">

<img src="assets/banner.svg" alt="From Watching to Reasoning: acquisition, memory, control, and verification for long-video agents" width="100%">

# Awesome Long-Video Agent Papers

**A curated research guide to agentic systems for long-form video understanding.**

[![Papers](https://img.shields.io/badge/Papers-101-0f766e?style=flat-square)](papers/index.md)
[![Taxonomy](https://img.shields.io/badge/Taxonomy-4_stages_%C2%B7_16_categories-6366f1?style=flat-square)](#taxonomy)
[![Survey](https://img.shields.io/badge/Survey-In_preparation-475569?style=flat-square)](#about-the-survey)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-16a34a?style=flat-square)](CONTRIBUTING.md)
[![GitHub](https://img.shields.io/badge/GitHub-white?style=flat-square)](https://github.com/PhuTran1005/Awesome-Long-Video-Agent-Papers)
[![License](https://img.shields.io/badge/License-Apache_2.0-2563eb?style=flat-square)](LICENSE)

**[Badge colors](#badge-colors)** · **[Recent additions](#recent-additions)** · **[Explore the taxonomy](#taxonomy)** · **[Browse all papers](papers/index.md)** · **[Get BibTeX](references.bib)** · **[Suggest a paper](https://github.com/PhuTran1005/Awesome-Long-Video-Agent-Papers/issues/new?template=paper.yml)**

</div>

## About the Survey

This repository accompanies **From Watching to Reasoning: A Comprehensive Survey of Agentic Systems for Long-Form Video Understanding**, a survey manuscript in preparation.

Long videos make exhaustive, high-resolution processing expensive. Video agents address this challenge through **active evidence seeking**: they decide where to look, what to remember, which tool to call, and when the available evidence supports an answer. We organize this literature around four connected functions of the agent loop.

> **What makes a video system agentic?** A later video-evidence action depends on an observation made earlier in the same inference trajectory. The defining feature is feedback from observed evidence into the next action.

<p align="center">
  <a href="assets/survey-teaser.png"><img src="assets/survey-teaser.png" alt="Survey teaser comparing conventional video processing, LLM-based video understanding, and an agentic loop with planning, observation, memory, verification, and multimodal evidence" width="960"></a>
  <br><sub>From passive processing to adaptive evidence seeking. Click the figure to view it at full resolution.</sub>
</p>

## Badge Colors

| Badge | Meaning |
| :--- | :--- |
| ![arXiv](https://img.shields.io/badge/arXiv-red?style=flat-square) | `red` for arXiv papers |
| ![Conference / Journal](https://img.shields.io/badge/Conference%20%2F%20Journal-blue?style=flat-square) | `blue` for conference/journal papers |
| ![GitHub](https://img.shields.io/badge/GitHub-white?style=flat-square) | `white` for GitHub repositories |
| ![Research area](https://img.shields.io/badge/Research%20area-purple?style=flat-square) | `purple` for research areas |
| ![Category](https://img.shields.io/badge/Category-green?style=flat-square) | `green` for categories |

Publication badges follow the venue recorded in the bibliography. A conference or journal paper may also have a red **arXiv** link to its preprint. Purple badges identify the broad research areas of the survey; green badges identify mechanisms within each area.

## Recent Additions

A growing reading list of **new methods that have not yet been incorporated into the survey taxonomy**. This section provides a home for future papers as the field evolves.

**[Browse recent additions →](papers/recent-additions.md)** · **[Suggest a new method](https://github.com/PhuTran1005/Awesome-Long-Video-Agent-Papers/issues/new?template=paper.yml)**

Entries are listed by release date, newest first. Suggested categories are provisional; papers join the taxonomy catalog after review and integration into the manuscript. The taxonomy counts below cover the classified collection.

## Taxonomy

Choose a stage to explore its mechanisms, papers, and publication links.

<!-- catalog-stats:start -->
**101 unique papers · 102 citation keys · 4 stages · 16 categories**
<!-- catalog-stats:end -->

<table>
<tr>
<td width="50%" valign="top">

### Evidence Acquisition

[![Evidence Acquisition](https://img.shields.io/badge/Evidence%20Acquisition-purple?style=flat-square)](papers/evidence-acquisition.md)

**Where should the agent look next?**

[![Retrieval-based](https://img.shields.io/badge/Retrieval--based-green?style=flat-square)](papers/evidence-acquisition.md#retrieval-based) [![Hierarchical](https://img.shields.io/badge/Hierarchical-green?style=flat-square)](papers/evidence-acquisition.md#hierarchical) [![Programmatic](https://img.shields.io/badge/Programmatic-green?style=flat-square)](papers/evidence-acquisition.md#programmatic) [![Learned policy](https://img.shields.io/badge/Learned%20policy-green?style=flat-square)](papers/evidence-acquisition.md#learned-policy)

[**Explore 33 papers →**](papers/evidence-acquisition.md)

</td>
<td width="50%" valign="top">

### Memory & State

[![Memory &amp; State Representation](https://img.shields.io/badge/Memory%20%26%20State%20Representation-purple?style=flat-square)](papers/memory-state.md)

**What should the agent remember?**

[![Caption / Text](https://img.shields.io/badge/Caption%20%2F%20Text-green?style=flat-square)](papers/memory-state.md#caption-text) [![Structured](https://img.shields.io/badge/Structured-green?style=flat-square)](papers/memory-state.md#structured) [![Latent / Compressed](https://img.shields.io/badge/Latent%20%2F%20Compressed-green?style=flat-square)](papers/memory-state.md#latent-compressed) [![Streaming / Online](https://img.shields.io/badge/Streaming%20%2F%20Online-green?style=flat-square)](papers/memory-state.md#streaming-online)

[**Explore 32 papers →**](papers/memory-state.md)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### Control & Planning

[![Control &amp; Planning](https://img.shields.io/badge/Control%20%26%20Planning-purple?style=flat-square)](papers/control-planning.md)

**Which action should the agent take?**

[![Fixed workflow](https://img.shields.io/badge/Fixed%20workflow-green?style=flat-square)](papers/control-planning.md#fixed-workflow) [![Autonomous tool use](https://img.shields.io/badge/Autonomous%20tool%20use-green?style=flat-square)](papers/control-planning.md#autonomous-tool-use) [![Multi-agent](https://img.shields.io/badge/Multi--agent-green?style=flat-square)](papers/control-planning.md#multi-agent) [![Learned control](https://img.shields.io/badge/Learned%20control-green?style=flat-square)](papers/control-planning.md#learned-control)

[**Explore 34 papers →**](papers/control-planning.md)

</td>
<td width="50%" valign="top">

### Verification & Aggregation

[![Verification &amp; Aggregation](https://img.shields.io/badge/Verification%20%26%20Aggregation-purple?style=flat-square)](papers/verification-aggregation.md)

**Is the evidence sufficient to answer?**

[![Self-consistency](https://img.shields.io/badge/Self--consistency-green?style=flat-square)](papers/verification-aggregation.md#self-consistency) [![Reflection / Refine](https://img.shields.io/badge/Reflection%20%2F%20Refine-green?style=flat-square)](papers/verification-aggregation.md#reflection-refine) [![Confidence / Calibration](https://img.shields.io/badge/Confidence%20%2F%20Calibration-green?style=flat-square)](papers/verification-aggregation.md#confidence-calibration) [![Evidence alignment &amp; Adjudication](https://img.shields.io/badge/Evidence%20alignment%20%26%20Adjudication-green?style=flat-square)](papers/verification-aggregation.md#evidence-alignment-adjudication)

[**Explore 17 papers →**](papers/verification-aggregation.md)

</td>
</tr>
</table>

Papers can contribute to several stages, so category counts overlap. Assignments follow the manuscript taxonomy. The collection also includes **agent-enabling baselines and foundational methods**; inclusion in a branch does not imply that every method independently satisfies the closed-loop criterion.

## Find Your Reading Path

| If you are interested in… | Start here | Continue with |
| :--- | :--- | :--- |
| Searching long videos efficiently | [Retrieval-based acquisition](papers/evidence-acquisition.md#retrieval-based) | [Hierarchical acquisition](papers/evidence-acquisition.md#hierarchical) |
| Remembering events across long horizons | [Structured memory](papers/memory-state.md#structured) | [Streaming / online memory](papers/memory-state.md#streaming-online) |
| Learning to reason with video tools | [Learned acquisition policies](papers/evidence-acquisition.md#learned-policy) | [Learned control](papers/control-planning.md#learned-control) |
| Coordinating specialized agents | [Multi-agent systems](papers/control-planning.md#multi-agent) | [Evidence alignment & adjudication](papers/verification-aggregation.md#evidence-alignment-adjudication) |
| Making answers more trustworthy | [Reflection / refinement](papers/verification-aggregation.md#reflection-refine) | [Confidence / calibration](papers/verification-aggregation.md#confidence-calibration) |

For a chronological view, open the **[complete paper index](papers/index.md)** and search by method, title, or first author.

## Collection & Bibliography

The collection maps the manuscript's `sections/taxonomy.tex` to `custom.bib` using exact citation keys. Bibliographic years and venues are retained from that source; a linked preprint may have an earlier release date than the listed publication year.

| Resource | What you will find |
| :--- | :--- |
| [Recent additions](papers/recent-additions.md) | New methods awaiting taxonomy integration, with provisional categories |
| [Taxonomy paper index](papers/index.md) | A deduplicated index, organized by year, with links back to each taxonomy branch |
| [BibTeX bibliography](references.bib) | All taxonomy citation records, with their original keys |
| [Structured catalog](data/catalog.json) | Titles, authors, venues, citation aliases, and all category assignments |
| [Data notes](docs/DATA_NOTES.md) | Provenance, duplicate handling, link sources, and metadata conventions |

**arXiv / Paper** badges link to publication or preprint pages. White **GitHub** badges link to verified code repositories when available. **BibTeX** links jump to the corresponding source record. Where a direct identifier is unavailable, **Find paper** explicitly opens a title search. Full author lists are available in the bibliography and structured catalog.

## Contributing

Relevant papers, metadata corrections, and taxonomy suggestions are welcome. Please include a primary publication link and explain how the work fits a stage of the agent loop.

**[Read the contribution guide](CONTRIBUTING.md)** · **[Suggest a paper](https://github.com/PhuTran1005/Awesome-Long-Video-Agent-Papers/issues/new?template=paper.yml)** · **[Report a correction](https://github.com/PhuTran1005/Awesome-Long-Video-Agent-Papers/issues/new?template=correction.yml)**

## Citation

The survey's public paper link and formal citation will be added when available. Until then, please cite the individual papers using [references.bib](references.bib).

## Acknowledgments & License

The repository layout is inspired by [Awesome Multimodal Token Compression](https://github.com/cokeshao/Awesome-Multimodal-Token-Compression). We thank the authors whose research makes this collection possible.

Repository materials are provided under the existing [Apache 2.0 license](LICENSE). Linked papers and external resources remain subject to their respective licenses.

<p align="center"><sub>Explore the evidence. Follow the reasoning. Keep the sources close.</sub></p>
