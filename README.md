# quarto-talk-template

Quarto formats for science talks and posters. Content is plain Markdown,
every figure is made by a script, and the look lives in the extension.

- **`talk-revealjs`**: slides. Clean, modern, neutral; the look lives in one
  file so a talk can switch to a branded variant
  ([nmfs-opensci/quarto-talk-template](https://github.com/nmfs-opensci/quarto-talk-template),
  planned) by changing one line. Example: `template.qmd`.
- **`poster-typst`**: a large-format PDF poster (42 × 42 in by default), via
  Typst, so no LaTeX. Example: `poster/poster.qmd`.

**See them:** <https://eeholmes.github.io/quarto-talk-template/> (slides) and
<https://eeholmes.github.io/quarto-talk-template/poster.pdf> (poster).

## Start a talk

A new repo or folder for one talk:

```bash
quarto use template eeholmes/quarto-talk-template
```

This copies the theme, the example deck (renamed to your folder's name), the
figure scripts and the Makefile.

A repo that already exists, e.g. one with several talks:

```bash
quarto add eeholmes/quarto-talk-template      # installs _extensions/eeholmes/talk/ and .../poster/
```

then copy `scripts/talk_style.py` (the figure-style shim) next to your figure
scripts and put `format: talk-revealjs` in each deck (`format: poster-typst`
for a poster). Run the same command again to update both formats.

Decks or posters in subfolders need a `_quarto.yml` at the top of the repo
(any project file will do; see this repo's), because Quarto looks for
`_extensions/` beside the document or at the project root.

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

## Posters

`poster/` is a complete example: `poster.qmd`, one script per figure in
`poster/scripts/`, and its own `Makefile` and `requirements.txt`.

```bash
cd poster
make            # run the figure scripts (incl. the QR code), then render poster.pdf
make poster     # render only
```

Write the poster in blocks that flow down columns:

```markdown
::: {.block title="Methods"}
Text, lists, citations [@key], and figures go inside a block.
:::

::: {.block .highlight title="Key Points"}
An accent-coloured block.
:::

::: {.colbreak}
:::

::: {.block title="References"}
::: {#refs}
:::
:::
```

- A block never splits across columns; `::: {.colbreak}` starts the next one.
- `![Caption.](figures/fig_x.png){#fig-x script="scripts/fig_x.py" width="100%"}`
  adds "Code: scripts/fig_x.py" to the caption, linked through `code-base-url`.
- Draw figures at printed size so their fonts match: one column of the default
  poster is 11.8 in wide (`COLUMN_WIDTH_IN` in `poster/scripts/poster_style.py`).
  Poster text is 32 pt; figure labels about 22–28 pt.
- YAML beyond Quarto's own: `qr` (an image) and `qr-caption` for the header
  (`scripts/qr_code.py` makes `figures/qr_code.svg` from `qr-url:`),
  `poster-footer`, `poster-columns` (3), `poster-width` / `poster-height`
  (42in), `fontsize` (32pt), `bibliographystyle` (a Typst/CSL style name).
- Colours are at the top of `_extensions/poster/typst-template.typ`. The poster
  uses Roboto, bundled in the extension; it does not yet share the talk's
  `brand.scss`.

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
| `_quarto.yml` | Makes the repo a Quarto project, so `poster/` (and talk folders) find `_extensions/` |
| `_extensions/poster/` | The poster format: Typst layout (`typst-template.typ`), YAML mapping (`typst-show.typ`), the block/colbreak/caption filter (`poster.lua`), Roboto (Apache-2.0) |
| `poster/` | Example poster with its figure scripts, Makefile and references |
| `scripts/` | Figure scripts and the `talk_style.py` shim |
| `figures/` | Output of `scripts/` |
| `scripts/qr_code.py` | Writes `figures/qr-repo.svg` from the deck's `repo:` |
| `skills/science-talk/SKILL.md` | Guide for coding agents: from abstract, notes and notebooks to a finished deck or poster |
| `.github/workflows/publish.yml` | Renders the deck and the poster on every PR (with a link check and a self-contained build) and publishes both to GitHub Pages on push to `main` |

## Agents

`skills/science-talk/SKILL.md` describes how a coding agent should build a talk
or a poster with these formats: decide which it is, brief, evidence ledger,
story (a spine of beats for a talk; a main message and block plan for a
poster), figure plan, draft, render and inspect the PDF. It is written to be installed as a Claude Code / Antigravity
skill, and agents working in a talk repo can be pointed at it directly.

## Reuse and citation

Template code is dedicated to the public domain under CC0 1.0 (see `LICENSE`);
use it however you like, no credit needed. The bundled fonts (Inter, Source Serif 4,
JetBrains Mono) are under the SIL Open Font License 1.1
(`_extensions/talk/talk-fonts/*-OFL.txt`); Roboto 2.138 is under Apache 2.0
(`_extensions/poster/fonts/`). The poster format comes from the AGU26 poster in
[fish-pace/2026-go-bgc-hackweek](https://github.com/fish-pace/2026-go-bgc-hackweek). `skills/science-talk/SKILL.md`
adapts parts of [alfredo-hs/quarto-talks](https://github.com/alfredo-hs/quarto-talks) (MIT).
