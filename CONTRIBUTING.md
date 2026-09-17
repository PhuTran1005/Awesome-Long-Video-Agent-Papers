# Contributing

Thank you for helping maintain this collection. Contributions should be accurate, easy to verify, and consistent with the survey's scope.

## Suggest a Paper

Open a [paper suggestion](https://github.com/PhuTran1005/Awesome-Long-Video-Agent-Papers/issues/new?template=paper.yml) with the title, authors, publication link, BibTeX, and proposed taxonomy branch. Explain which earlier observation affects a later evidence-access decision. For an agent-enabling baseline or foundational method, explain that role explicitly.

Check the [full index](papers/index.md) first. A preprint and its conference version normally belong to one paper entry. Methods may belong to multiple branches when the taxonomy supports those assignments.

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

The five files in `papers/` are generated. Update their source data rather than editing those pages directly. Use English throughout the repository.

## Synchronize with the Manuscript

Maintainers can regenerate the source catalog from the survey:

```bash
python3 scripts/catalog.py --import-survey /path/to/survey
python3 scripts/catalog.py --check
```

The survey directory must contain `sections/taxonomy.tex`, `custom.bib`, and `files/survey_teaser.png`. This replaces the imported catalog and bibliography and copies the teaser; review the diff to preserve any repository-only additions. Link overrides survive re-imports. If the taxonomy structure changes, update the stage definitions in `scripts/catalog.py` first.

## Corrections

For incorrect titles, broken links, duplicate records, or category assignments, open a [metadata correction](https://github.com/PhuTran1005/Awesome-Long-Video-Agent-Papers/issues/new?template=correction.yml). Include the affected citation key and a primary source supporting the correction.

Keep discussion focused on the research and treat contributors respectfully.
