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
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
STAGES = [
    ("evidence-acquisition", "Evidence Acquisition", "Where should the agent look next?", [
        ("retrieval-based", "Retrieval-based", "Retrieve relevant moments, documents, or multimodal evidence in response to a query."),
        ("hierarchical", "Hierarchical", "Navigate from coarse summaries to finer temporal or spatial evidence."),
        ("programmatic", "Programmatic", "Compose executable programs that probe video content with perception tools."),
        ("learned-policy", "Learned policy", "Learn when, where, or at what granularity to acquire the next observation."),
    ]),
    ("memory-state", "Memory & State Representation", "What should the agent remember?", [
        ("caption-text", "Caption / Text", "Retain captions, textual summaries, and language-based accounts of past observations."),
        ("structured", "Structured", "Organize evidence as events, entities, graphs, or other explicitly addressable structures."),
        ("latent-compressed", "Latent / Compressed", "Maintain compact representations that reduce the cost of storing and revisiting video context."),
        ("streaming-online", "Streaming / Online", "Update memory as new observations arrive and support reasoning over an evolving stream."),
    ]),
    ("control-planning", "Control & Planning", "Which action should the agent take?", [
        ("fixed-workflow", "Fixed workflow", "Coordinate evidence processing through a predefined sequence of stages."),
        ("autonomous-tool-use", "Autonomous tool use", "Let a controller choose and invoke tools as the evidence and task evolve."),
        ("multi-agent", "Multi-agent", "Distribute perception, reasoning, and coordination across collaborating agents."),
        ("learned-control", "Learned control", "Learn action selection and planning policies for long-horizon video reasoning."),
    ]),
    ("verification-aggregation", "Verification & Aggregation", "Is the evidence sufficient to answer?", [
        ("self-consistency", "Self-consistency", "Compare candidate answers or reasoning paths to assess agreement."),
        ("reflection-refine", "Reflection / Refine", "Revisit evidence and revise an answer or plan through feedback."),
        ("confidence-calibration", "Confidence / Calibration", "Use uncertainty estimates to guide reasoning and evidence seeking."),
        ("evidence-alignment-adjudication", "Evidence alignment & Adjudication", "Check claims against evidence and reconcile conflicting observations or agent outputs."),
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
    branches = [line for line in active.splitlines() if "\\citep{" in line]
    specs = [(s, c) for s in STAGES for c in s[3]]
    if len(branches) != len(specs):
        raise ValueError("Taxonomy structure changed; review the 16 branch definitions before importing.")
    papers, identities, used_keys = {}, {}, []
    for line, (stage, category) in zip(branches, specs):
        for match in re.finditer(r"(?:^|,)\s*([^,]+?)\s*\\citep\{([^}]+)\}", line):
            name, key = plain(match[1]), match[2].strip()
            fields = entries[key]["fields"]
            url, kind = paper_link(fields)
            identity = url if kind == "Paper" else plain(fields["title"]).lower()
            canonical = identities.setdefault(identity, key)
            if canonical not in papers:
                papers[canonical] = {
                    "id": canonical, "name": name, "title": plain(fields["title"]),
                    "authors": plain(fields["author"]), "year": int(fields["year"]),
                    "venue": plain(fields.get("booktitle", fields.get("journal", "Preprint"))),
                    "url": url, "link_label": kind, "citation_keys": [], "categories": [],
                }
            paper = papers[canonical]
            if key not in paper["citation_keys"]:
                paper["citation_keys"].append(key)
                used_keys.append(key)
            membership = stage[0] + "/" + category[0]
            if membership not in paper["categories"]:
                paper["categories"].append(membership)
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
    shutil.copyfile(directory / "files/survey_teaser.png", ROOT / "assets/survey-teaser.png")


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
    repo = github_repository(url)
    image = f"![GitHub stars for {escape(repo)}](https://img.shields.io/github/stars/{repo}?style=social&label=Star)"
    return f"[{image}](https://github.com/{repo})"


def publication_badge(paper):
    venue = venue_label(paper)
    if venue == "arXiv" or (venue == "Preprint" and urlsplit(paper["url"]).hostname == "arxiv.org"):
        return badge("arXiv", "red", message=paper["year"])
    return badge(venue, "lightgrey" if venue == "Preprint" else "blue", message=paper["year"])


def row(paper, crosslinks=False):
    authors = paper["authors"].split(" and ")
    first = authors[0].split(",")
    author = " ".join(reversed(first)).strip() + (" et al." if len(authors) > 1 else "")
    details = f'<strong>{escape(paper["name"])}</strong><br>{escape(paper["title"])}<br><sub>{escape(author)}</sub>'
    if paper["link_label"] == "Find paper":
        links = f'[Find paper]({paper["url"]})'
    elif urlsplit(paper["url"]).hostname == "arxiv.org":
        links = badge("arXiv", "red", paper["url"])
    else:
        links = badge("Paper", "blue" if venue_label(paper) != "Preprint" else "lightgrey", paper["url"])
    if paper.get("code_url"):
        links += " " + badge("GitHub", "white", paper["code_url"]) + " " + github_stars_badge(paper["code_url"])
    links += f' · [BibTeX](../references.bib#L{paper["bib_line"]})'
    publication = publication_badge(paper)
    if crosslinks:
        categories = []
        for membership in paper["categories"]:
            stage_id, cat_id = membership.split("/")
            stage = next(s for s in STAGES if s[0] == stage_id)
            cat = next(c for c in stage[3] if c[0] == cat_id)
            categories.append(badge(cat[1], "green", f"{stage_id}.md#{cat_id}"))
        return f'| {details} | {publication} | {"<br>".join(categories)} | {links} |'
    return f'| {details} | {publication} | {links} |'


def render(data):
    papers = data["papers"]
    output = {}
    bib_source = (ROOT / "references.bib").read_text()
    entries = parse_bib(bib_source)
    for paper in papers:
        paper["bib_line"] = bib_source[:bib_source.index(entries[paper["id"]]["raw"])].count("\n") + 1
    note = "> Venue and year follow the supplied survey bibliography. **arXiv / Paper** badges link to bibliographic identifiers or documented link overrides; **Find paper** opens a title search when no direct identifier is available. Methods can appear in multiple branches. See the [badge colors](../README.md#badge-colors).\n"
    for stage_id, title, question, cats in STAGES:
        selected = [p for p in papers if any(c.startswith(stage_id + "/") for c in p["categories"])]
        lines = ["<!-- Generated by scripts/catalog.py; edit data/catalog.json and rebuild. -->", "", "[← Overview](../README.md) · [All papers](index.md) · [BibTeX](../references.bib)", '', '<a id="top"></a>', '', f"# {title}", "", badge(title, "purple", "../README.md#taxonomy"), "", f"**{question}**", "", f"{len(selected)} unique papers across {len(cats)} mechanisms. Assignments follow the survey taxonomy.", "", " ".join(badge(c[1], "green", f"#{c[0]}") for c in cats), "", note]
        for cat_id, cat_title, description in cats:
            group = sorted([p for p in selected if stage_id + "/" + cat_id in p["categories"]], key=lambda p: (-p["year"], p["name"].casefold()))
            lines += [f'<a id="{cat_id}"></a>', "", f"## {cat_title}", "", description, "", f"**{len(group)} papers** · Newest bibliographic year first.", "", "| Method & paper | Year · Venue | Links |", "| :--- | :--- | :--- |"]
            lines += [row(p) for p in group]
            lines += ["", "[Back to top](#top)", ""]
        output[f"papers/{stage_id}.md"] = "\n".join(lines)
    lines = ["<!-- Generated by scripts/catalog.py; edit data/catalog.json and rebuild. -->", "", "[← Overview](../README.md) · [Recent additions](recent-additions.md) · [BibTeX](../references.bib) · [Machine-readable catalog](../data/catalog.json)", "", "# All Papers", "", "This index covers the survey taxonomy. See [Recent Additions](recent-additions.md) for methods awaiting taxonomy integration.", "", f"**{len(papers)} unique papers**, indexed by year. Use your browser's **Find** command to search a method, title, or author. The category links open the corresponding reading list.", "", note, " · ".join(f"[{y}](#year-{y})" for y in sorted({p["year"] for p in papers}, reverse=True)), ""]
    for year in sorted({p["year"] for p in papers}, reverse=True):
        lines += [f'<a id="year-{year}"></a>', "", f"## {year}", "", "| Method & paper | Year · Venue | Taxonomy | Links |", "| :--- | :--- | :--- | :--- |"]
        lines += [row(p, True) for p in sorted(papers, key=lambda p: p["name"].casefold()) if p["year"] == year]
        lines += [""]
    output["papers/index.md"] = "\n".join(lines)
    readme = (ROOT / "README.md").read_text()
    keys = sum(len(p["citation_keys"]) for p in papers)
    summary = f"**{len(papers)} unique papers · {keys} citation keys · {len(STAGES)} stages · {sum(len(s[3]) for s in STAGES)} categories**"
    readme = re.sub(r"(?<=<!-- catalog-stats:start -->).*?(?=<!-- catalog-stats:end -->)", "\n" + summary + "\n", readme, flags=re.S)
    readme = re.sub(r"badge/Papers-\d+-", f"badge/Papers-{len(papers)}-", readme)
    for stage_id, _, _, _ in STAGES:
        count = sum(any(c.startswith(stage_id + "/") for c in p["categories"]) for p in papers)
        readme = re.sub(r"\[\*\*Explore \d+ papers →\*\*\]\(papers/" + stage_id + r"\.md\)", f"[**Explore {count} papers →**](papers/{stage_id}.md)", readme)
    output["README.md"] = readme
    return output


def validate(data):
    papers = data["papers"]
    assert len({p["id"] for p in papers}) == len(papers), "Duplicate paper IDs"
    allowed = {s[0] + "/" + c[0] for s in STAGES for c in s[3]}
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
    ET.parse(ROOT / "assets/banner.svg")
    assert (ROOT / "assets/survey-teaser.png").read_bytes().startswith(b"\x89PNG\r\n\x1a\n")
    print(f"Validated {checked} local links and the visual assets.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--import-survey", type=Path, help="Survey directory containing sections/taxonomy.tex, custom.bib, and files/survey_teaser.png")
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
    print("Catalogs are up to date." if args.check else "Rendered five paper catalogs and refreshed README counts.")


if __name__ == "__main__":
    main()
