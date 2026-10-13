#!/usr/bin/env python3
"""Render the README artwork (banner, stage cards, stage headers) to PNG with headless Chrome.

The artwork reuses the visual language of the survey's pipeline figure: pastel boxes with
a saturated border, a dashed inner frame, numbered circles, and the figure's own icons
(assets/icons). Counts come from data/catalog.json, so rerun this after the catalog changes.

    python3 scripts/artwork.py                      # writes assets/banner.png, card-*.png, header-*.png
    python3 scripts/artwork.py --survey /path/to/survey   # exports the teaser (panel a only) and publication chart

Requires Google Chrome / Chromium and Pillow; the HTML sources are written next to the PNGs only in
a temporary directory.
"""

import base64
import json
import shutil
import subprocess
import sys
import tempfile
from html import escape
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
import catalog
from theme import PALETTE, SHORT

ROOT = Path(__file__).resolve().parents[1]
SANS = "'Liberation Sans', Arimo, Arial, Helvetica, sans-serif"
SERIF = "Tinos, 'Liberation Serif', 'Times New Roman', serif"
PURPLE = "#7b3fc4"
INK = "#1b1b1b"
GRAY = "#6b6b6b"
# Order and numbering follow the loop in the survey's pipeline figure.
LOOP = [("control-planning", 1, "Control", "reason / plan / act"),
        ("evidence-acquisition", 2, "Acquisition", "seek / retrieve / observe"),
        ("memory-state", 3, "Memory", "write / compress / retrieve"),
        ("verification-aggregation", 4, "Verification", "check / aggregate / stop")]


def icon(name):
    data = base64.b64encode((ROOT / "assets/icons" / f"{name}.png").read_bytes()).decode()
    return f"data:image/png;base64,{data}"


def page(width, height, body, css=""):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;padding:0;background:transparent}}
body{{position:relative;width:{width}px;height:{height}px;font-family:{SANS};color:{INK};overflow:hidden}}
*{{box-sizing:border-box}} .serif{{font-family:{SERIF}}}
{css}</style></head><body>{body}</body></html>"""


def banner(n_papers, n_stages, n_cats):
    boxes, arrows = [], {0: ("action", "a<sub>t</sub>"), 1: ("observation", "o<sub>t</sub>"), 2: ("state", "s<sub>t+1</sub>")}
    for i, (stage_id, number, title, hint) in enumerate(LOOP):
        p = PALETTE[stage_id]
        boxes.append(f"""<div class="box" style="background:{p['fill']};border-color:{p['border']}">
          <div class="head"><span class="dot" style="background:{p['border']}">{number}</span><span class="name">{title}</span></div>
          <div class="hint">{hint}</div>
          <div class="inner" style="border-color:{p['border']}"><img src="{icon(p['icon'])}"></div></div>""")
        if i in arrows:
            label, math = arrows[i]
            boxes.append(f"""<div class="arrow"><div class="lab serif">{label}<br><i>{math}</i></div>
              <svg width="110" height="20" viewBox="0 0 110 20"><path d="M2 10H98" stroke="{INK}" stroke-width="3.5" fill="none"/><path d="M92 2l14 8-14 8z" fill="{INK}"/></svg></div>""")
    body = f"""<div class="card">
      <div class="top"><span class="eyebrow">AWESOME LONG-VIDEO AGENT PAPERS</span><span class="stats">{n_papers} papers &nbsp;·&nbsp; {n_stages} stages &nbsp;·&nbsp; {n_cats} mechanisms</span></div>
      <h1>Beyond Passive Watching</h1>
      <p class="sub serif">A Comprehensive Survey of Agentic Systems for Long-Form Video Understanding</p>
      <div class="row">{"".join(boxes)}</div>
      <svg class="back" width="1312" height="64" viewBox="0 0 1312 64"><path d="M1189 0V44H123V6" stroke="{PURPLE}" stroke-width="3.5" stroke-dasharray="12 9" fill="none"/><path d="M113 14l10-14 10 14z" fill="{PURPLE}"/></svg>
      <div class="loop serif">verification feedback &nbsp;<i>v<sub>t+1</sub></i> &nbsp;·&nbsp; need more evidence, next cycle</div>
    </div>"""
    css = f"""
.card{{position:absolute;inset:2px;background:#fff;border:2px solid #d5dbe6;border-radius:26px;padding:34px 44px 0}}
.top{{display:flex;justify-content:space-between;font-size:18px;font-weight:700;letter-spacing:3px;color:{GRAY}}}
.stats{{letter-spacing:1.5px;font-weight:400}}
h1{{margin:18px 0 0;font-size:76px;line-height:1.05;letter-spacing:-2px;font-weight:700}}
.sub{{margin:8px 0 28px;font-size:33px;color:#4a4a4a}}
.row{{display:flex;align-items:center;justify-content:space-between;width:1312px}}
.box{{width:246px;height:262px;border:3.5px solid;border-radius:20px;padding:16px 18px}}
.head{{display:flex;align-items:center;gap:11px}} .name{{font-size:27px;font-weight:700}}
.dot{{width:34px;height:34px;border-radius:50%;color:#fff;font-size:20px;font-weight:700;display:flex;align-items:center;justify-content:center}}
.hint{{margin:6px 0 11px;font-size:18px;color:{GRAY};text-align:center}}
.inner{{height:140px;background:#fff;border:2.5px dashed;border-radius:14px;display:flex;align-items:center;justify-content:center}}
.inner img{{max-width:150px;max-height:104px}}
.arrow{{width:110px;text-align:center;margin-top:-16px}} .lab{{font-size:22px;line-height:1.15;margin-bottom:6px}} sub{{font-size:.7em}}
.back{{display:block;margin-top:6px}} .loop{{position:absolute;left:0;right:0;bottom:50px;text-align:center;font-size:25px;color:{PURPLE}}}"""
    return page(1400, 640, body, css), 1400, 640


def stage_card(stage_id, title, question, count, categories):
    p = PALETTE[stage_id]
    mech = "".join(f'<li><span style="background:{p["border"]}"></span>{escape(SHORT[c])}</li>' for c in categories)
    body = f"""<div class="c" style="background:{p['fill']};border-color:{p['border']}">
      <div class="num" style="background:{p['border']}"><b>{count}</b><small>papers</small></div>
      <h2>{escape(title)}</h2><p class="serif q">{escape(question)}</p>
      <div class="in" style="border-color:{p['border']}"><img src="{icon(p['icon'])}"><ul>{mech}</ul></div></div>"""
    css = f"""
.c{{position:absolute;inset:6px;border:3.5px solid;border-radius:22px;padding:24px 30px}}
h2{{margin:0;font-size:30px;font-weight:700;width:500px;line-height:1.1;white-space:nowrap}}
.q{{margin:8px 0 0;font-size:23px;font-style:italic;color:#555}}
.num{{position:absolute;right:26px;top:22px;width:82px;height:82px;border-radius:50%;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center}}
.num b{{font-size:34px;line-height:1}} .num small{{font-size:14px;margin-top:2px}}
.in{{position:absolute;left:30px;right:30px;bottom:26px;height:140px;background:#fff;border:2.5px dashed;border-radius:14px;display:flex;align-items:center;gap:22px;padding:0 24px}}
.in img{{width:112px;max-height:104px;object-fit:contain}}
ul{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:12px 14px;font-size:22px;flex:1}}
li{{display:flex;align-items:center;gap:9px;white-space:nowrap}} li span{{width:11px;height:11px;border-radius:50%;flex:none}}"""
    return page(660, 320, body, css), 660, 320


def stage_header(stage_id, question, count, n_cats):
    p = PALETTE[stage_id]
    body = f"""<div class="h" style="background:{p['fill']};border-color:{p['border']}">
      <div class="ic" style="border-color:{p['border']}"><img src="{icon(p['icon'])}"></div>
      <div class="q serif">{escape(question)}</div>
      <div class="cnt"><b style="color:{p['ink']}">{count} papers</b><span>{n_cats} mechanisms</span></div></div>"""
    css = f"""
.h{{position:absolute;inset:4px;border:3.5px solid;border-radius:20px;display:flex;align-items:center;gap:26px;padding:0 28px}}
.ic{{width:100px;height:78px;background:#fff;border:2.5px dashed;border-radius:12px;display:flex;align-items:center;justify-content:center}}
.ic img{{max-width:78px;max-height:60px}} .q{{flex:1;font-size:36px;font-style:italic;color:#2a2a2a}}
.cnt{{text-align:right;display:flex;flex-direction:column;gap:2px}} .cnt b{{font-size:32px}} .cnt span{{font-size:19px;color:{GRAY}}}"""
    return page(1400, 118, body, css), 1400, 118


def chrome():
    for name in ("google-chrome", "chromium", "chromium-browser", "google-chrome-stable"):
        if shutil.which(name):
            return name
    sys.exit("Chrome or Chromium is required to render the artwork.")


def shoot(browser, html, width, height, target, tmp):
    source = tmp / (target.stem + ".html")
    source.write_text(html)
    subprocess.run([browser, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars", "--force-device-scale-factor=2",
                    "--default-background-color=00000000", f"--window-size={width},{height + 200}", f"--screenshot={target}", source.as_uri()],
                   check=True, capture_output=True, timeout=120)
    # Headless Chrome's viewport is shorter than the requested window; render tall, then crop.
    with Image.open(target) as shot:
        shot.crop((0, 0, width * 2, height * 2)).save(target, optimize=True)


def prepare_figures(survey):
    """Export the manuscript figures used by the README: teaser panel (a) and the publication chart."""
    teaser = Image.open(survey / "files/new_teaser.png").convert("RGB")
    panel = teaser.crop((0, 0, teaser.width, 3092))
    ImageDraw.Draw(panel).rectangle((0, 3078, 450, 3092), fill="white")  # top edge of panel (b)'s label
    page = Image.new("RGB", (panel.width, panel.height + 20), "white")
    page.paste(panel, (0, 0))
    page.resize((2400, round(page.height * 2400 / page.width)), Image.LANCZOS).save(ROOT / "assets/survey-teaser.png", optimize=True)
    growth = Image.open(survey / "files/publication_growth_teaser.png").convert("RGB")
    growth.resize((1800, round(growth.height * 1800 / growth.width)), Image.LANCZOS).save(ROOT / "assets/publication-growth.png", optimize=True)
    print("wrote assets/survey-teaser.png and assets/publication-growth.png")


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "--survey":
        return prepare_figures(Path(sys.argv[2]))
    data = json.loads((ROOT / "data/catalog.json").read_text())
    papers = data["papers"]
    browser = chrome()
    jobs = {"banner.png": banner(len(papers), len(catalog.STAGES), sum(len(s[3]) for s in catalog.STAGES))}
    for stage_id, title, question, cats in catalog.STAGES:
        count = len(catalog.stage_papers(papers, stage_id))
        jobs[f"card-{stage_id}.png"] = stage_card(stage_id, title, question, count, [c[0] for c in cats])
        jobs[f"header-{stage_id}.png"] = stage_header(stage_id, question, count, len(cats))
    with tempfile.TemporaryDirectory() as tmp:
        for name, (html, width, height) in jobs.items():
            shoot(browser, html, width, height, ROOT / "assets" / name, Path(tmp))
            print("wrote assets/" + name)


if __name__ == "__main__":
    main()
