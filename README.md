# quarto-talk-template

A Quarto revealjs theme for science talks: clean, modern, neutral. Slides are
plain Markdown, every figure is made by a script, and the look lives in one
file so a talk can switch to a branded variant
([nmfs-opensci/quarto-talk-template](https://github.com/nmfs-opensci/quarto-talk-template),
planned) by changing one line.

**See it:** render `template.qmd`, or the published copy once Pages is on.

## Start a talk

A new repo or folder for one talk:

```bash
quarto use template eeholmes/quarto-talk-template
```

This copies the theme, the example deck (renamed to your folder's name), the
figure scripts and the Makefile.

A repo that already exists, e.g. one with several talks:

```bash
quarto add eeholmes/quarto-talk-template      # installs _extensions/eeholmes/talk/
```

then copy `scripts/talk_style.py` (the figure-style shim) next to your figure
scripts and put `format: talk-revealjs` in each deck. Run the same command
again to update the theme.

## Build

You need [Quarto](https://quarto.org) 1.6 or later. For the figure scripts,
also the Python packages in `requirements.txt`.

```bash
pip install -r requirements.txt   # once
make                              # run the figure scripts, then render
make slides                       # render only, using the figures already in figures/
make preview                      # live preview while editing
make pdf                          # PDF copy via headless Chrome (`quarto install chromium` if needed)
make standalone                   # one self-contained HTML (~10 MB) that works offline
```

Figures are committed, so the slides render without rerunning slow scripts and
the GitHub Action needs only Quarto. Rendered HTML and PDF are not committed.

## Writing slides

```markdown
# Section title                      dark divider slide

## Slide title                       normal slide; ::: notes ... ::: for speaker notes

## Closing {.dark}                   any slide on the dark background

## The claim {.statement}            one claim, large and centred; optional line under it
## The question? {.question}         a question the talk will answer
## Title {.visual}                   one figure as the slide's evidence, full size
## Title {.math}                     one equation, centred and large
## Title {.code}                     a short code excerpt, shown larger
## {.quote}                          > quotation, then [Source, year]{.quote-source}
## Thank you {.dark .closing}        closing slide; a ::: {.qr} block sits on the right

::: {.qr}                            QR code for repo:, with the link under it
:::

![Caption.](figures/fig_x.png){script="scripts/fig_x.py" fig-alt="..."}
                                     caption gets "Code: scripts/fig_x.py", linked
                                     via code-base-url in the YAML header

::: {.takeaway}                      accent box for the slide's conclusion
:::

::: {.stats}                         row of big numbers
[42%]{.stat} label text

[3×]{.stat} label text
:::

::: {.refs}                          small citation line pinned to the slide bottom
:::

[text]{.lead}  [text]{.small}  [text]{.muted}  [text]{.accent}  [text]{.hl}
```

Columns, callouts, code blocks, Mermaid diagrams, tables and `::: notes` are
standard Quarto and are styled to match. Press **S** for the speaker view.

YAML fields beyond Quarto's own:

| Field | What it does |
| --- | --- |
| `repo: github.com/org/repo` | The talk's repository. Feeds the `::: {.qr}` block, and caption "Code:" links (unless `code-base-url` is set) |
| `footer:` | Quarto's own footer. Leave out for none; `"{{< meta repo >}}"` or `"{{< meta title >}}"` for the repo or title; or any text |
| `headings: sans` / `serif` | Heading face: Inter Display or Source Serif 4 Display. Body text is Inter either way |
| `kicker` | Small uppercase line above the title (series or event name) |
| `event`, `talk-url` | Shown on the title slide (`talk-url` without `https://`) |
| `code-base-url` | Prefix for caption "Code:" links, if not derived from `repo:` |

Authors and `affiliations` use Quarto's normal author schema and are numbered
automatically. The QR code image is made by `scripts/qr_code.py` (run by
`make figures`) from `repo:`.

## Figures

Each figure has its own script in `scripts/` that writes a PNG to `figures/`.
Scripts start with

```python
from talk_style import FULL, HALF, WIDE, SERIES, apply_style
apply_style()
fig, ax = plt.subplots(figsize=FULL)
```

`talk_style` sets Inter, the theme's colours and a colour-blind-safe series
palette (validated; use the colours in order and fold anything past six into
"Other"). `FULL`, `HALF` and `WIDE` are drawn at the size they appear on a
1600 × 900 slide, so font sizes match the slide text.

## Switching between this theme and a branded one

Both variants use the same markup, so a deck written for one renders in the
other. Install both and change the format:

```yaml
format: talk-revealjs        # this theme
format: nmfs-talk-revealjs   # NMFS-branded variant
```

and rebuild figures with the matching style: `make figures TALK_THEME=nmfs-talk`.

## Files

| Path | What it is |
| --- | --- |
| `template.qmd` | Example deck that shows every layout |
| `_extensions/talk/brand.scss` | All colours and fonts. The only file a branded variant replaces |
| `_extensions/talk/talk.scss` | Layout and components; uses only `brand.scss` variables |
| `_extensions/talk/talk.lua` | Dark section slides, and the caption "Code:" link |
| `_extensions/talk/title-slide.html` | Title-slide layout |
| `_extensions/talk/talk_style.py` | Matplotlib style matched to `brand.scss` |
| `_extensions/talk/talk-fonts/`, `mpl-fonts/` | Inter, Source Serif 4 and JetBrains Mono (SIL OFL 1.1, licences included), bundled so talks look the same offline |
| `scripts/` | Figure scripts and the `talk_style.py` shim |
| `figures/` | Output of `scripts/` |
| `scripts/qr_code.py` | Writes `figures/qr-repo.svg` from the deck's `repo:` |
| `skills/science-talk/SKILL.md` | Guide for coding agents: from abstract, notes and notebooks to a finished deck |
| `.github/workflows/publish.yml` | Renders the deck on every PR (with a link check and a self-contained build) and publishes to GitHub Pages on push to `main` |

## Agents

`skills/science-talk/SKILL.md` describes how a coding agent should build a talk
with this theme: brief, evidence ledger, spine, figure plan, draft, render and
inspect the PDF. It is written to be installed as a Claude Code / Antigravity
skill, and agents working in a talk repo can be pointed at it directly.

## Reuse and citation

Template code is dedicated to the public domain under CC0 1.0 (see `LICENSE`);
use it however you like, no credit needed. The bundled fonts (Inter, Source Serif 4,
JetBrains Mono) are under the SIL Open Font License 1.1
(`_extensions/talk/talk-fonts/*-OFL.txt`). `skills/science-talk/SKILL.md`
adapts parts of [alfredo-hs/quarto-talks](https://github.com/alfredo-hs/quarto-talks) (MIT).
