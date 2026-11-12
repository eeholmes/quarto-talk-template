---
name: science-talk
description: Build or revise a science talk (Quarto revealjs deck, format talk-revealjs or nmfs-talk-revealjs) or a science poster (Quarto Typst poster, format poster-typst) from an abstract plus the project's working material — notes, discussion threads, issues, and Jupyter notebooks. Use when asked to plan, outline, storyboard, draft, or finish slides or a poster, to turn notebook analyses into talk or poster figures, or to check a deck or poster before it is presented or printed.
---

# Science talk or poster

A talk and a poster are both arguments with evidence, built from the same
project material, but they are used differently:

| | Talk | Poster |
|---|---|---|
| Who controls the pace | the speaker | the reader |
| Without the presenter | meaningless | must stand on its own |
| Time with the audience | 10–45 min, everyone at once | 1–3 min per reader, often 5–10 with you there |
| How much it holds | one idea per slide; detail goes in what you say | more: data, methods, sample sizes, references, all on the page |
| Order | a sequence the audience can't skip | blocks in columns; readers jump to the title, Key Points, and the figures |
| Afterwards | slides shared as a PDF | photographed and kept as a record |

**Decide which you are making first.** "Poster", "poster session", a board
size, or AGU/OSM/ASLO-style poster sessions mean a poster. "Talk",
"presentation", "slides", "seminar", or a time slot mean a talk. If it is
unclear, ask. If both are wanted, build the evidence ledger and figures once
and tell each story separately.

The formats' markup and build commands are in the template README
(`eeholmes/quarto-talk-template`). This file is about the decisions.

## Ground rules (both)

1. **Never invent a result.** No number, trend, model score, figure,
   citation, or quotation that is not in the source material or produced by
   code you ran. If the story needs something that does not exist yet, write
   it as an open item in the evidence ledger, not as a claim.
2. **The source of truth is the project, not your summary of it.** Notebooks
   and notes change during a project; the abstract was written before the
   work was done. When they disagree, say so and ask which is current.
3. **Static output.** Talks are presented from the PDF unless the user says
   otherwise, and posters are printed. Do not depend on animation,
   step-by-step reveals, video, hover, or live code.
4. **Ask only what changes the result.** Make a conservative assumption about
   anything else and record it in the notes.

## Inputs to look for (both)

Read before drafting, and list what you read in the notes file:

| Source | Where it usually is | What to take from it |
|---|---|---|
| Abstract | user message, `abstract.md`, a submission system | the promise the talk or poster must keep; its key claims |
| Working notes | `agent/`, `docs/design/`, `claude/notes/`, `notes/`, meeting notes | decisions, caveats, what was tried and dropped |
| Discussion threads | GitHub issues and Discussions, PR descriptions, pasted chat | open questions, disagreements, who did what |
| Notebooks | `*.ipynb` in the project repo or contributor folders | results, figures, the code and data behind them |
| Earlier slides or posters | `.pptx`, `.pdf`, `poster/` | figures and wording already shown publicly |

For a notebook, record the path, the commit, and the cells that produce each
result you use. Read outputs as well as code; an output may be stale, so prefer
re-running the cell (or the extracted script) to trusting a saved output.

## Workflow

### 1. Brief

Establish, from the request or by asking, and write at the top of
`NOTES.md` in the talk's or poster's folder (create it if missing):

- audience and what they already know;
- **talk:** length and question time; presenters and who speaks which part;
  date and venue; whether slides are shared before or after;
- **poster:** meeting, session, date and time; **board size and orientation
  from the meeting's rules** (e.g. AGU: max 44 × 44 in, boards shared, so the
  template's 42 × 42 in); whether it is also shown as an e-poster or a short
  oral "lightning" pitch; who stands at it;
- the one sentence the audience should leave with.

### 2. Evidence ledger (both)

Before writing any slide or block, build a table in `NOTES.md` of the claims
you could make:

| Claim | Evidence | Source | Status |
|---|---|---|---|
| U-Net beats DINEOF on held-out gaps | RMSE table | `notebooks/eval.ipynb` cells 12–14 @ `abc123` | settled |
| Errors grow near the coast | maps only, no metric | issue #41 | tentative |
| Works for multi-variable input | not run | abstract | **open** |

Status is `settled` (reproducible result), `tentative` (shown but not checked
or still under discussion), or `open` (promised or hoped for, no result yet).
Firm claims come only from `settled` rows. A `tentative` row appears with its
caveat **written on the slide or poster**, not only said aloud — a poster is
read and photographed when you are not there. An `open` row is cut, framed as
next steps, or flagged to the user — never presented as a finding.

Check the abstract against the ledger and tell the user plainly about any
promise the evidence does not yet support.

### 3. The story

**Talk — a spine of beats.** The problem, why it matters, the question, the
approach, the main evidence, what it means, what is next. A beat is not
automatically one slide. For a 20-minute talk aim for 15–20 slides; above 24,
cut. Prefer one decisive result shown well over a catalogue; robustness
checks, alternatives and long tables go to backup slides after the closing
slide.

**Poster — a main message and a block plan.** Write the main message (two
sentences at most), then plan the blocks in reading order in a table:

| Block | Content | Figure | Source / new work |
|---|---|---|---|

Layout rules for the plan:

- **Title states the finding**, not the topic. It is the most-read text on
  the poster.
- **Key Points first** (top of the first column, `.highlight` block): the 3
  findings a reader who stops there should take away.
- Then context (Introduction, Objectives), what was done (Data, Methods), the
  evidence (Results — usually the largest share of the area, mostly figures),
  and the close (Conclusions, Next Steps, References, Acknowledgements).
- Reading order is down each column, left to right; plan where each
  `::: {.colbreak}` goes so no block is stranded at a column bottom.
- **Budget:** about 500–800 words of body text in total, 3–6 figures, no block
  over ~120 words. More than a talk carries, far less than a paper: methods
  detail that a talk would say aloud must be on the poster, but compressed.
- **Uncertainty and sample sizes on the page** (n, intervals, what "coastal"
  means) — the reader cannot ask.
- Note a 1-minute and a 3-minute spoken walkthrough in `NOTES.md` for when you
  are standing at the board.

### 4. Figure plan (both)

For each beat or block that needs evidence, decide the figure before drawing
it, and add it to a figure table in `NOTES.md`:

| Figure | What the reader should see | Data | From notebook | Script | Status |
|---|---|---|---|---|---|

Then make each one:

- One script per figure in `scripts/fig_*.py`. Talk: start from
  `from talk_style import apply_style, FULL, HALF, WIDE, SERIES`. Poster: from
  `poster_style` (`COLUMN_WIDTH_IN`, `DPI`, `apply_style`).
- Port the plotting code from the notebook; do not screenshot notebook output.
- Slow steps (loading cloud data, running a model) go in a separate compute
  script that writes a small file to `data/`; the figure script reads only
  that. Each script's docstring names the source notebook, commit, and data.
- **Draw at the size it is shown**, so the font sizes in the script are what
  people see. Talk: `FULL`/`HALF`/`WIDE` at slide size. Poster: one column is
  `COLUMN_WIDTH_IN` (11.8 in on the default 42 in poster) at 300 dpi; body text
  is 32 pt, so figure labels are about 22–28 pt.
- Direct labels instead of legends where possible. Talk: no figure title if
  the slide title says it. Poster: the caption states the takeaway in a full
  sentence, because no one is there to say it.
- Never change what the evidence shows when redrawing it — same data, units,
  uncertainty, and filtering as the source.
- Run each script and look at the image before using it.

### 5a. Draft the deck (talk)

Start from the template deck's YAML header (`format: talk-revealjs`, `repo:`,
`footer:`, `headings:`). Write informative slide titles; a title that states
the finding is usually better than a topic label. Choose the slide form by
purpose:

| Form | Markup | Use for |
|---|---|---|
| Ordinary slide | `## Title` | explanation, short lists (≤ 3–5 short bullets) |
| Section divider | `# Title` | a real change of phase; 2–4 per talk at most |
| Statement | `## The claim {.statement}` | one claim the audience must keep |
| Question | `## The question? {.question}` | a question the talk then answers |
| Visual | `## Title {.visual}` + one figure | primary evidence, full size |
| Figure + text | `:::: {.columns}` | a result beside what explains it |
| Big numbers | `::: {.stats}` | two or three headline numbers |
| Take-away box | `::: {.takeaway}` | the conclusion of a dense slide |
| Quote | `## {.quote}` + `>` + `{.quote-source}` | exact wording that matters, with source |
| Math | `## Title {.math}` | one equation, symbols defined below it |
| Code | `## Title {.code}` | a short excerpt (≤ 12 lines) that teaches one step |
| Closing | `## Thank you {.dark .closing}` + `::: {.qr}` | contact, slides link, repo QR code |

Every figure gets `fig-alt` text and `script="scripts/fig_x.py"` so its caption
links to the code. Put what you will say, and who says it, in `::: notes`.
Cite sources with `::: {.refs}` or a references slide.

### 5b. Draft the poster

Start from the template's `poster/poster.qmd` (`format: poster-typst`). Fill
the YAML: title, authors with `- ref:` affiliations, `qr-url` / `qr` /
`qr-caption`, `poster-footer` (meeting, session, board, contact),
`code-base-url`, `bibliography`, and size keys if the board differs. Then
write the blocks from the block plan:

- `::: {.block title="..."}` per block; `.highlight` for Key Points only.
- `::: {.colbreak}` where the plan breaks columns.
- Figures with `#fig-` ids, `script="scripts/fig_x.py"`, `width="100%"`, and
  referred to in the text as `@fig-x`.
- Short paragraphs and bullets; full sentences in captions.
- References in a block containing `::: {#refs}`; keep to the few that matter.

Writing (both): plain, direct sentences. Avoid slogan-like phrasing, stacked
colons in titles, "not X but Y" constructions, and generic presentation
language. Units on every number.

### 6. Render and inspect

**Talk:**

```bash
make figures   # scripts → figures/
make slides    # deck HTML
make pdf       # the file that will be presented
```

Look at every page of the PDF (rasterise pages or screenshot slides if you
cannot open it). Check: nothing clipped or overlapping the footer; text and
labels readable at projection size; each figure's point visible in a few
seconds; no run of three or more slides with the same layout; claims match
the ledger; the QR code points to the right repo; slide count fits the time.

**Poster:**

```bash
cd poster && make   # figure scripts (incl. QR code), then poster.pdf
```

Rasterise the whole poster to see the layout, then crops at 100% to check
text. Check: page size matches the board; no block overflowing its column or
the page bottom, and no big empty column bottoms; body text ≥ 24 pt and figure
labels legible from about 2 m (≈ 20 pt or more at print size); figures sharp
at print size (≥ 150 dpi); the title and Key Points alone tell the story;
every caption states its takeaway; claims and caveats match the ledger; the QR
code scans to the right URL; footer has the session, board number and contact.

Fix by editing content first (cut, split, shorten). Never shrink core text
below readable size to make it fit.

### 7. Hand off

Report: the output paths (PDF, and HTML for a talk), the commands run and
their result, the sources used, any `tentative` or `open` items still shown,
figures not yet reproducible from a script, and anything you assumed. Update
`NOTES.md` so the next session can pick up.

---

Parts of the talk structure and the inspection checklist are adapted from
[alfredo-hs/quarto-talks](https://github.com/alfredo-hs/quarto-talks) (MIT).
The poster story format follows the AGU26 poster in
[fish-pace/2026-go-bgc-hackweek](https://github.com/fish-pace/2026-go-bgc-hackweek)
(`poster/STORY.md`).
