# Catalog Data Notes

[← Overview](../README.md) · [Structured catalog](../data/catalog.json) · [BibTeX](../references.bib)

## Provenance

The initial collection is derived from the supplied manuscript's `sections/taxonomy.tex` and `custom.bib`. The taxonomy determines membership; the bibliography provides titles, authors, venues, and years. SHA-256 hashes in `data/catalog.json` identify the exact imported source snapshots.

The source taxonomy contains **102 distinct active citation keys**. These resolve to **101 unique papers** across four stages and sixteen mechanisms. Commented-out citations are excluded. Cross-category appearances are preserved without increasing the unique-paper count.

Only references cited by the taxonomy are included in `references.bib`; unrelated entries and template references from the source bibliography are excluded. The teaser is copied from the supplied manuscript assets.

## Identity and Aliases

The two Video-EM records, `wang2025video` and `wang2025episodic`, share arXiv identifier **2508.09486**. They appear as one catalog entry, with both citation keys retained in the bibliography. The displayed title uses the first active taxonomy reference.

Method names follow the taxonomy even when the full paper title uses a different name. In particular, **Video-BrowseComp** is the taxonomy label for the record `liang2026videobrowseragenticopenwebvideo`. The complete bibliographic title remains visible beside it.

## Links and Publication Metadata

Direct URLs are taken from bibliography URL fields, DOI fields, and complete arXiv identifiers. Additional publication links are recorded in [link-overrides.json](../data/link-overrides.json), with their primary verification sources.

The structured catalog retains the original imported link; overrides are applied when rendering the Markdown pages. Consumers should merge the override map by paper ID to use the enriched links.

A **Paper** link identifies a publication or preprint. **Find paper** is a clearly labeled title search used only when a direct identifier is missing. Code repositories are not inferred from method names.

Publication years and venues follow the supplied bibliography. They have **not** undergone a full independent venue audit. For example, some supplied records list a 2026 bibliographic year for NeurIPS volume 38; the collection preserves those records rather than silently changing the survey's bibliography. Preprint release dates may also precede publication years.

The paper tables use abbreviated venue names and the first author for readability. Full metadata is available in the JSON and BibTeX files. Display normalization removes LaTeX case-protection braces and converts common accents; original BibTeX entries remain intact.

## Scope and Interpretation

The taxonomy includes agentic systems alongside selected agent-enabling baselines and foundational methods. Category membership describes a methodological role; it does not establish that every listed method independently meets the survey's behavioral definition of agency.

This is a curated snapshot of the survey taxonomy, not a claim of exhaustive coverage or a performance ranking. The survey is in preparation; no public manuscript URL, author list, acceptance claim, or formal survey citation is supplied here.

## Recent Additions

[Recent Additions](../papers/recent-additions.md) is a manually maintained list for methods awaiting integration into the manuscript taxonomy. Suggested stages are provisional. These entries do not affect the imported catalog, exported bibliography, or taxonomy counts.

Catalog rebuilds and manuscript imports preserve this page. Once a method is integrated into the taxonomy, its pending row is removed to avoid duplicate listings.

## Maintenance

See [CONTRIBUTING.md](../CONTRIBUTING.md) for import, rebuild, and validation commands. Automated checks cover citation-key coverage, duplicate assignments, category validity, deterministic page generation, and local file and anchor links. They do not guarantee continued availability of external websites.
