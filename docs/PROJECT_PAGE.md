# Survey project page

The `project-page` branch contains the research website for **Beyond Passive Watching: A Comprehensive Survey of Agentic Systems for Long-Form Video Understanding**.

The site is static HTML, CSS, and JavaScript. It needs no npm packages, API keys, external fonts, or backend. The manuscript is in preparation; a public paper URL, author list, affiliations, and formal survey citation should be added only when confirmed.

## Preview locally

From the repository root:

```bash
python -X utf8 scripts/build_project_page.py
python -m http.server 8000 --bind 127.0.0.1
```

Open [the local preview](http://127.0.0.1:8000). You can also open [index.html](../index.html) directly: the catalog is embedded, so search and filters do not require fetching JSON. Clipboard behavior on file URLs depends on the browser; the citation dialog always allows manual copying.

## Content and interactions

- Research overview, original manuscript teaser, and expandable taxonomy figure.
- Interactive explanations of acquisition, memory, planning, and verification.
- Four keyboard-accessible taxonomy tabs linking sixteen mechanisms to the explorer.
- Search across method, title, authors, venue, and mechanism. Multiple search terms are combined.
- Combined stage, mechanism, bibliographic year, core/enabling scope, and verified-code filters.
- Year/name sorting, incremental loading, and shareable query-string filters.
- Individual original BibTeX entries with copy support, and a full bibliography download.
- Catalog-derived stage counts and year chart; overlapping memberships never inflate the unique-paper total.
- Responsive layouts, reduced-motion support, accessible dialogs, and a complete paper list without JavaScript.

## Edit and rebuild

| File | Purpose |
| --- | --- |
| [index.template.html](../project-page/index.template.html) | Page copy, structure, and metadata |
| [styles.css](../project-page/styles.css) | Visual design and responsive layouts |
| [app.js](../project-page/app.js) | Explorer, taxonomy, dialogs, and agent-loop interaction |
| [build_project_page.py](../scripts/build_project_page.py) | Generates HTML and packages the static site |
| [catalog.json](../data/catalog.json) | Source paper metadata and taxonomy membership |
| [link-overrides.json](../data/link-overrides.json) | Verified publication-link corrections |
| [code-links.json](../data/code-links.json) | Verified official repositories |
| [references.bib](../references.bib) | Original bibliographic entries |

Edit the template, not the generated root `index.html`. Rebuild after changing content or catalog data:

```bash
python -X utf8 scripts/build_project_page.py
python -X utf8 scripts/catalog.py --check
python -X utf8 scripts/build_project_page.py --check
node --check project-page/app.js
```

The UTF-8 flag supports Windows systems whose default encoding differs from UTF-8. If catalog metadata changes, regenerate the Markdown catalog using the existing contribution workflow before running checks. Stage definitions come from `scripts/catalog.py`; stage artwork and colors retain the existing survey identity.

The builder checks catalog/bibliography coverage, paper IDs, categories, HTTPS publication/code links, duplicate HTML IDs, image alt attributes, and local assets/anchors. `--check` also detects stale generated HTML. It does not test continued availability of external sites.

## GitHub Pages

The [Project page workflow](../.github/workflows/project-page.yml) builds and deploys pushes to `project-page`. Pull requests run checks and package the site without deployment. The workflow publishes only the packaged website, not the whole repository.

The project page is hosted at **[phutran1005.github.io/Awesome-Long-Video-Agent-Papers/](https://phutran1005.github.io/Awesome-Long-Video-Agent-Papers/)**, alongside the [personal homepage](https://phutran1005.github.io/).

Repository Pages uses **GitHub Actions**. The `github-pages` environment allows deployment from `project-page`. After changing the site, rebuild and commit the generated HTML, then push the branch:

```bash
python -X utf8 scripts/build_project_page.py
python -X utf8 scripts/build_project_page.py --check
git push origin project-page
```

Follow the deployment in [GitHub Actions](https://github.com/PhuTran1005/Awesome-Long-Video-Agent-Papers/actions). The workflow runs automatically on pushes; the default `main` branch remains the paper collection. GitHub's [custom Pages workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) describes the hosting configuration.

For another static host:

```bash
python -X utf8 scripts/build_project_page.py --output dist
```

Upload the contents of `dist/`. All asset paths are relative and support a GitHub Pages repository subpath. The Open Graph image uses this repository's expected Pages URL; update it in the template if hosting elsewhere.

## Design and attribution

The academic project-page progression takes inspiration from [LVOmniBench](https://kd-tao.github.io/LVOmniBench/): a clear research identity, direct resources, explanatory figures, and a browseable research collection. The layout, typography, styling, diagrams, and explorer implementation here are original. No source code, text, or artwork was copied from that site. Survey figures and four stage icons are the existing repository assets. The decorative video ribbon is an illustration, not dataset footage.

Repository license: [Apache 2.0](../LICENSE). Metadata scope and provenance: [data notes](DATA_NOTES.md).
