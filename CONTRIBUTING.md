# Contributing

Thank you for helping maintain this collection. Contributions should be accurate, easy to verify, and consistent with the survey's scope.

## Suggest a Paper

Open a [paper suggestion](https://github.com/PhuTran1005/Awesome-Long-Video-Agent-Papers/issues/new?template=paper.yml) with the title, authors, publication link, BibTeX, and proposed taxonomy branch. Explain which earlier observation affects a later evidence-access decision. For an agent-enabling baseline or foundational method, explain that role explicitly.

Check the [taxonomy index](papers/index.md) and [recent additions](papers/recent-additions.md) first. A preprint and its conference version normally belong to one paper entry. Methods may belong to multiple branches when the taxonomy supports those assignments.

## Add a Recent Method

Methods that are not yet part of the manuscript taxonomy belong in [Recent Additions](papers/recent-additions.md). A finalized taxonomy assignment is not required.

Edit that page directly and add a row to the **Latest Methods** table with the release date, method name and full title, a concise contribution, a suggested stage (or **To be determined**), and primary publication links. Use the date conventions on that page and order entries newest first. Remove the empty-state sentence when adding the first method. Include BibTeX in the issue or pull request.

This manually maintained page survives catalog rebuilds and manuscript imports. Add pending methods here without changing the taxonomy catalog or its bibliography. Once a method is integrated into the manuscript, update the generated catalog and remove its pending row.

Run the existing consistency check before submitting:

```bash
python3 scripts/catalog.py --check
```

## Update the Catalog

The repository requires **Python 3.10 or newer**, with no third-party dependencies.

1. Edit `data/catalog.json` and add or correct the corresponding record in `references.bib`. Keep the original citation key when updating an existing paper.
2. Use an arXiv, DOI, publisher, or official proceedings URL. Preserve the bibliographic publication year and distinguish it from the preprint year.
3. Add independently checked publication links to `data/link-overrides.json`, including the primary source used to verify the match.
4. Rebuild the paper pages and README counts:

   ```bash
   python3 scripts/catalog.py
   ```

5. Check the generated content and local links:

   ```bash
   python3 scripts/catalog.py --check
   ```

6. Open a pull request explaining the change and its source.

The taxonomy tables in `README.md` (between the `taxonomy:start` / `taxonomy:end` markers) and `papers/index.md` are generated; `papers/recent-additions.md` is maintained manually. For generated pages, update the source data rather than editing the rendered pages directly. Use English throughout the repository.

## Badge Style

Follow the [badge colors](README.md#badge-colors) throughout the collection. The generated catalogs apply badges automatically. For recent additions, use the following Markdown, replacing example destinations with verified URLs:

```markdown
[![arXiv 2026](https://img.shields.io/badge/arXiv-2026-red?style=flat&labelColor=555)](https://arxiv.org/abs/ARXIV_ID)
[![CVPR 2026](https://img.shields.io/badge/CVPR-2026-blue?style=flat&labelColor=555)](https://example.org/paper)
[![Code](https://img.shields.io/github/stars/OWNER/REPOSITORY?style=flat&logo=github&logoColor=white&label=Code&labelColor=24292f&color=57606a)](https://github.com/OWNER/REPOSITORY)
[![Evidence Acquisition](https://img.shields.io/badge/Evidence%20Acquisition-c0609f?style=flat)](README.md#evidence-acquisition)
[![Retrieval](https://img.shields.io/badge/Retrieval-c0609f?style=flat)](README.md#retrieval-based)
```

The relative destinations above are written from the repository root. When adding a row to `papers/recent-additions.md`, prefix them with `../`. Publication colors reflect the bibliographic venue; a published paper may also have a red arXiv link. Keep text labels descriptive so readers do not have to rely on color alone.

For a taxonomy entry with a verified official GitHub repository, add its paper ID to [data/code-links.json](data/code-links.json), with `url` for the repository and `source` for the primary page confirming the paper-to-code match. These links survive manuscript re-imports. The renderer automatically adds the Code badge with a live star count. Existing inline `code_url` fields are also supported; the dedicated code-link map takes precedence.

Use `style=flat` for badges; the Code badge combines a dark `Code` label with the live star count. Publication badges use `VENUE-YEAR-COLOR` with `labelColor=555` for the venue segment. Omit stars when no verified GitHub repository is available; do not hard-code a star count.

See the official [static badge](https://shields.io/badges/static-badge) and [GitHub stars](https://shields.io/badges/git-hub-repo-stars) documentation for supported options.

## Regenerate the Artwork

The README banner and stage cards are rendered from `data/catalog.json` by `scripts/artwork.py` (requires Google Chrome or Chromium and Pillow). Rerun it after the catalog changes so the counts stay in sync:

```bash
python3 scripts/artwork.py
python3 scripts/artwork.py --survey /path/to/survey   # teaser panel (a) and publication chart
```

`assets/taxonomy.png` is exported separately from the appendix figure of the compiled manuscript.

## Synchronize with the Manuscript

Maintainers can regenerate the source catalog from the survey:

```bash
python3 scripts/catalog.py --import-survey /path/to/survey
python3 scripts/catalog.py --check
```

The survey directory must contain `sections/taxonomy.tex` and `custom.bib`. This replaces the imported catalog and bibliography; review the diff to preserve any repository-only additions. Publication-link overrides and verified code links survive re-imports. If the taxonomy structure changes, update the stage definitions in `scripts/catalog.py` first.

## Corrections

For incorrect titles, broken links, duplicate records, or category assignments, open a [metadata correction](https://github.com/PhuTran1005/Awesome-Long-Video-Agent-Papers/issues/new?template=correction.yml). Include the affected citation key and a primary source supporting the correction.

Keep discussion focused on the research and treat contributors respectfully.
