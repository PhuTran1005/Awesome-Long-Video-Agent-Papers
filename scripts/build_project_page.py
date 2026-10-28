#!/usr/bin/env python3
"""Build the static project page from the survey catalog (Python standard library only)."""
import argparse
from collections import Counter
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import sys
from urllib.parse import unquote, urlsplit

sys.dont_write_bytecode = True
from catalog import STAGES, parse_bib, venue_label
from theme import PALETTE

ROOT = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/PhuTran1005/Awesome-Long-Video-Agent-Papers'
STAGE_CLASSES = ['acquisition', 'memory', 'control', 'verification']
STAGE_SHORT = ['Acquisition', 'Memory', 'Planning', 'Verification']
DESCRIPTIONS = [
    'Seek relevant evidence instead of processing every frame. Acquisition methods decide which moments, modalities, and levels of detail to observe.',
    'Make earlier observations useful for later decisions. Memory methods organize, compress, retrieve, and update evidence across long temporal horizons.',
    'Turn observations into an actionable next step. Controllers select tools, coordinate agents, and choose how to allocate the reasoning process.',
    'Assess whether an answer is supported. Verification methods compare hypotheses, revisit evidence, express uncertainty, and reconcile competing claims.'
]


def escape(value):
    return html.escape(str(value), quote=True)


def read_json(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))


def load_data():
    catalog = read_json('data/catalog.json')
    overrides = read_json('data/link-overrides.json')
    code_links = read_json('data/code-links.json')
    bibliography = parse_bib((ROOT / 'references.bib').read_text(encoding='utf-8'))
    papers = catalog['papers']
    ids = [p['id'] for p in papers]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate paper IDs')
    if not set(overrides) <= set(ids) or not set(code_links) <= set(ids):
        raise ValueError('Unknown paper ID in link maps')
    keys = [key for p in papers for key in p['citation_keys']]
    if set(keys) != set(bibliography) or len(keys) != len(set(keys)):
        raise ValueError('Catalog and bibliography citation keys differ')
    allowed = {s[0] + '/' + c[0] for s in STAGES for c in s[3]}
    if any(not p['categories'] or not set(p['categories']) <= allowed for p in papers):
        raise ValueError('Invalid category assignment')
    for paper in papers:
        if paper['id'] in overrides:
            paper['url'] = overrides[paper['id']]['url']
            paper['link_label'] = 'Paper'
        if paper['id'] in code_links:
            paper['code_url'] = code_links[paper['id']]['url']
        paper['venue_label'] = venue_label(paper)
        paper['bibtex'] = '\n\n'.join(bibliography[key]['raw'] for key in paper['citation_keys'])
        for field in ['url', 'code_url']:
            if paper.get(field) and urlsplit(paper[field]).scheme != 'https':
                raise ValueError('Expected HTTPS publication/code link: ' + paper['id'])
    return sorted(papers, key=lambda p: (-p['year'], p['name'].casefold()))


def render_card(paper, category_names, stage_classes):
    tags = ''.join(f'<a class="paper-tag {stage_classes[c.split("/")[0]]}" href="#papers" data-filter-category="{escape(c)}">{escape(category_names[c])}</a>' for c in paper['categories'])
    first = paper['authors'].split(' and ')[0]
    if ',' in first:
        parts = first.split(',', 1)
        first = parts[1].strip() + ' ' + parts[0].strip()
    authors = first + (' et al.' if ' and ' in paper['authors'] else '')
    label = 'Find paper' if paper['link_label'] == 'Find paper' else ('arXiv' if 'arxiv.org' in paper['url'] else 'Paper')
    enabling = '<sup title="Agent-enabling method or conceptual precursor">†</sup>' if paper['enabling'] else ''
    scope = '<span class="paper-scope">Agent-enabling method</span>' if paper['enabling'] else ''
    code = f'<a class="code-link" href="{escape(paper["code_url"])}" target="_blank" rel="noopener noreferrer" aria-label="Official code for {escape(paper["name"])}">Code ↗</a>' if paper.get('code_url') else ''
    return f'''<article class="paper-card" data-paper-id="{escape(paper['id'])}" id="paper-{escape(paper['id'])}">
<div class="paper-identity"><div class="paper-method">{escape(paper['name'])}{enabling}</div><div class="paper-meta"><span class="paper-year">{paper['year']}</span> {escape(paper['venue_label'])}</div>{scope}</div>
<div class="paper-body"><a class="paper-title" href="{escape(paper['url'])}" target="_blank" rel="noopener noreferrer">{escape(paper['title'])}</a><p class="paper-authors" title="{escape(paper['authors'])}">{escape(authors)}</p><div class="paper-tags">{tags}</div></div>
<div class="paper-links"><a class="publication-link" href="{escape(paper['url'])}" target="_blank" rel="noopener noreferrer" aria-label="{label} for {escape(paper['name'])}">{label} ↗</a>{code}<button data-cite="{escape(paper['id'])}" aria-label="BibTeX for {escape(paper['name'])}" hidden>BibTeX ⧉</button></div></article>'''


def render():
    papers = load_data()
    category_names = {s[0] + '/' + c[0]: c[1] for s in STAGES for c in s[3]}
    stage_classes = {s[0]: STAGE_CLASSES[i] for i, s in enumerate(STAGES)}
    counts = Counter(c for p in papers for c in p['categories'])
    years = Counter(p['year'] for p in papers)
    tabs, panels, filters, options, stage_data = [], [], [], [], []
    filters.append(f'<button class="stage-filter" data-stage="" aria-pressed="true">All papers <span>{len(papers)}</span></button>')
    for index, (stage_id, title, question, categories) in enumerate(STAGES):
        cls = STAGE_CLASSES[index]
        count = sum(any(c.startswith(stage_id + '/') for c in p['categories']) for p in papers)
        tabs.append(f'<button class="taxonomy-tab {cls}" role="tab" id="tab-{stage_id}" aria-controls="panel-{stage_id}" aria-selected="{str(index == 0).lower()}" tabindex="{0 if index == 0 else -1}"><span class="tab-number">0{index+1}</span><span class="tab-copy"><strong>{escape(title)}</strong><small>{count} papers · 4 mechanisms</small></span><span class="tab-arrow" aria-hidden="true">↗</span></button>')
        mechanisms, category_data = [], []
        options.append(f'<optgroup label="{escape(title)}">')
        for category_id, category_title, description, _ in categories:
            full_id = stage_id + '/' + category_id
            mechanisms.append(f'<a class="mechanism" href="#papers" data-filter-category="{full_id}" title="{escape(description)}"><span>{escape(category_title)}</span><small>{counts[full_id]}</small><span aria-hidden="true">↗</span></a>')
            options.append(f'<option value="{full_id}" data-stage="{stage_id}">{escape(category_title)} ({counts[full_id]})</option>')
            category_data.append({'id': full_id, 'title': category_title, 'count': counts[full_id]})
        options.append('</optgroup>')
        icon = PALETTE[stage_id]['icon']
        panels.append(f'<section class="taxonomy-panel {cls}" role="tabpanel" id="panel-{stage_id}" aria-labelledby="tab-{stage_id}" tabindex="0"><div class="panel-header"><div><p class="panel-kicker">Stage 0{index+1} / {escape(STAGE_SHORT[index])}</p><h3>{escape(question)}</h3></div><img class="panel-icon" src="assets/icons/{icon}.png" width="48" height="48" alt="" loading="lazy"></div><p class="panel-description">{escape(DESCRIPTIONS[index])}</p><div class="mechanisms">{"".join(mechanisms)}</div><div class="panel-footer"><span></span>{count} unique papers in this stage · Click a mechanism to explore</div></section>')
        filters.append(f'<button class="stage-filter {cls}" data-stage="{stage_id}" aria-pressed="false">{escape(STAGE_SHORT[index])} <span>{count}</span></button>')
        stage_data.append({'id': stage_id, 'title': title, 'count': count, 'categories': category_data})
    bars = ''.join(f'<div class="chart-row"><span class="chart-year">{year}</span><div class="chart-track"><span class="chart-fill" style="--bar-width:{years[year]/max(years.values())*100:.2f}%"></span></div><span class="chart-value">{years[year]}</span></div>' for year in sorted(years))
    # Prevent bibliography text from closing an application/json script element.
    payload = json.dumps({'papers': papers, 'stages': stage_data, 'categoryNames': category_names}, ensure_ascii=False, separators=(',', ':')).replace('&', '\u0026').replace('<', '\u003c').replace('>', '\u003e')
    values = {
        'REPO': REPO, 'TOTAL': str(len(papers)), 'ENABLING': str(sum(p['enabling'] for p in papers)),
        'YEAR_RANGE': f'{min(years)}–{max(years)}', 'TAXONOMY_TABS': '\n'.join(tabs),
        'TAXONOMY_PANELS': '\n'.join(panels), 'STAGE_FILTERS': '\n'.join(filters),
        'CATEGORY_OPTIONS': '\n'.join(options),
        'YEAR_OPTIONS': ''.join(f'<option value="{year}">{year}</option>' for year in sorted(years, reverse=True)),
        'YEAR_BARS': bars, 'PAPER_CARDS': '\n'.join(render_card(p, category_names, stage_classes) for p in papers),
        'DATA_JSON': payload,
    }
    template = (ROOT / 'project-page/index.template.html').read_text(encoding='utf-8')
    result = re.sub(r'@@([A-Z_]+)@@', lambda m: values[m[1]], template)
    if re.search(r'@@[A-Z_]+@@', result):
        raise ValueError('Unexpanded template token')
    return result


class PageValidator(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.cards = set(), [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                raise ValueError('Duplicate HTML id: ' + attrs['id'])
            self.ids.add(attrs['id'])
        if 'data-paper-id' in attrs:
            self.cards.append(attrs['data-paper-id'])
        for name in ['href', 'src']:
            if attrs.get(name):
                self.links.append(attrs[name])
        if tag == 'a' and attrs.get('target') == '_blank' and 'noopener' not in attrs.get('rel', ''):
            raise ValueError('External link lacks noopener')
        if tag == 'img' and 'alt' not in attrs:
            raise ValueError('Image lacks alt text')

    def verify(self, expected):
        if set(self.cards) != expected or len(self.cards) != len(expected):
            raise ValueError('Paper coverage mismatch')
        for link in self.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            if parsed.path and not (ROOT / unquote(parsed.path)).is_file():
                raise ValueError('Missing local asset: ' + link)
            if not parsed.path and parsed.fragment and parsed.fragment not in self.ids:
                raise ValueError('Missing anchor: ' + link)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check generated HTML without writing')
    parser.add_argument('--output', type=Path, help='Package a minimal static site into this directory')
    args = parser.parse_args()
    if args.check and args.output:
        parser.error('--check and --output cannot be combined')
    result = render()
    validator = PageValidator()
    validator.feed(result)
    validator.verify({p['id'] for p in read_json('data/catalog.json')['papers']})
    target = ROOT / 'index.html'
    if args.check:
        if not target.exists() or target.read_text(encoding='utf-8') != result:
            raise SystemExit('Project page is stale. Run: python scripts/build_project_page.py')
        print(f'Project page is current: {len(validator.cards)} papers, all local links valid.')
        return
    if args.output:
        output = args.output.resolve()
        if output == ROOT or output in [ROOT / name for name in ['assets', 'data', 'project-page', 'scripts', '.git']]:
            parser.error('Choose a dedicated output directory, such as dist')
        output.mkdir(parents=True, exist_ok=True)
        (output / 'index.html').write_text(result, encoding='utf-8', newline='\n')
        paths = ['project-page/styles.css', 'project-page/app.js', 'project-page/favicon.svg', 'references.bib', 'data/catalog.json', 'assets/banner.png', 'assets/survey-teaser.png', 'assets/taxonomy.png']
        paths += ['assets/icons/' + PALETTE[s[0]]['icon'] + '.png' for s in STAGES]
        for name in paths:
            destination = output / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, destination)
        (output / '.nojekyll').touch()
        print('Packaged static site: ' + str(output))
    else:
        target.write_text(result, encoding='utf-8', newline='\n')
        print(f'Built index.html: {len(validator.cards)} papers.')


if __name__ == '__main__':
    main()
