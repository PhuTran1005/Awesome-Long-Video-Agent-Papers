#!/usr/bin/env python3
"""Import the survey bibliography and render the GitHub paper catalogs (stdlib only)."""

import argparse
import hashlib
import html
import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

from theme import PALETTE, SHORT

ROOT = Path(__file__).resolve().parents[1]
STAGES = [
    ("evidence-acquisition", "Evidence Acquisition", "Where should the agent look next?", [
        ("retrieval-based", "Retrieval-Based Acquisition", "Retrieve relevant moments, documents, or multimodal evidence in response to a query.", "sec:acq_retrieval"),
        ("hierarchical", "Hierarchical Acquisition", "Navigate from coarse summaries to finer temporal or spatial evidence.", "sec:acq_hierarchical"),
        ("learned-acquisition", "Learned Acquisition Policies", "Learn when, where, or at what granularity to acquire the next observation.", "sec:acq_learned"),
        ("programmatic", "Programmatic Acquisition", "Compose executable programs that probe video content with perception tools.", "sec:acq_programmatic"),
    ]),
    ("memory-state", "Memory & State Representation", "What should the agent remember?", [
        ("textual", "Textual Memory", "Retain captions, textual summaries, and language-based accounts of past observations.", "sec:mem_text"),
        ("structured", "Structured Memory", "Organize evidence as events, entities, graphs, or other explicitly addressable structures.", "sec:mem_structured"),
        ("compact", "Compact Memory Representation", "Maintain compact latent representations that reduce the cost of storing and revisiting video context.", "sec:mem_latent"),
        ("streaming", "Streaming Memory Management", "Update memory as new observations arrive and support reasoning over an evolving stream.", "sec:mem_streaming"),
    ]),
    ("control-planning", "Control & Planning", "Which action should the agent take?", [
        ("autonomous-tool-use", "Autonomous Tool Use", "Let a controller choose and invoke tools as the evidence and task evolve.", "sec:ctl_tools"),
        ("multi-agent", "Multi-Agent Control", "Distribute perception, reasoning, and coordination across collaborating agents.", "sec:ctl_multi"),
        ("learned-control", "Learned Control Policies", "Learn action selection and planning policies for long-horizon video reasoning.", "sec:ctl_learned"),
        ("fixed-workflow", "Fixed Workflows", "Coordinate evidence processing through a predefined sequence of stages.", "sec:ctl_fixed"),
    ]),
    ("verification-aggregation", "Verification & Aggregation", "Is the evidence sufficient to answer?", [
        ("consensus", "Consensus / Self-Consistency", "Compare candidate answers or reasoning paths to assess agreement.", "sec:ver_selfcons"),
        ("reflection", "Reflection / Refine", "Revisit evidence and revise an answer or plan through feedback.", "sec:ver_reflect"),
        ("confidence", "Confidence / Uncertainty", "Use uncertainty estimates to guide reasoning and evidence seeking.", "sec:ver_conf"),
        ("evidence-alignment", "Evidence Alignment & Adjudication", "Check claims against evidence and reconcile conflicting observations or agent outputs.", "sec:ver_align"),
    ]),
]


def plain(value):
    """Remove BibTeX case protection while retaining common accented author names."""
    accents = {"'": "\u0301", "`": "\u0300", '"': "\u0308", "^": "\u0302", "~": "\u0303"}
    value = re.sub(r"\\([\'`\"^~])\{?(\\i|[A-Za-z])\}?", lambda m: unicodedata.normalize("NFC", m[2].replace("\\i", "i") + accents[m[1]]), value)
    value = value.replace("\\&", "&").replace("\\_", "_").replace("--", "–")
    value = value.replace("$^{*}$", "*")
    value = re.sub(r"\\+\$", "", value).replace("$", "")
    return re.sub(r"\s+", " ", value.replace("{", "").replace("}", "").replace(chr(92), "")).strip()


def parse_bib(source):
    """Parse braced/quoted BibTeX fields, preserving each complete source entry."""
    entries = {}
    pattern = re.compile(r"@(\w+)\s*\{\s*([^,]+),")
    offset = 0
    while match := pattern.search(source, offset):
        i, depth = match.end(), 1
        while i < len(source) and depth:
            if source[i] == "\\":
                i += 2
                continue
            depth += (source[i] == "{") - (source[i] == "}")
            i += 1
        if depth:
            raise ValueError(f"Unclosed bibliography entry: {match[2]}")
        raw, fields = source[match.start():i], {}
        body = source[match.end():i - 1]
        cursor = 0
        while field := re.search(r"(\w+)\s*=\s*", body[cursor:]):
            name = field[1].lower()
            pos = cursor + field.end()
            start = pos
            if body[pos] == "{":
                pos, level = pos + 1, 1
                while pos < len(body) and level:
                    if body[pos] == "\\":
                        pos += 2
                        continue
                    level += (body[pos] == "{") - (body[pos] == "}")
                    pos += 1
                value = body[start + 1:pos - 1]
            elif body[pos] == '"':
                pos += 1
                while pos < len(body) and (body[pos] != '"' or body[pos - 1] == "\\"):
                    pos += 1
                value = body[start + 1:pos]
                pos += 1
            else:
                end = body.find(",", pos)
                pos = len(body) if end < 0 else end
                value = body[start:pos].strip()
            fields[name] = value
            cursor = pos + 1
        key = match[2].strip()
        if key in entries:
            raise ValueError(f"Duplicate citation key: {key}")
        entries[key] = {"fields": fields, "raw": raw}
        offset = i
    return entries


def paper_link(fields):
    if fields.get("url"):
        return fields["url"], "Paper"
    if fields.get("doi"):
        return "https://doi.org/" + fields["doi"], "Paper"
    identifier = re.search(r"(?:arXiv\s*:\s*|^)(\d{4}\.\d{4,5})(?:v\d+)?", fields.get("eprint", "") or fields.get("journal", ""), re.I)
    if identifier:
        return "https://arxiv.org/abs/" + identifier[1], "Paper"
    return "https://scholar.google.com/scholar?q=" + quote('"' + plain(fields["title"]) + '"'), "Find paper"


def import_survey(directory):
    taxonomy = (directory / "sections/taxonomy.tex").read_text()
    bibliography = (directory / "custom.bib").read_text()
    entries = parse_bib(bibliography)
    active = re.sub(r"(?<!\\)%[^\n]*", "", taxonomy)
    labels = {c[3]: (stage, c) for stage in STAGES for c in stage[3]}
    papers, identities, used_keys, current, seen = {}, {}, [], None, set()
    for line in active.splitlines():
        label = re.search(r"\\ref\{(sec:(?:acq|mem|ctl|ver)_\w+)\}", line)
        if label:
            if label[1] not in labels:
                raise ValueError(f"Unknown taxonomy branch {label[1]}; update STAGES in scripts/catalog.py first.")
            current = labels[label[1]]
            seen.add(label[1])
        if "\\citep{" not in line:
            continue
        stage, category = current
        for match in re.finditer(r"(?:^|,)\s*([^,]+?)\s*\\citep\{([^}]+)\}", line):
            enabling = "\\dagger" in match[1]
            name, key = plain(re.sub(r"\$\^\{\\dagger\}\$", "", match[1])), match[2].strip()
            fields = entries[key]["fields"]
            url, kind = paper_link(fields)
            identity = url if kind == "Paper" else plain(fields["title"]).lower()
            canonical = identities.setdefault(identity, key)
            if canonical not in papers:
                papers[canonical] = {
                    "id": canonical, "name": name, "title": plain(fields["title"]),
                    "authors": plain(fields["author"]), "year": int(fields["year"]),
                    "venue": plain(fields.get("booktitle", fields.get("journal", "Preprint"))),
                    "url": url, "link_label": kind, "enabling": False, "citation_keys": [], "categories": [],
                }
            paper = papers[canonical]
            paper["enabling"] = paper["enabling"] or enabling
            if key not in paper["citation_keys"]:
                paper["citation_keys"].append(key)
                used_keys.append(key)
            membership = stage[0] + "/" + category[0]
            if membership not in paper["categories"]:
                paper["categories"].append(membership)
    if seen != set(labels):
        raise ValueError(f"Taxonomy is missing branches: {sorted(set(labels) - seen)}")
    cited = {key.strip() for group in re.findall(r"\\citep\{([^}]+)\}", active) for key in group.split(",")}
    if cited != set(used_keys):
        raise ValueError(f"Unmapped citations: {cited.symmetric_difference(used_keys)}")
    data = {
        "schema_version": 1,
        "sources": {"taxonomy": "sections/taxonomy.tex", "bibliography": "custom.bib",
                    "taxonomy_sha256": hashlib.sha256(taxonomy.encode()).hexdigest(),
                    "bibliography_sha256": hashlib.sha256(bibliography.encode()).hexdigest()},
        "papers": list(papers.values()),
    }
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "data/catalog.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    (ROOT / "references.bib").write_text("% Taxonomy references; original citation keys and metadata retained.\n\n" + "\n\n".join(entries[k]["raw"] for k in used_keys) + "\n")


def escape(value):
    return html.escape(str(value), quote=False).replace("|", "&#124;")


def venue_label(paper):
    venue = paper["venue"]
    if "arxiv" in venue.lower():
        return "arXiv"
    for fragment, label in [
        ("Findings of the Association for Computational Linguistics: ACL", "Findings of ACL"),
        ("Findings of the Association for Computational Linguistics: EMNLP", "Findings of EMNLP"),
        ("Computer Vision and Pattern Recognition", "CVPR"),
        ("computer vision and pattern recognition", "CVPR"),
        ("International Conference on Computer Vision", "ICCV"),
        ("international conference on computer vision", "ICCV"),
        ("European Conference on Computer Vision", "ECCV"),
        ("Empirical Methods in Natural Language Processing", "EMNLP"),
        ("Annual Meeting of the Association for Computational Linguistics", "ACL"),
        ("Neural Information Processing Systems", "NeurIPS"),
        ("neural information processing systems", "NeurIPS"),
        ("International Conference on Machine Learning", "ICML"),
        ("International Conference on Learning Representations", "ICLR"),
        ("Transactions on Machine Learning Research", "TMLR"),
        ("Transactions on Pattern Analysis and Machine Intelligence", "TPAMI"),
        ("AAAI Conference", "AAAI"),
        ("USENIX Symposium", "NSDI"),
        ("MAGMaR", "MAGMaR Workshop"),
        ("Winter Conference on Applications of Computer Vision", "WACV"),
        ("ACM International Conference on Multimedia", "ACM MM"),
        ("Scaling Environments for Agents", "SEA Workshop"),
        ("LLM-based Multi-Agent Systems", "LLM-MAS Workshop"),
        ("Agents in the Wild", "Agents in the Wild"),
        ("ACM SIGKDD", "KDD"),
    ]:
        if fragment in venue:
            return label
    return venue


def badge(label, color, target=None, *, message=None):
    """Use rounded badges; an optional message creates a two-color badge."""
    def encode(value):
        return quote(str(value).replace("-", "--").replace("_", "__"), safe="")
    content = encode(label)
    alt = str(label)
    if message is not None:
        content += "-" + encode(message)
        alt += " " + str(message)
    options = "style=flat" + ("&labelColor=555" if message is not None else "")
    if label == "GitHub":
        options += "&logo=github&logoColor=181717"
    image = f"![{escape(alt)}](https://img.shields.io/badge/{content}-{color}?{options})"
    return f"[{image}]({target})" if target else image


def github_repository(url):
    """Normalize a repository URL for the GitHub stars endpoint."""
    parsed = urlsplit(url)
    parts = parsed.path.strip("/").split("/")
    assert parsed.scheme == "https" and parsed.hostname == "github.com" and len(parts) >= 2, url
    owner, repo = parts[0], parts[1].removesuffix(".git")
    assert re.fullmatch(r"[A-Za-z0-9-]+", owner) and re.fullmatch(r"[A-Za-z0-9_.-]+", repo), url
    return owner + "/" + repo


def github_stars_badge(url):
    """One compact badge: dark `Code` label and the live star count (served by Shields.io)."""
    repo = github_repository(url)
    image = f"![Code, GitHub stars for {escape(repo)}](https://img.shields.io/github/stars/{repo}?style=flat&logo=github&logoColor=white&label=Code&labelColor=24292f&color=57606a)"
    return f"[{image}](https://github.com/{repo})"


def publication_badge(paper):
    venue = venue_label(paper)
    if venue == "arXiv" or (venue == "Preprint" and urlsplit(paper["url"]).hostname == "arxiv.org"):
        return badge("arXiv", "red", message=paper["year"])
    return badge(venue, "lightgrey" if venue == "Preprint" else "blue", message=paper["year"])


CATEGORY_INDEX = {s[0] + "/" + c[0]: (s, c) for s in STAGES for c in s[3]}
ENABLING_NOTE = "<sup>†</sup>"


def row(paper, crosslinks=False):
    """Render one table row; the root README and papers/index.md use different relative paths."""
    prefix = "../" if crosslinks else ""
    authors = paper["authors"].split(" and ")
    first = authors[0].split(",")
    author = " ".join(reversed(first)).strip() + (" et al." if len(authors) > 1 else "")
    name = escape(paper["name"]) + (ENABLING_NOTE if paper.get("enabling") else "")
    method = f'<strong>{name}</strong><br>{publication_badge(paper)}'
    if paper["link_label"] == "Find paper":
        title, links = escape(paper["title"]), [f'[Find&nbsp;paper]({paper["url"]})']
    else:
        title = f'<a href="{html.escape(paper["url"], quote=True)}">{escape(paper["title"])}</a>'
        arxiv = urlsplit(paper["url"]).hostname == "arxiv.org"
        links = [badge("arXiv", "red", paper["url"]) if arxiv else badge("Paper", "blue" if venue_label(paper) != "Preprint" else "lightgrey", paper["url"])]
    links.append(badge("BibTeX", "lightgrey", f'{prefix}references.bib#L{paper["bib_line"]}'))
    cell = " ".join(links) + (("<br>" + github_stars_badge(paper["code_url"])) if paper.get("code_url") else "")
    paper_cell = f'{title}<br><sub>{escape(author)}</sub>'
    if crosslinks:
        categories = [badge(CATEGORY_INDEX[m][1][1], PALETTE[m.split("/")[0]]["badge"], f"{prefix}README.md#{m.split('/')[1]}") for m in paper["categories"]]
        return f'| {method} | {paper_cell} | {"<br>".join(categories)} | {cell} |'
    return f'| {method} | {paper_cell} | {cell} |'


def stage_papers(papers, stage_id):
    return [p for p in papers if any(c.startswith(stage_id + "/") for c in p["categories"])]


def render_taxonomy(papers):
    """Render the complete taxonomy: stage cards, taxonomy figure, and one table per category."""
    total_enabling = sum(bool(p.get("enabling")) for p in papers)
    cards = "\n".join(f'  <a href="#{s[0]}"><img src="assets/card-{s[0]}.png" width="49%" alt="Stage {i}: {escape(s[1])}"></a>' for i, s in enumerate(STAGES, 1))
    lines = ['<div align="center">', cards, "</div>", "",
              '<p align="center">',
              '  <a href="assets/taxonomy.png"><img src="assets/taxonomy.png" alt="Stage-centered taxonomy of long-video agents and agent-enabling methods" width="720"></a>',
              "  <br><sub><b>The method-level taxonomy</b> from the survey appendix. Click to view at full resolution.</sub>",
              "</p>", "",
              f"> **Reading the tables.** Categories are *non-exclusive*: a paper appears under every branch where it makes a substantive methodological contribution. Unmarked entries are *core video agents* whose later evidence-access actions depend on earlier video-derived observations. Entries marked with <sup>†</sup> ({total_enabling} papers) are *agent-enabling methods or conceptual precursors*: they contribute useful video processing, memory, retrieval, or reflection mechanisms without independently establishing closed-loop video-evidence behavior.", ""]
    for number, (stage_id, title, question, cats) in enumerate(STAGES, 1):
        selected = stage_papers(papers, stage_id)
        group_counts = {c[0]: sum(stage_id + "/" + c[0] in p["categories"] for p in papers) for c in cats}
        chips = " ".join(badge(SHORT[c[0]], PALETTE[stage_id]["badge"], f"#{c[0]}", message=group_counts[c[0]]) for c in cats)
        lines += [f'<a id="{stage_id}"></a>', "", f"## {title}", "",
                  f'<img src="assets/header-{stage_id}.png" width="100%" alt="Stage {number}: {escape(question)}">', "", '<div align="center">', "", chips, "", "</div>", ""]
        for cat_id, cat_title, description, _ in cats:
            group = sorted([p for p in selected if stage_id + "/" + cat_id in p["categories"]], key=lambda p: (-p["year"], p["name"].casefold()))
            count_badge = f'<img src="https://img.shields.io/badge/{len(group)}_papers-{PALETTE[stage_id]["badge"]}?style=flat" alt="{len(group)} papers">'
            lines += [f'<a id="{cat_id}"></a>', "", "<details>",
                      f'<summary><b>{cat_title}</b> &nbsp;{count_badge}&nbsp; <sub><i>👆 click to expand</i></sub></summary>', "",
                      f"{description}", "", "| Method | Paper | Links |", "| :--- | :--- | :--- |"]
            lines += [row(p) for p in group]
            lines += ["", '<div align="right"><a href="#taxonomy">↑ Back to taxonomy</a></div>', "", "</details>", ""]
    return "\n".join(lines)


def render(data):
    papers = data["papers"]
    output = {}
    bib_source = (ROOT / "references.bib").read_text()
    entries = parse_bib(bib_source)
    for paper in papers:
        paper["bib_line"] = bib_source[:bib_source.index(entries[paper["id"]]["raw"])].count("\n") + 1
    note = "> Venue and year follow the supplied survey bibliography. **arXiv / Paper** badges link to bibliographic identifiers or documented link overrides; **Find paper** opens a title search when no direct identifier is available. Methods can appear in multiple branches; <sup>†</sup> marks agent-enabling methods. See the [badge colors](../README.md#badge-colors).\n"
    lines = ["<!-- Generated by scripts/catalog.py; edit data/catalog.json and rebuild. -->", "", "[← Overview](../README.md) · [Taxonomy](../README.md#taxonomy) · [Recent additions](recent-additions.md) · [BibTeX](../references.bib) · [Machine-readable catalog](../data/catalog.json)", "", "# All Papers", "", "A chronological view of the survey taxonomy. For the stage-by-stage tables, see the [taxonomy in the README](../README.md#taxonomy); for methods awaiting integration, see [Recent Additions](recent-additions.md).", "", f"**{len(papers)} unique papers**, indexed by year. Use your browser's **Find** command to search a method, title, or author. The category links open the corresponding table in the README.", "", note, " · ".join(f"[{y}](#year-{y})" for y in sorted({p["year"] for p in papers}, reverse=True)), ""]
    for year in sorted({p["year"] for p in papers}, reverse=True):
        lines += [f'<a id="year-{year}"></a>', "", f"## {year}", "", "| Method & paper | Year · Venue | Taxonomy | Links |", "| :--- | :--- | :--- | :--- |"]
        lines += [row(p, True) for p in sorted(papers, key=lambda p: p["name"].casefold()) if p["year"] == year]
        lines += [""]
    output["papers/index.md"] = "\n".join(lines)
    readme = (ROOT / "README.md").read_text()
    keys = sum(len(p["citation_keys"]) for p in papers)
    summary = f"**{len(papers)} unique papers · {len(STAGES)} stages · {sum(len(s[3]) for s in STAGES)} categories**"
    readme = re.sub(r"(?<=<!-- catalog-stats:start -->).*?(?=<!-- catalog-stats:end -->)", "\n" + summary + "\n", readme, flags=re.S)
    readme = re.sub(r"badge/Papers-\d+-", f"badge/Papers-{len(papers)}-", readme)
    readme = re.sub(r"(?<=<!-- taxonomy:start -->).*?(?=<!-- taxonomy:end -->)", lambda _: "\n" + render_taxonomy(papers) + "\n", readme, flags=re.S)
    output["README.md"] = readme
    return output


def validate(data):
    papers = data["papers"]
    assert len({p["id"] for p in papers}) == len(papers), "Duplicate paper IDs"
    allowed = set(CATEGORY_INDEX)
    entries = parse_bib((ROOT / "references.bib").read_text())
    keys = [key for p in papers for key in p["citation_keys"]]
    assert set(keys) == set(entries), "Catalog and bibliography keys differ"
    assert len(keys) == len(set(keys)), "Citation key assigned to multiple papers"
    for paper in papers:
        assert paper["categories"] and set(paper["categories"]) <= allowed
        assert len(paper["categories"]) == len(set(paper["categories"])), paper["id"]
        assert paper["id"] in paper["citation_keys"], paper["id"]
        assert paper["url"].startswith("https://"), paper["id"]
        assert paper["link_label"] in ("Paper", "Find paper")
        if paper.get("code_url"):
            github_repository(paper["code_url"])
        assert all(paper[field] for field in ("name", "title", "authors", "year", "venue"))
    print(f"Validated {len(papers)} papers, {len(keys)} citation keys, {len(allowed)} categories.")



def check_local_links():
    """Check repository-relative Markdown/HTML links and GitHub-style anchors."""
    checked = 0
    for source in ROOT.rglob("*.md"):
        if ".git" in source.parts:
            continue
        body = source.read_text()
        links = re.findall(r"\]\(([^\s)]+)\)", body)
        links += re.findall(r'(?:href|src)="([^"]+)"', body)
        for link in links:
            parsed = urlsplit(html.unescape(link))
            if parsed.scheme or parsed.netloc:
                continue
            target = (source.parent / unquote(parsed.path)).resolve() if parsed.path else source
            assert target.is_relative_to(ROOT), f"Link escapes repository: {source}: {link}"
            assert target.exists(), f"Missing local target: {source}: {link}"
            anchor = unquote(parsed.fragment)
            if anchor and target.suffix == ".md":
                content = target.read_text()
                anchors = set(re.findall(r'id="([^"]+)"', content))
                for heading in re.findall(r"^#{1,6} +(.+)$", content, re.M):
                    slug = re.sub(r"[^\w\- ]", "", html.unescape(heading).lower()).replace(" ", "-")
                    anchors.add(slug)
                assert anchor in anchors, f"Missing anchor: {source}: {link}"
            elif anchor and target.suffix == ".bib":
                assert re.fullmatch(r"L[1-9][0-9]*", anchor), link
                assert int(anchor[1:]) <= len(target.read_text().splitlines()), link
            checked += 1
    for asset in ["banner.png", "survey-teaser.png", "taxonomy.png", "publication-growth.png"]:
        assert (ROOT / "assets" / asset).read_bytes().startswith(b"\x89PNG\r\n\x1a\n"), asset
    print(f"Validated {checked} local links and the visual assets.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--import-survey", type=Path, help="Survey directory containing sections/taxonomy.tex and custom.bib")
    parser.add_argument("--check", action="store_true", help="Validate metadata and check generated catalogs without writing files")
    args = parser.parse_args()
    if args.import_survey and args.check:
        parser.error("--import-survey and --check cannot be combined")
    if args.import_survey:
        import_survey(args.import_survey)
    data = json.loads((ROOT / "data/catalog.json").read_text())
    overrides_path = ROOT / "data/link-overrides.json"
    if overrides_path.exists():
        overrides = json.loads(overrides_path.read_text())
        assert all(v["url"].startswith("https://") and v["source"].startswith("https://") for v in overrides.values())
        assert set(overrides) <= {p["id"] for p in data["papers"]}, "Unknown override ID"
        for paper in data["papers"]:
            if paper["id"] in overrides:
                paper["url"] = overrides[paper["id"]]["url"]
                paper["link_label"] = "Paper"
    code_links_path = ROOT / "data/code-links.json"
    if code_links_path.exists():
        code_links = json.loads(code_links_path.read_text())
        assert set(code_links) <= {p["id"] for p in data["papers"]}, "Unknown code-link ID"
        for key, entry in code_links.items():
            github_repository(entry["url"])
            assert entry["source"].startswith("https://"), key
        for paper in data["papers"]:
            if paper["id"] in code_links:
                paper["code_url"] = code_links[paper["id"]]["url"]
    validate(data)
    stale = []
    for path, content in render(data).items():
        target = ROOT / path
        if args.check:
            if not target.exists() or target.read_text() != content:
                stale.append(path)
        else:
            target.parent.mkdir(exist_ok=True)
            target.write_text(content)
    if stale:
        sys.exit("Stale catalogs: " + ", ".join(stale))
    check_local_links()
    print("Catalogs are up to date." if args.check else "Rendered the README taxonomy and the paper index.")


if __name__ == "__main__":
    main()
