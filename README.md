<div align="center">

<a href="#taxonomy"><img src="assets/banner.png" alt="Beyond Passive Watching: a comprehensive survey of agentic systems for long-form video understanding" width="100%"></a>

# Awesome Long-Video Agent Papers

**A curated, taxonomy-organized reading list on agentic systems for long-form video understanding.**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-4a9a62?style=flat)](CONTRIBUTING.md)
[![Stars](https://img.shields.io/github/stars/PhuTran1005/Awesome-Long-Video-Agent-Papers?style=social&label=Stars)](https://github.com/PhuTran1005/Awesome-Long-Video-Agent-Papers)

[![Papers](https://img.shields.io/badge/Papers-106-4a82c9?style=flat)](papers/index.md)
[![Taxonomy](https://img.shields.io/badge/Taxonomy-4_stages_%C2%B7_16_categories-6b7280?style=flat)](#taxonomy)
[![Survey](https://img.shields.io/badge/Survey-In_preparation-b8921a?style=flat)](#about-the-survey)
[![License](https://img.shields.io/badge/License-Apache_2.0-6b7280?style=flat)](LICENSE)

[**Taxonomy**](#taxonomy) &nbsp;·&nbsp; [**All papers by year**](papers/index.md) &nbsp;·&nbsp; [**Recent additions**](papers/recent-additions.md) &nbsp;·&nbsp; [**BibTeX**](references.bib) &nbsp;·&nbsp; [**Suggest a paper**](https://github.com/PhuTran1005/Awesome-Long-Video-Agent-Papers/issues/new?template=paper.yml)

</div>

## About the Survey

This repository accompanies **Beyond Passive Watching: A Comprehensive Survey of Agentic Systems for Long-Form Video Understanding**, a survey manuscript in preparation.

**[Project page](https://phutran1005.github.io/Awesome-Long-Video-Agent-Papers/) ? [Source, local preview, and deployment](docs/PROJECT_PAGE.md)**

Long videos make exhaustive, high-resolution processing expensive. Video agents address this challenge through **active evidence seeking**: they decide where to look, what to remember, which tool to call, and when the available evidence supports an answer. We organize this literature around four connected functions of the agent loop: **acquire** evidence, **remember** it, **plan** the next action, and **verify** the answer.

> [!NOTE]
> **What makes a video system agentic?** A later video-evidence action depends on an observation made earlier in the same inference trajectory. The defining feature is feedback from observed evidence into the next action.

<p align="center">
  <a href="assets/survey-teaser.png"><img src="assets/survey-teaser.png" alt="Survey teaser comparing conventional video processing, LLM-based video understanding, and an agentic loop with planning, observation, memory, verification, and multimodal evidence" width="880"></a>
  <br><sub>From passive processing to adaptive evidence seeking. Click the figure to view it at full resolution.</sub>
</p>

## Statistics

<p align="center">
  <img src="assets/publication-growth.png" width="760" alt="Number of papers on agentic systems for long-form video understanding per publication year">
  <br><sub>Papers on agentic systems for long-form video understanding, by publication year. The 2026 cutoff is September 2026.</sub>
</p>

## Recent Additions

A growing reading list of **new methods that have not yet been incorporated into the survey taxonomy**. Entries are listed by release date, newest first, with provisional categories; papers join the taxonomy catalog after review and integration into the manuscript.

**[Browse recent additions →](papers/recent-additions.md)** · **[Suggest a new method](https://github.com/PhuTran1005/Awesome-Long-Video-Agent-Papers/issues/new?template=paper.yml)**

## Find Your Reading Path

| If you are interested in… | Start here | Continue with |
| :--- | :--- | :--- |
| Searching long videos efficiently | [Retrieval-based acquisition](#retrieval-based) | [Hierarchical acquisition](#hierarchical) |
| Remembering events across long horizons | [Structured memory](#structured) | [Streaming memory](#streaming) |
| Learning to reason with video tools | [Learned acquisition policies](#learned-acquisition) | [Learned control](#learned-control) |
| Coordinating specialized agents | [Multi-agent systems](#multi-agent) | [Evidence alignment & adjudication](#evidence-alignment) |
| Making answers more trustworthy | [Reflection / refine](#reflection) | [Confidence / uncertainty](#confidence) |

For a chronological view, open the **[complete paper index](papers/index.md)** and search by method, title, or first author.

## Taxonomy

Every paper in the survey is listed below, grouped by stage and mechanism. **Pick a stage card** to jump straight to its tables.

<!-- catalog-stats:start -->
**106 unique papers · 4 stages · 16 categories**
<!-- catalog-stats:end -->

<!-- taxonomy:start -->
<div align="center">
  <a href="#evidence-acquisition"><img src="assets/card-evidence-acquisition.png" width="49%" alt="Stage 1: Evidence Acquisition"></a>
  <a href="#memory-state"><img src="assets/card-memory-state.png" width="49%" alt="Stage 2: Memory &amp; State Representation"></a>
  <a href="#control-planning"><img src="assets/card-control-planning.png" width="49%" alt="Stage 3: Control &amp; Planning"></a>
  <a href="#verification-aggregation"><img src="assets/card-verification-aggregation.png" width="49%" alt="Stage 4: Verification &amp; Aggregation"></a>
</div>

<p align="center">
  <a href="assets/taxonomy.png"><img src="assets/taxonomy.png" alt="Stage-centered taxonomy of long-video agents and agent-enabling methods" width="720"></a>
  <br><sub><b>The method-level taxonomy</b> from the survey appendix. Click to view at full resolution.</sub>
</p>

> **Reading the tables.** Categories are *non-exclusive*: a paper appears under every branch where it makes a substantive methodological contribution. Unmarked entries are *core video agents* whose later evidence-access actions depend on earlier video-derived observations. Entries marked with <sup>†</sup> (18 papers) are *agent-enabling methods or conceptual precursors*: they contribute useful video processing, memory, retrieval, or reflection mechanisms without independently establishing closed-loop video-evidence behavior.

<a id="evidence-acquisition"></a>

## Evidence Acquisition

<img src="assets/header-evidence-acquisition.png" width="100%" alt="Stage 1: Where should the agent look next?">

<div align="center">

[![Retrieval 16](https://img.shields.io/badge/Retrieval-16-c0609f?style=flat&labelColor=555)](#retrieval-based) [![Hierarchical 10](https://img.shields.io/badge/Hierarchical-10-c0609f?style=flat&labelColor=555)](#hierarchical) [![Learned policies 10](https://img.shields.io/badge/Learned%20policies-10-c0609f?style=flat&labelColor=555)](#learned-acquisition) [![Programmatic 2](https://img.shields.io/badge/Programmatic-2-c0609f?style=flat&labelColor=555)](#programmatic)

</div>

<a id="retrieval-based"></a>

<details>
<summary><b>Retrieval-Based Acquisition</b> &nbsp;<img src="https://img.shields.io/badge/16_papers-c0609f?style=flat" alt="16 papers">&nbsp; <sub><i>👆 click to expand</i></sub></summary>

Retrieve relevant moments, documents, or multimodal evidence in response to a query.

| Method | Paper | Links |
| :--- | :--- | :--- |
| <strong>DVD</strong><br>![NeurIPS 2026](https://img.shields.io/badge/NeurIPS-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2505.18079">Deep video discovery: Agentic search with tool use for long-form video understanding</a><br><sub>Xiaoyi Zhang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2505.18079) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L360) |
| <strong>EventMemAgent</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2602.15329">EventMemAgent: Hierarchical Event-Centric Memory for Online Video Understanding with Adaptive Tool Use</a><br><sub>Siwei Wen et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2602.15329) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L394) |
| <strong>FALCONEye</strong><br>![WACV 2026](https://img.shields.io/badge/WACV-2026-blue?style=flat&labelColor=555) | FALCONEye: Finding Answers and Localizing Content in ONE-hour-long videos with multi-modal LLMs<br><sub>Carlos Plou et al.</sub> | [Find&nbsp;paper](https://scholar.google.com/scholar?q=%22FALCONEye%3A%20Finding%20Answers%20and%20Localizing%20Content%20in%20ONE-hour-long%20videos%20with%20multi-modal%20LLMs%22) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L425) |
| <strong>MERIT</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2608.07663">Keep It Simple: Multi-Key Episodic Memory Retrieval for Ultra-Long Video Understanding</a><br><sub>Yeeun Choi et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2608.07663) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L411) |
| <strong>OmniRAG-Agent</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2602.03707">OmniRAG-Agent: Agentic Omnimodal Reasoning for Low-Resource Long Audio-Video Question Answering</a><br><sub>Yifan Zhu et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2602.03707) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L384) |
| <strong>PyraVid</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2605.17065">PyraVid: Hierarchical Multimodal Memory for Long-Horizon Video Reasoning</a><br><sub>Sikuan Yan et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2605.17065) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L404) |
| <strong>TRACE</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2608.22516">TRACE: Temporal Retrieval with Anchored and Convergent Evidence for Long-Horizon Video Understanding</a><br><sub>Pengyiang Liu et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2608.22516) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L418) |
| <strong>VESTA</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2608.31005">From Intent to Evidence: Policy-Steered Multi-Strategy Retrieval for Long-Video Agents</a><br><sub>Can Zhang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2608.31005) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L434) |
| <strong>VideoRAG<sup>†</sup></strong><br>![KDD 2026](https://img.shields.io/badge/KDD-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2502.01549">Videorag: Retrieval-augmented generation with extreme long-context videos</a><br><sub>Xubin Ren et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2502.01549) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L352)<br>[![Code, GitHub stars for HKUDS/VideoRAG](https://img.shields.io/github/stars/HKUDS/VideoRAG?style=flat&logo=github&logoColor=white&label=Code&labelColor=24292f&color=57606a)](https://github.com/HKUDS/VideoRAG) |
| <strong>VideoSeek</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2603.20185">VideoSeek: Long-Horizon Video Agent with Tool-Guided Seeking</a><br><sub>Jingyang Lin et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2603.20185) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L369) |
| <strong>VSeek</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2607.02959">Incentivizing Vision Language Models to Search for Long Video Question Answering</a><br><sub>Harsh Goel et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2607.02959) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L377) |
| <strong>AVI</strong><br>![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2511.14446">Agentic Video Intelligence: A Flexible Framework for Advanced Video Exploration and Understanding</a><br><sub>Hong Gao et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2511.14446) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L345) |
| <strong>DrVideo</strong><br>![CVPR 2025](https://img.shields.io/badge/CVPR-2025-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2406.12846">Drvideo: Document retrieval based long video understanding</a><br><sub>Ziyu Ma et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2406.12846) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L337)<br>[![Code, GitHub stars for Upper9527/DrVideo](https://img.shields.io/github/stars/Upper9527/DrVideo?style=flat&logo=github&logoColor=white&label=Code&labelColor=24292f&color=57606a)](https://github.com/Upper9527/DrVideo) |
| <strong>GraphVideoAgent</strong><br>![ACM MM 2025](https://img.shields.io/badge/ACM%20MM-2025-blue?style=flat&labelColor=555) | <a href="https://doi.org/10.1145/3746027.3755537">GraphVideoAgent: Enhancing Long-form Video Understanding with Entity Relation Graphs</a><br><sub>Meng Chu et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://doi.org/10.1145/3746027.3755537) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L319) |
| <strong>VideoExplorer</strong><br>![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2506.10821">VideoExplorer: Think With Videos For Agentic Long-Video Understanding</a><br><sub>Huaying Yuan et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2506.10821) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L309) |
| <strong>VideoAgent</strong><br>![ECCV 2024](https://img.shields.io/badge/ECCV-2024-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2403.10517">Videoagent: Long-form video understanding with large language model as agent</a><br><sub>Xiaohan Wang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2403.10517) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L266)<br>[![Code, GitHub stars for wxh1996/VideoAgent](https://img.shields.io/github/stars/wxh1996/VideoAgent?style=flat&logo=github&logoColor=white&label=Code&labelColor=24292f&color=57606a)](https://github.com/wxh1996/VideoAgent) |

<div align="right"><a href="#taxonomy">↑ Back to taxonomy</a></div>

</details>

<a id="hierarchical"></a>

<details>
<summary><b>Hierarchical Acquisition</b> &nbsp;<img src="https://img.shields.io/badge/10_papers-c0609f?style=flat" alt="10 papers">&nbsp; <sub><i>👆 click to expand</i></sub></summary>

Navigate from coarse summaries to finer temporal or spatial evidence.

| Method | Paper | Links |
| :--- | :--- | :--- |
| <strong>AOP-Agent</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2605.28192">Agentic Active Omni-Modal Perception for Multi-Hop Audio-Visual Reasoning</a><br><sub>Ke Xu et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2605.28192) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L501) |
| <strong>GOPAgen</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2606.06532">GOPAgen: Motion-Aware and Efficient Agentic Long-Video Understanding with Structural Memory and Hierarchical Reasoning</a><br><sub>Haozhe Chi et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2606.06532) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L511) |
| <strong>HAVEN</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | Hierarchical Long Video Understanding with Audiovisual Entity Cohesion and Agentic Search<br><sub>Xinlei Yin et al.</sub> | [Find&nbsp;paper](https://scholar.google.com/scholar?q=%22Hierarchical%20Long%20Video%20Understanding%20with%20Audiovisual%20Entity%20Cohesion%20and%20Agentic%20Search%22) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L492) |
| <strong>Homer</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2607.02588">Homer: Understanding Long-form Videos with Hierarchical Memory and Agentic Reasoning</a><br><sub>Yixin Ji et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2607.02588) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L521) |
| <strong>MM-MEM</strong><br>![ACL 2026](https://img.shields.io/badge/ACL-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2603.01455">From verbatim to gist: Distilling pyramidal multimodal memory via semantic information bottleneck for long-horizon video agents</a><br><sub>Niu Lian et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2603.01455) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L476) |
| <strong>VideoARM</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2512.12360">Videoarm: Agentic reasoning over hierarchical memory for long-form video understanding</a><br><sub>Yufei Yin et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2512.12360) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L484) |
| <strong>VideoLucy</strong><br>![NeurIPS 2026](https://img.shields.io/badge/NeurIPS-2026-blue?style=flat&labelColor=555) | Videolucy: Deep memory backtracking for long video understanding<br><sub>Jialong Zuo et al.</sub> | [Find&nbsp;paper](https://scholar.google.com/scholar?q=%22Videolucy%3A%20Deep%20memory%20backtracking%20for%20long%20video%20understanding%22) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L457) |
| <strong>ZoomV</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2504.01407">ZoomV: Temporal Zoom-in for Efficient Long Video Understanding</a><br><sub>Yuan Zhang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2504.01407) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L466) |
| <strong>T*</strong><br>![CVPR 2025](https://img.shields.io/badge/CVPR-2025-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2504.02259">Re-thinking temporal search for long-form video understanding</a><br><sub>Jinhui Ye et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2504.02259) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L441) |
| <strong>VideoTree</strong><br>![CVPR 2025](https://img.shields.io/badge/CVPR-2025-blue?style=flat&labelColor=555) | Videotree: Adaptive tree-based video representation for llm reasoning on long videos<br><sub>Ziyang Wang et al.</sub> | [Find&nbsp;paper](https://scholar.google.com/scholar?q=%22Videotree%3A%20Adaptive%20tree-based%20video%20representation%20for%20llm%20reasoning%20on%20long%20videos%22) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L449) |

<div align="right"><a href="#taxonomy">↑ Back to taxonomy</a></div>

</details>

<a id="learned-acquisition"></a>

<details>
<summary><b>Learned Acquisition Policies</b> &nbsp;<img src="https://img.shields.io/badge/10_papers-c0609f?style=flat" alt="10 papers">&nbsp; <sub><i>👆 click to expand</i></sub></summary>

Learn when, where, or at what granularity to acquire the next observation.

| Method | Paper | Links |
| :--- | :--- | :--- |
| <strong>Conan</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2510.20470">Conan: Progressive learning to reason like a detective over multi-scale visual evidence</a><br><sub>Kun Ouyang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2510.20470) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L540) |
| <strong>EVA</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2603.22918">EVA: Efficient Reinforcement Learning for End-to-End Video Agent</a><br><sub>Yaolun Zhang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2603.22918) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L232) |
| <strong>EventMemAgent</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2602.15329">EventMemAgent: Hierarchical Event-Centric Memory for Online Video Understanding with Adaptive Tool Use</a><br><sub>Siwei Wen et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2602.15329) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L394) |
| <strong>LongVT</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2511.20785">Longvt: Incentivizing" thinking with long videos" via native tool calling</a><br><sub>Zuhao Yang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2511.20785) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L548)<br>[![Code, GitHub stars for EvolvingLMMs-Lab/LongVT](https://img.shields.io/github/stars/EvolvingLMMs-Lab/LongVT?style=flat&logo=github&logoColor=white&label=Code&labelColor=24292f&color=57606a)](https://github.com/EvolvingLMMs-Lab/LongVT) |
| <strong>OmniRAG-Agent</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2602.03707">OmniRAG-Agent: Agentic Omnimodal Reasoning for Low-Resource Long Audio-Video Question Answering</a><br><sub>Yifan Zhu et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2602.03707) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L384) |
| <strong>SAGE</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2512.13874">Sage: Training smart any-horizon agents for long video reasoning with reinforcement learning</a><br><sub>Jitesh Jain et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2512.13874) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L207) |
| <strong>Video-MTR</strong><br>![ICML 2026](https://img.shields.io/badge/ICML-2026-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=UhPwL6LYOc">Video-MTR: Reinforced Multi-Turn Reasoning for Long Video Understanding</a><br><sub>Yuan Xie et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=UhPwL6LYOc) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L257) |
| <strong>VideoZoomer</strong><br>![ICLR 2026](https://img.shields.io/badge/ICLR-2026-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=ARHCFvgx6G">VideoZoomer: Reinforcement-Learned Temporal Focusing for Long Video Reasoning</a><br><sub>Yang Ding et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=ARHCFvgx6G) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L531) |
| <strong>VITAL</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2508.04416">Thinking with videos: Multimodal tool-augmented reinforcement learning for long video reasoning</a><br><sub>Haoji Zhang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2508.04416) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L215) |
| <strong>VSeek</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2607.02959">Incentivizing Vision Language Models to Search for Long Video Question Answering</a><br><sub>Harsh Goel et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2607.02959) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L377) |

<div align="right"><a href="#taxonomy">↑ Back to taxonomy</a></div>

</details>

<a id="programmatic"></a>

<details>
<summary><b>Programmatic Acquisition</b> &nbsp;<img src="https://img.shields.io/badge/2_papers-c0609f?style=flat" alt="2 papers">&nbsp; <sub><i>👆 click to expand</i></sub></summary>

Compose executable programs that probe video content with perception tools.

| Method | Paper | Links |
| :--- | :--- | :--- |
| <strong>HPP</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2606.21734">HPP: Hierarchical Programmatic Probing for Long Video Understanding by Decoupling Perception and Reasoning</a><br><sub>Awais Rauf et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2606.21734) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L564) |
| <strong>ViperGPT<sup>†</sup></strong><br>![ICCV 2023](https://img.shields.io/badge/ICCV-2023-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2303.08128">Vipergpt: Visual inference via python execution for reasoning</a><br><sub>Dídac Surís et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2303.08128) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L556)<br>[![Code, GitHub stars for cvlab-columbia/viper](https://img.shields.io/github/stars/cvlab-columbia/viper?style=flat&logo=github&logoColor=white&label=Code&labelColor=24292f&color=57606a)](https://github.com/cvlab-columbia/viper) |

<div align="right"><a href="#taxonomy">↑ Back to taxonomy</a></div>

</details>

<a id="memory-state"></a>

## Memory & State Representation

<img src="assets/header-memory-state.png" width="100%" alt="Stage 2: What should the agent remember?">

<div align="center">

[![Textual 6](https://img.shields.io/badge/Textual-6-b8921a?style=flat&labelColor=555)](#textual) [![Structured 14](https://img.shields.io/badge/Structured-14-b8921a?style=flat&labelColor=555)](#structured) [![Compact 6](https://img.shields.io/badge/Compact-6-b8921a?style=flat&labelColor=555)](#compact) [![Streaming 9](https://img.shields.io/badge/Streaming-9-b8921a?style=flat&labelColor=555)](#streaming)

</div>

<a id="textual"></a>

<details>
<summary><b>Textual Memory</b> &nbsp;<img src="https://img.shields.io/badge/6_papers-b8921a?style=flat" alt="6 papers">&nbsp; <sub><i>👆 click to expand</i></sub></summary>

Retain captions, textual summaries, and language-based accounts of past observations.

| Method | Paper | Links |
| :--- | :--- | :--- |
| <strong>MERIT</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2608.07663">Keep It Simple: Multi-Key Episodic Memory Retrieval for Ultra-Long Video Understanding</a><br><sub>Yeeun Choi et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2608.07663) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L411) |
| <strong>SiLVR<sup>†</sup></strong><br>![TMLR 2026](https://img.shields.io/badge/TMLR-2026-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=mQZbh9Zlbw">SiLVR: A Simple Language-based Video Reasoning Framework</a><br><sub>Ce Zhang et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=mQZbh9Zlbw) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L595) |
| <strong>DrVideo</strong><br>![CVPR 2025](https://img.shields.io/badge/CVPR-2025-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2406.12846">Drvideo: Document retrieval based long video understanding</a><br><sub>Ziyu Ma et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2406.12846) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L337)<br>[![Code, GitHub stars for Upper9527/DrVideo](https://img.shields.io/github/stars/Upper9527/DrVideo?style=flat&logo=github&logoColor=white&label=Code&labelColor=24292f&color=57606a)](https://github.com/Upper9527/DrVideo) |
| <strong>LangRepo<sup>†</sup></strong><br>![Findings of ACL 2025](https://img.shields.io/badge/Findings%20of%20ACL-2025-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2403.14622">Language repository for long video understanding</a><br><sub>Kumara Kahatapitiya et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2403.14622) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L578) |
| <strong>Mr. Video<sup>†</sup></strong><br>![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=7n2Kv5BUz2">MR. Video: MapReduce as an Effective Principle for Long Video Understanding</a><br><sub>Ziqi Pang et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=7n2Kv5BUz2) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L586) |
| <strong>LifelongMemory<sup>†</sup></strong><br>![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2312.05269">Lifelongmemory: Leveraging llms for answering queries in long-form egocentric videos</a><br><sub>Ying Wang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2312.05269) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L571) |

<div align="right"><a href="#taxonomy">↑ Back to taxonomy</a></div>

</details>

<a id="structured"></a>

<details>
<summary><b>Structured Memory</b> &nbsp;<img src="https://img.shields.io/badge/14_papers-b8921a?style=flat" alt="14 papers">&nbsp; <sub><i>👆 click to expand</i></sub></summary>

Organize evidence as events, entities, graphs, or other explicitly addressable structures.

| Method | Paper | Links |
| :--- | :--- | :--- |
| <strong>AVA</strong><br>![NSDI 2026](https://img.shields.io/badge/NSDI-2026-blue?style=flat&labelColor=555) | <a href="https://www.usenix.org/conference/nsdi26/presentation/yan">AVA: Towards Agentic Video Analytics with Vision Language Models</a><br><sub>Yuxuan Yan et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://www.usenix.org/conference/nsdi26/presentation/yan) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L672) |
| <strong>EGAgent</strong><br>![ACL 2026](https://img.shields.io/badge/ACL-2026-blue?style=flat&labelColor=555) | <a href="https://aclanthology.org/2026.acl-long.2161/">Agentic Very Long Video Understanding</a><br><sub>Aniket Rege et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://aclanthology.org/2026.acl-long.2161/) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L629) |
| <strong>EventMemAgent</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2602.15329">EventMemAgent: Hierarchical Event-Centric Memory for Online Video Understanding with Adaptive Tool Use</a><br><sub>Siwei Wen et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2602.15329) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L394) |
| <strong>MAGIC-Video</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2605.08271">Bridging Modalities, Spanning Time: Structured Memory for Ultra-Long Agentic Video Reasoning</a><br><sub>Jiazheng Li et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2605.08271) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L680) |
| <strong>MemDreamer</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2606.07512">MemDreamer: Decoupling Perception and Reasoning for Long Video Understanding via Hierarchical Graph Memory and Agentic Retrieval Mechanism</a><br><sub>Cong Chen et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2606.07512) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L690) |
| <strong>TCogMap<sup>†</sup></strong><br>![Agents in the Wild 2026](https://img.shields.io/badge/Agents%20in%20the%20Wild-2026-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=ZTnt0PzHnL">From Segments to Scenes: Temporal Understanding for Agentic Autonomous Driving via Vision-Language Models</a><br><sub>Kevin Cannons et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=ZTnt0PzHnL) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L663) |
| <strong>VideoLucy</strong><br>![NeurIPS 2026](https://img.shields.io/badge/NeurIPS-2026-blue?style=flat&labelColor=555) | Videolucy: Deep memory backtracking for long video understanding<br><sub>Jialong Zuo et al.</sub> | [Find&nbsp;paper](https://scholar.google.com/scholar?q=%22Videolucy%3A%20Deep%20memory%20backtracking%20for%20long%20video%20understanding%22) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L457) |
| <strong>VideoRAG<sup>†</sup></strong><br>![KDD 2026](https://img.shields.io/badge/KDD-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2502.01549">Videorag: Retrieval-augmented generation with extreme long-context videos</a><br><sub>Xubin Ren et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2502.01549) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L352)<br>[![Code, GitHub stars for HKUDS/VideoRAG](https://img.shields.io/github/stars/HKUDS/VideoRAG?style=flat&logo=github&logoColor=white&label=Code&labelColor=24292f&color=57606a)](https://github.com/HKUDS/VideoRAG) |
| <strong>WorldMM</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2512.02425">Worldmm: Dynamic multimodal memory agent for long video reasoning</a><br><sub>Woongyeong Yeo et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2512.02425) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L697) |
| <strong>Embodied VideoAgent</strong><br>![ICCV 2025](https://img.shields.io/badge/ICCV-2025-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2501.00358">Embodied videoagent: Persistent memory from egocentric videos and embodied sensors enables dynamic scene understanding</a><br><sub>Yue Fan et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2501.00358) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L654) |
| <strong>GCAgent</strong><br>![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2511.12027">Gcagent: Long-video understanding via schematic and narrative episodic memory</a><br><sub>Jeong Hun Yeo et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2511.12027) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L615) |
| <strong>GraphVideoAgent</strong><br>![ACM MM 2025](https://img.shields.io/badge/ACM%20MM-2025-blue?style=flat&labelColor=555) | <a href="https://doi.org/10.1145/3746027.3755537">GraphVideoAgent: Enhancing Long-form Video Understanding with Entity Relation Graphs</a><br><sub>Meng Chu et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://doi.org/10.1145/3746027.3755537) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L319) |
| <strong>Video-EM</strong><br>![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2508.09486">Video-EM: Event-Centric Episodic Memory for Long-Form Video Understanding</a><br><sub>Yun Wang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2508.09486) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L622) |
| <strong>DoraemonGPT</strong><br>![ICML 2024](https://img.shields.io/badge/ICML-2024-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=QMy2RLnxGN">DoraemonGPT: Toward Understanding Dynamic Scenes with Large Language Models (Exemplified as A Video Agent)</a><br><sub>Zongxin Yang et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=QMy2RLnxGN) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L606) |

<div align="right"><a href="#taxonomy">↑ Back to taxonomy</a></div>

</details>

<a id="compact"></a>

<details>
<summary><b>Compact Memory Representation</b> &nbsp;<img src="https://img.shields.io/badge/6_papers-b8921a?style=flat" alt="6 papers">&nbsp; <sub><i>👆 click to expand</i></sub></summary>

Maintain compact latent representations that reduce the cost of storing and revisiting video context.

| Method | Paper | Links |
| :--- | :--- | :--- |
| <strong>MemoryCard<sup>†</sup></strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2606.05917">MemoryCard: Topic-Aware Multi-Modal Clue Compression for Long-Video Question Answering</a><br><sub>Qing Yang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2606.05917) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L730) |
| <strong>MM-MEM</strong><br>![ACL 2026](https://img.shields.io/badge/ACL-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2603.01455">From verbatim to gist: Distilling pyramidal multimodal memory via semantic information bottleneck for long-horizon video agents</a><br><sub>Niu Lian et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2603.01455) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L476) |
| <strong>StreamMeCo<sup>†</sup></strong><br>![Findings of ACL 2026](https://img.shields.io/badge/Findings%20of%20ACL-2026-blue?style=flat&labelColor=555) | <a href="https://aclanthology.org/2026.findings-acl.647/">Streammeco: Long-term agent memory compression for efficient streaming video understanding</a><br><sub>Junxi Wang et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://aclanthology.org/2026.findings-acl.647/) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L722) |
| <strong>TASKER<sup>†</sup></strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2606.29445">Bridging VideoQA and Video-Guided Agentic Tasks via Generalized Keyframe Extraction</a><br><sub>Sunqi Fan et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2606.29445) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L740) |
| <strong>MA-LMM<sup>†</sup></strong><br>![CVPR 2024](https://img.shields.io/badge/CVPR-2024-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2404.05726">Ma-lmm: Memory-augmented large multimodal model for long-term video understanding</a><br><sub>Bo He et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2404.05726) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L713)<br>[![Code, GitHub stars for boheumd/MA-LMM](https://img.shields.io/github/stars/boheumd/MA-LMM?style=flat&logo=github&logoColor=white&label=Code&labelColor=24292f&color=57606a)](https://github.com/boheumd/MA-LMM) |
| <strong>MovieChat<sup>†</sup></strong><br>![CVPR 2024](https://img.shields.io/badge/CVPR-2024-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2307.16449">Moviechat: From dense token to sparse memory for long video understanding</a><br><sub>Enxin Song et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2307.16449) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L705) |

<div align="right"><a href="#taxonomy">↑ Back to taxonomy</a></div>

</details>

<a id="streaming"></a>

<details>
<summary><b>Streaming Memory Management</b> &nbsp;<img src="https://img.shields.io/badge/9_papers-b8921a?style=flat" alt="9 papers">&nbsp; <sub><i>👆 click to expand</i></sub></summary>

Update memory as new observations arrive and support reasoning over an evolving stream.

| Method | Paper | Links |
| :--- | :--- | :--- |
| <strong>Light-Omni</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2607.05511">Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory</a><br><sub>Chang Nie et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2607.05511) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L805) |
| <strong>StreamBridge<sup>†</sup></strong><br>![NeurIPS 2026](https://img.shields.io/badge/NeurIPS-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2505.05467">Streambridge: Turning your offline video large language model into a proactive streaming assistant</a><br><sub>Haibo Wang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2505.05467) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L765) |
| <strong>StreamingVLM<sup>†</sup></strong><br>![ICLR 2026](https://img.shields.io/badge/ICLR-2026-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=gVbPWbA97s">StreamingVLM: Real-Time Understanding for Infinite Video Streams</a><br><sub>Ruyi Xu et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=gVbPWbA97s) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L796) |
| <strong>StreamMeCo<sup>†</sup></strong><br>![Findings of ACL 2026](https://img.shields.io/badge/Findings%20of%20ACL-2026-blue?style=flat&labelColor=555) | <a href="https://aclanthology.org/2026.findings-acl.647/">Streammeco: Long-term agent memory compression for efficient streaming video understanding</a><br><sub>Junxi Wang et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://aclanthology.org/2026.findings-acl.647/) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L722) |
| <strong>TaYS</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2603.02872">Think-as-you-see: Streaming chain-of-thought reasoning for large vision-language models</a><br><sub>Jialiang Zhang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2603.02872) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L781) |
| <strong>ThinkStream<sup>†</sup></strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2603.12938">Thinking in streaming video</a><br><sub>Zikang Liu et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2603.12938) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L789) |
| <strong>VAM</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2605.16481">Visual Agentic Memory: Enabling Online Long Video Understanding via Online Indexing, Hierarchical Memory, and Agentic Retrieval</a><br><sub>Aiden Yiliu Li et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2605.16481) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L774) |
| <strong>Dispider<sup>†</sup></strong><br>![CVPR 2025](https://img.shields.io/badge/CVPR-2025-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2501.03218">Dispider: Enabling video llms with active real-time interaction via disentangled perception, decision, and reaction</a><br><sub>Rui Qian et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2501.03218) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L757)<br>[![Code, GitHub stars for Mark12Ding/Dispider](https://img.shields.io/github/stars/Mark12Ding/Dispider?style=flat&logo=github&logoColor=white&label=Code&labelColor=24292f&color=57606a)](https://github.com/Mark12Ding/Dispider) |
| <strong>StreamAgent</strong><br>![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2508.01875">Streamagent: Towards anticipatory agents for streaming video understanding</a><br><sub>Haolin Yang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2508.01875) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L750) |

<div align="right"><a href="#taxonomy">↑ Back to taxonomy</a></div>

</details>

<a id="control-planning"></a>

## Control & Planning

<img src="assets/header-control-planning.png" width="100%" alt="Stage 3: Which action should the agent take?">

<div align="center">

[![Tool use 8](https://img.shields.io/badge/Tool%20use-8-4a82c9?style=flat&labelColor=555)](#autonomous-tool-use) [![Multi-agent 14](https://img.shields.io/badge/Multi--agent-14-4a82c9?style=flat&labelColor=555)](#multi-agent) [![Learned control 8](https://img.shields.io/badge/Learned%20control-8-4a82c9?style=flat&labelColor=555)](#learned-control) [![Fixed workflow 6](https://img.shields.io/badge/Fixed%20workflow-6-4a82c9?style=flat&labelColor=555)](#fixed-workflow)

</div>

<a id="autonomous-tool-use"></a>

<details>
<summary><b>Autonomous Tool Use</b> &nbsp;<img src="https://img.shields.io/badge/8_papers-4a82c9?style=flat" alt="8 papers">&nbsp; <sub><i>👆 click to expand</i></sub></summary>

Let a controller choose and invoke tools as the evidence and task evolve.

| Method | Paper | Links |
| :--- | :--- | :--- |
| <strong>LensWalk</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2603.24558">LensWalk: Agentic video understanding by planning how you see in videos</a><br><sub>Keliang Li et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2603.24558) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L40) |
| <strong>LongShOTAgent</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2512.16978">A Benchmark for Omni-Modal Reasoning in Long Videos</a><br><sub>Mohammed Irfan Kurpath et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2512.16978) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L20) |
| <strong>M3-Agent</strong><br>![ICLR 2026](https://img.shields.io/badge/ICLR-2026-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=PMz29A7Muq">Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory</a><br><sub>Lin Long et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=PMz29A7Muq) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L11) |
| <strong>OmniAgent</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2512.23646">Active Perception Agent for Omnimodal Audio-Video Understanding</a><br><sub>Keda Tao et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2512.23646) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L48) |
| <strong>OmniGAIA</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2602.22897">OmniGAIA: Towards Native Omni-Modal AI Agents</a><br><sub>Xiaoxi Li et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2602.22897) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L58) |
| <strong>Video-BrowseComp</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2512.23044">Video-Browser: Towards Agentic Open-web Video Browsing</a><br><sub>Zhengyang Liang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2512.23044) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L30) |
| <strong>VideoThinker</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2601.15724">VideoThinker: Building Agentic VideoLLMs with LLM-Guided Tool Reasoning</a><br><sub>Chenglin Li et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2601.15724) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L68) |
| <strong>OmAgent</strong><br>![EMNLP 2024](https://img.shields.io/badge/EMNLP-2024-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2406.16620">Omagent: A multi-modal agent framework for complex video understanding with task divide-and-conquer</a><br><sub>Lu Zhang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2406.16620) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L3) |

<div align="right"><a href="#taxonomy">↑ Back to taxonomy</a></div>

</details>

<a id="multi-agent"></a>

<details>
<summary><b>Multi-Agent Control</b> &nbsp;<img src="https://img.shields.io/badge/14_papers-4a82c9?style=flat" alt="14 papers">&nbsp; <sub><i>👆 click to expand</i></sub></summary>

Distribute perception, reasoning, and coordination across collaborating agents.

| Method | Paper | Links |
| :--- | :--- | :--- |
| <strong>AffectSeek</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2605.05640">AffectSeek: Agentic Affective Understanding in Long Videos under Vague User Queries</a><br><sub>Zhen Zhang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2605.05640) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L145) |
| <strong>CADER</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2607.24582">CADER: Confidence-Aware Dynamic Evidence Reasoning for Long-Video Understanding</a><br><sub>Jinlong Yang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2607.24582) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L192) |
| <strong>COACH</strong><br>![LLM-MAS Workshop 2026](https://img.shields.io/badge/LLM--MAS%20Workshop-2026-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=PrJ80Pvii2">COACH: Collaborative Agents for Contextual Highlighting A Multi-Agent Framework for Sports Video Analysis</a><br><sub>Tsz-To Wong et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=PrJ80Pvii2) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L128) |
| <strong>HiCrew</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2604.21444">HiCrew: Hierarchical Reasoning for Long-Form Video Understanding via Question-Aware Multi-Agent Collaboration</a><br><sub>Yuehan Zhu et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2604.21444) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L155) |
| <strong>IMPACT-CYCLE</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2604.20136">IMPACT-CYCLE: A Contract-Based Multi-Agent System for Claim-Level Supervisory Correction of Long-Video Semantic Memory</a><br><sub>Weitong Kong et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2604.20136) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L165) |
| <strong>LongVideoAgent</strong><br>![ACL 2026](https://img.shields.io/badge/ACL-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2512.20618">Longvideoagent: Multi-agent reasoning with long videos</a><br><sub>Runtao Liu et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2512.20618) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L120) |
| <strong>ReAgent-V</strong><br>![NeurIPS 2026](https://img.shields.io/badge/NeurIPS-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2506.01300">Reagent-v: A reward-driven multi-agent framework for video understanding</a><br><sub>Yiyang Zhou et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2506.01300) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L111) |
| <strong>SVAgent</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | SVAgent: Storyline-guided Long Video Understanding via Cross-Modal Multi-Agent Collaboration<br><sub>Zhongyu Yang et al.</sub> | [Find&nbsp;paper](https://scholar.google.com/scholar?q=%22SVAgent%3A%20Storyline-guided%20Long%20Video%20Understanding%20via%20Cross-Modal%20Multi-Agent%20Collaboration%22) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L175) |
| <strong>Symphony</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2603.17307">Symphony: A Cognitively-Inspired Multi-Agent System for Long-Video Understanding</a><br><sub>Haiyang Yan et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2603.17307) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L103) |
| <strong>VideoChat-M1</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2511.19524">Videochat-m1: Collaborative policy planning for video understanding via multi-agent reinforcement learning</a><br><sub>Boyu Chen et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2511.19524) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L184) |
| <strong>VideoHV-Agent</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2603.04977">Think, Then Verify: A Hypothesis-Verification Multi-Agent Framework for Long Video Understanding</a><br><sub>Zheng Wang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2603.04977) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L137) |
| <strong>LVAgent</strong><br>![ICCV 2025](https://img.shields.io/badge/ICCV-2025-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2503.10200">Lvagent: Long video understanding by multi-round dynamical collaboration of mllm agents</a><br><sub>Boyu Chen et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2503.10200) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L86)<br>[![Code, GitHub stars for 64327069/LVAgent](https://img.shields.io/github/stars/64327069/LVAgent?style=flat&logo=github&logoColor=white&label=Code&labelColor=24292f&color=57606a)](https://github.com/64327069/LVAgent) |
| <strong>VideoMultiAgents</strong><br>![SEA Workshop 2025](https://img.shields.io/badge/SEA%20Workshop-2025-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=nBp1omOQ4P">A Multi-agent Reasoning Framework for Video Question Answering</a><br><sub>Abhi Kamboj et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=nBp1omOQ4P) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L94) |
| <strong>TraveLER</strong><br>![EMNLP 2024](https://img.shields.io/badge/EMNLP-2024-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2404.01476">TraveLER: A Modular Multi-LMM Agent Framework for Video Question-Answering</a><br><sub>Chuyi Shang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2404.01476) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L78) |

<div align="right"><a href="#taxonomy">↑ Back to taxonomy</a></div>

</details>

<a id="learned-control"></a>

<details>
<summary><b>Learned Control Policies</b> &nbsp;<img src="https://img.shields.io/badge/8_papers-4a82c9?style=flat" alt="8 papers">&nbsp; <sub><i>👆 click to expand</i></sub></summary>

Learn action selection and planning policies for long-horizon video reasoning.

| Method | Paper | Links |
| :--- | :--- | :--- |
| <strong>Ego-R1</strong><br>![TPAMI 2026](https://img.shields.io/badge/TPAMI-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2506.13654">Ego-R1: Agentic Chain-of-Tool-Thought for Ultra-Long Egocentric Video Reasoning</a><br><sub>Shulin Tian et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2506.13654) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L199) |
| <strong>EVA</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2603.22918">EVA: Efficient Reinforcement Learning for End-to-End Video Agent</a><br><sub>Yaolun Zhang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2603.22918) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L232) |
| <strong>LongVideo-R1</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2602.20913">Longvideo-r1: Smart navigation for low-cost long video understanding</a><br><sub>Jihao Qiu et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2602.20913) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L240) |
| <strong>SAGE</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2512.13874">Sage: Training smart any-horizon agents for long video reasoning with reinforcement learning</a><br><sub>Jitesh Jain et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2512.13874) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L207) |
| <strong>Video-MTR</strong><br>![ICML 2026](https://img.shields.io/badge/ICML-2026-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=UhPwL6LYOc">Video-MTR: Reinforced Multi-Turn Reasoning for Long Video Understanding</a><br><sub>Yuan Xie et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=UhPwL6LYOc) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L257) |
| <strong>VideoBrain</strong><br>![ICML 2026](https://img.shields.io/badge/ICML-2026-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=1TXn0PeBZJ">VideoBrain: Learning Adaptive Frame Sampling for Long Video Understanding</a><br><sub>Junbo Zou et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=1TXn0PeBZJ) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L223) |
| <strong>VideoTemp-o3</strong><br>![ICML 2026](https://img.shields.io/badge/ICML-2026-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=DlKdI669OM">VideoTemp-o3: Harmonizing Temporal Grounding and Video Understanding in Agentic Thinking-with-Videos</a><br><sub>Wenqi Liu et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=DlKdI669OM) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L248) |
| <strong>VITAL</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2508.04416">Thinking with videos: Multimodal tool-augmented reinforcement learning for long video reasoning</a><br><sub>Haoji Zhang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2508.04416) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L215) |

<div align="right"><a href="#taxonomy">↑ Back to taxonomy</a></div>

</details>

<a id="fixed-workflow"></a>

<details>
<summary><b>Fixed Workflows</b> &nbsp;<img src="https://img.shields.io/badge/6_papers-4a82c9?style=flat" alt="6 papers">&nbsp; <sub><i>👆 click to expand</i></sub></summary>

Coordinate evidence processing through a predefined sequence of stages.

| Method | Paper | Links |
| :--- | :--- | :--- |
| <strong>SVAgent</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | SVAgent: Storyline-guided Long Video Understanding via Cross-Modal Multi-Agent Collaboration<br><sub>Zhongyu Yang et al.</sub> | [Find&nbsp;paper](https://scholar.google.com/scholar?q=%22SVAgent%3A%20Storyline-guided%20Long%20Video%20Understanding%20via%20Cross-Modal%20Multi-Agent%20Collaboration%22) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L175) |
| <strong>VideoChat-A1</strong><br>![AAAI 2026](https://img.shields.io/badge/AAAI-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2506.06097">Videochat-a1: Thinking with long videos by chain-of-shot reasoning</a><br><sub>Zikang Wang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2506.06097) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L299) |
| <strong>VCA</strong><br>![ICCV 2025](https://img.shields.io/badge/ICCV-2025-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2412.10471">Vca: Video curious agent for long video understanding</a><br><sub>Zeyuan Yang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2412.10471) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L291) |
| <strong>MoReVQA<sup>†</sup></strong><br>![CVPR 2024](https://img.shields.io/badge/CVPR-2024-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2404.06511">Morevqa: Exploring modular reasoning models for video question answering</a><br><sub>Juhong Min et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2404.06511) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L275) |
| <strong>VideoAgent</strong><br>![ECCV 2024](https://img.shields.io/badge/ECCV-2024-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2403.10517">Videoagent: Long-form video understanding with large language model as agent</a><br><sub>Xiaohan Wang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2403.10517) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L266)<br>[![Code, GitHub stars for wxh1996/VideoAgent](https://img.shields.io/github/stars/wxh1996/VideoAgent?style=flat&logo=github&logoColor=white&label=Code&labelColor=24292f&color=57606a)](https://github.com/wxh1996/VideoAgent) |
| <strong>VideoINSTA</strong><br>![Findings of EMNLP 2024](https://img.shields.io/badge/Findings%20of%20EMNLP-2024-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2409.20365">Videoinsta: Zero-shot long video understanding via informative spatial-temporal reasoning with llms</a><br><sub>Ruotong Liao et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2409.20365) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L283) |

<div align="right"><a href="#taxonomy">↑ Back to taxonomy</a></div>

</details>

<a id="verification-aggregation"></a>

## Verification & Aggregation

<img src="assets/header-verification-aggregation.png" width="100%" alt="Stage 4: Is the evidence sufficient to answer?">

<div align="center">

[![Consensus 4](https://img.shields.io/badge/Consensus-4-4a9a62?style=flat&labelColor=555)](#consensus) [![Reflection 10](https://img.shields.io/badge/Reflection-10-4a9a62?style=flat&labelColor=555)](#reflection) [![Confidence 3](https://img.shields.io/badge/Confidence-3-4a9a62?style=flat&labelColor=555)](#confidence) [![Alignment 6](https://img.shields.io/badge/Alignment-6-4a9a62?style=flat&labelColor=555)](#evidence-alignment)

</div>

<a id="consensus"></a>

<details>
<summary><b>Consensus / Self-Consistency</b> &nbsp;<img src="https://img.shields.io/badge/4_papers-4a9a62?style=flat" alt="4 papers">&nbsp; <sub><i>👆 click to expand</i></sub></summary>

Compare candidate answers or reasoning paths to assess agreement.

| Method | Paper | Links |
| :--- | :--- | :--- |
| <strong>A4VL</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=N3kgr2kNGt">A Multi-Agent Perception-Action Alliance for Efficient Long Video Reasoning</a><br><sub>Yichang Xu et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=N3kgr2kNGt) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L815) |
| <strong>TRACE</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2608.22516">TRACE: Temporal Retrieval with Anchored and Convergent Evidence for Long-Horizon Video Understanding</a><br><sub>Pengyiang Liu et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2608.22516) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L418) |
| <strong>LVAgent</strong><br>![ICCV 2025](https://img.shields.io/badge/ICCV-2025-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2503.10200">Lvagent: Long video understanding by multi-round dynamical collaboration of mllm agents</a><br><sub>Boyu Chen et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2503.10200) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L86)<br>[![Code, GitHub stars for 64327069/LVAgent](https://img.shields.io/github/stars/64327069/LVAgent?style=flat&logo=github&logoColor=white&label=Code&labelColor=24292f&color=57606a)](https://github.com/64327069/LVAgent) |
| <strong>LifelongMemory<sup>†</sup></strong><br>![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2312.05269">Lifelongmemory: Leveraging llms for answering queries in long-form egocentric videos</a><br><sub>Ying Wang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2312.05269) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L571) |

<div align="right"><a href="#taxonomy">↑ Back to taxonomy</a></div>

</details>

<a id="reflection"></a>

<details>
<summary><b>Reflection / Refine</b> &nbsp;<img src="https://img.shields.io/badge/10_papers-4a9a62?style=flat" alt="10 papers">&nbsp; <sub><i>👆 click to expand</i></sub></summary>

Revisit evidence and revise an answer or plan through feedback.

| Method | Paper | Links |
| :--- | :--- | :--- |
| <strong>A.I.R</strong><br>![ICLR 2026](https://img.shields.io/badge/ICLR-2026-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=SZVpOKw0YD">A.I.R.: Enabling Adaptive, Iterative, and Reasoning-based Frame Selection For Video Question Answering</a><br><sub>Yuanhao Zou et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=SZVpOKw0YD) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L879) |
| <strong>AVP</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2512.05774">Active video perception: Iterative evidence seeking for agentic long video understanding</a><br><sub>Ziyang Wang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2512.05774) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L871) |
| <strong>CRAFT</strong><br>![MAGMaR Workshop 2026](https://img.shields.io/badge/MAGMaR%20Workshop-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2605.19075">Craft: Critic-refined adaptive key-frame targeting for multimodal video question answering</a><br><sub>Mahesh Bhosale et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2605.19075) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L863) |
| <strong>ProVCA</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2604.02891">Progressive Video Condensation with MLLM Agent for Long-form Video Understanding</a><br><sub>Yufei Yin et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2604.02891) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L888) |
| <strong>Reflect-R1</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2606.27922">Reflect-R1: Evidence-Driven Reflection for Self-Correction in Long Video Understanding</a><br><sub>Shuimu Chen et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2606.27922) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L847) |
| <strong>TimeSearch-R</strong><br>![ICLR 2026](https://img.shields.io/badge/ICLR-2026-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=gqb1hvuGcj">TimeSearch-R: Adaptive Temporal Search for Long-Form Video Understanding via Self-Verification Reinforcement Learning</a><br><sub>Junwen Pan et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=gqb1hvuGcj) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L854) |
| <strong>ZoomV</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2504.01407">ZoomV: Temporal Zoom-in for Efficient Long Video Understanding</a><br><sub>Yuan Zhang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2504.01407) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L466) |
| <strong>MASR</strong><br>![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2504.17213">MASR: Self-Reflective Reasoning through Multimodal Hierarchical Attention Focusing for Agent-based Video Understanding</a><br><sub>Shiwen Cao et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2504.17213) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L840) |
| <strong>AVUA</strong><br>![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2410.20252">Adaptive video understanding agent: Enhancing efficiency with dynamic frame sampling and feedback-driven reasoning</a><br><sub>Sullam Jeoung et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2410.20252) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L833) |
| <strong>Reflexion<sup>†</sup></strong><br>![NeurIPS 2023](https://img.shields.io/badge/NeurIPS-2023-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2303.11366">Reflexion: Language agents with verbal reinforcement learning</a><br><sub>Noah Shinn et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2303.11366) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L824) |

<div align="right"><a href="#taxonomy">↑ Back to taxonomy</a></div>

</details>

<a id="confidence"></a>

<details>
<summary><b>Confidence / Uncertainty</b> &nbsp;<img src="https://img.shields.io/badge/3_papers-4a9a62?style=flat" alt="3 papers">&nbsp; <sub><i>👆 click to expand</i></sub></summary>

Use uncertainty estimates to guide reasoning and evidence seeking.

| Method | Paper | Links |
| :--- | :--- | :--- |
| <strong>CADER</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2607.24582">CADER: Confidence-Aware Dynamic Evidence Reasoning for Long-Video Understanding</a><br><sub>Jinlong Yang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2607.24582) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L192) |
| <strong>FALCONEye</strong><br>![WACV 2026](https://img.shields.io/badge/WACV-2026-blue?style=flat&labelColor=555) | FALCONEye: Finding Answers and Localizing Content in ONE-hour-long videos with multi-modal LLMs<br><sub>Carlos Plou et al.</sub> | [Find&nbsp;paper](https://scholar.google.com/scholar?q=%22FALCONEye%3A%20Finding%20Answers%20and%20Localizing%20Content%20in%20ONE-hour-long%20videos%20with%20multi-modal%20LLMs%22) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L425) |
| <strong>VideoAgent2</strong><br>![SEA Workshop 2025](https://img.shields.io/badge/SEA%20Workshop-2025-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=MD8QyIZIoE">VideoAgent2: Enhancing the LLM-Based Agent System for Long-Form Video Understanding by Uncertainty-Aware CoT</a><br><sub>Zhuo Zhi et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=MD8QyIZIoE) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L895) |

<div align="right"><a href="#taxonomy">↑ Back to taxonomy</a></div>

</details>

<a id="evidence-alignment"></a>

<details>
<summary><b>Evidence Alignment & Adjudication</b> &nbsp;<img src="https://img.shields.io/badge/6_papers-4a9a62?style=flat" alt="6 papers">&nbsp; <sub><i>👆 click to expand</i></sub></summary>

Check claims against evidence and reconcile conflicting observations or agent outputs.

| Method | Paper | Links |
| :--- | :--- | :--- |
| <strong>TimeProVe</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2606.20561">TimeProVe: Propose, then Verify for Efficient Long Video Temporal Reasoning in Activities of Daily Living</a><br><sub>Arkaprava Sinha et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2606.20561) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L920) |
| <strong>VESTA</strong><br>![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2608.31005">From Intent to Evidence: Policy-Steered Multi-Strategy Retrieval for Long-Video Agents</a><br><sub>Can Zhang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2608.31005) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L434) |
| <strong>VideoHV-Agent</strong><br>![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2603.04977">Think, Then Verify: A Hypothesis-Verification Multi-Agent Framework for Long Video Understanding</a><br><sub>Zheng Wang et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2603.04977) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L137) |
| <strong>VideoSEAL</strong><br>![ICML 2026](https://img.shields.io/badge/ICML-2026-blue?style=flat&labelColor=555) | <a href="https://openreview.net/forum?id=RsPequeaiZ">VideoSEAL: Mitigating Evidence Misalignment in Agentic Long Video Understanding by Decoupling Answer Authority</a><br><sub>Chenhao Qiu et al.</sub> | [![Paper](https://img.shields.io/badge/Paper-blue?style=flat)](https://openreview.net/forum?id=RsPequeaiZ) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L904) |
| <strong>CogniGPT</strong><br>![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2509.24943">Perceive, Reflect and Understand Long Video: Progressive Multi-Granular Clue Exploration with Interactive Agents</a><br><sub>Jiahua Li et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2509.24943) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L913) |
| <strong>LVAgent</strong><br>![ICCV 2025](https://img.shields.io/badge/ICCV-2025-blue?style=flat&labelColor=555) | <a href="https://arxiv.org/abs/2503.10200">Lvagent: Long video understanding by multi-round dynamical collaboration of mllm agents</a><br><sub>Boyu Chen et al.</sub> | [![arXiv](https://img.shields.io/badge/arXiv-red?style=flat)](https://arxiv.org/abs/2503.10200) [![BibTeX](https://img.shields.io/badge/BibTeX-lightgrey?style=flat)](references.bib#L86)<br>[![Code, GitHub stars for 64327069/LVAgent](https://img.shields.io/github/stars/64327069/LVAgent?style=flat&logo=github&logoColor=white&label=Code&labelColor=24292f&color=57606a)](https://github.com/64327069/LVAgent) |

<div align="right"><a href="#taxonomy">↑ Back to taxonomy</a></div>

</details>

<!-- taxonomy:end -->

## Collection & Bibliography

The collection maps the manuscript's `sections/taxonomy.tex` to `custom.bib` using exact citation keys. Bibliographic years and venues are retained from that source; a linked preprint may have an earlier release date than the listed publication year.

| Resource | What you will find |
| :--- | :--- |
| [Taxonomy tables](#taxonomy) | Every paper, grouped by stage and mechanism (this page) |
| [Paper index](papers/index.md) | A deduplicated chronological index with links back to each taxonomy branch |
| [Recent additions](papers/recent-additions.md) | New methods awaiting taxonomy integration, with provisional categories |
| [BibTeX bibliography](references.bib) | All taxonomy citation records, with their original keys |
| [Verified code links](data/code-links.json) | Official repositories and primary sources used to confirm each link |
| [Structured catalog](data/catalog.json) | Titles, authors, venues, citation aliases, and all category assignments |
| [Data notes](docs/DATA_NOTES.md) | Provenance, duplicate handling, link sources, and metadata conventions |

### Badge Colors

| Badge | Meaning |
| :--- | :--- |
| ![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555) | `red` for arXiv papers |
| ![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555) | `blue` for conference and journal papers |
| ![Code](https://img.shields.io/badge/Code-24292f?style=flat&logo=github&logoColor=white) | `dark` for official code repositories, with a live star count |
| ![Acquisition](https://img.shields.io/badge/Acquisition-c0609f?style=flat) ![Memory](https://img.shields.io/badge/Memory-b8921a?style=flat) ![Control](https://img.shields.io/badge/Control-4a82c9?style=flat) ![Verification](https://img.shields.io/badge/Verification-4a9a62?style=flat) | one color per stage, taken from the survey's pipeline figure: pink, gold, blue, green |

Venue badges separate the **venue** (dark gray) from the **year**, following the bibliography. A conference or journal paper may also link to its red **arXiv** preprint. **Find paper** opens a title search when no direct identifier is available. Star counts are served by Shields.io and may refresh with a caching delay. Full author lists are available in the bibliography and structured catalog.

## Contributing

> [!IMPORTANT]
> Relevant papers, metadata corrections, and taxonomy suggestions are welcome. Please include a primary publication link and explain how the work fits a stage of the agent loop.

**[Read the contribution guide](CONTRIBUTING.md)** · **[Suggest a paper](https://github.com/PhuTran1005/Awesome-Long-Video-Agent-Papers/issues/new?template=paper.yml)** · **[Report a correction](https://github.com/PhuTran1005/Awesome-Long-Video-Agent-Papers/issues/new?template=correction.yml)**

## Citation

The survey's public paper link and formal citation will be added when available. Until then, please cite the individual papers using [references.bib](references.bib).

## Acknowledgments & License

The repository layout is inspired by [Awesome Multimodal Token Compression](https://github.com/cokeshao/Awesome-Multimodal-Token-Compression). We thank the authors whose research makes this collection possible.

Repository materials are provided under the existing [Apache 2.0 license](LICENSE). Linked papers and external resources remain subject to their respective licenses.

## Star History

<p align="center">
  <a href="https://star-history.com/#PhuTran1005/Awesome-Long-Video-Agent-Papers&Date"><img src="https://api.star-history.com/svg?repos=PhuTran1005/Awesome-Long-Video-Agent-Papers&type=Date" alt="Star history chart" width="600"></a>
</p>

<p align="center"><sub>Explore the evidence. Follow the reasoning. Keep the sources close.</sub></p>
