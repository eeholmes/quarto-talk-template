---
name: science-talk
description: Build or revise a science talk as a Quarto revealjs deck using the talk theme (format talk-revealjs or nmfs-talk-revealjs), starting from an abstract plus the project's working material — notes, discussion threads, issues, and Jupyter notebooks. Use when asked to plan, outline, draft, storyboard, or finish slides for a talk, to turn notebook analyses into talk figures, or to check a deck before it is presented.
---

# Science talk

A talk is an argument with evidence, given out loud to people who cannot
scroll back. This skill turns a project's working material into a deck that
renders with the talk theme, where every figure comes from a script and every
claim can be traced to its source.

The theme's own markup and build commands are in the template README
(`eeholmes/quarto-talk-template`). This file is about the decisions.

## Ground rules

1. **Never invent a result.** No number, trend, model score, figure,
   citation, or quotation that is not in the source material or produced by
   code you ran. If something the story needs does not exist yet, write it as
   an open item (see the evidence ledger), not as a slide claim.
2. **The source of truth is the project, not your summary of it.** Notebooks
   and notes change during a project; the abstract was written before the
   work was done. When they disagree, say so and ask which is current.
3. **The talk is presented from a PDF** unless the user says otherwise. Do not
   depend on animations, fragments that reveal content step by step, video,
   hover, or live code. Everything a slide needs must be visible in its final
   state.
4. **Ask only what changes the talk.** Make a conservative assumption about
   anything else and record it in the notes.

## Inputs to look for

Read before drafting, and list what you read in the talk's notes file:

| Source | Where it usually is | What to take from it |
|---|---|---|
| Abstract | user message, `abstract.md`, a submission system | the promise the talk must keep; its key claims |
| Working notes | `claude/notes/`, `notes/`, `docs/`, meeting notes | decisions, caveats, what was tried and dropped |
| Discussion threads | GitHub issues and Discussions, PR descriptions, pasted chat | open questions, disagreements, who did what |
| Notebooks | `*.ipynb` in the project repo or contributor folders | results, figures, the code and data behind them |
| Existing slides or posters | `.pptx`, `.pdf`, `poster/` | figures and wording already shown publicly |

For a notebook, record the path, the commit, and the cells that produce each
result you use. Read outputs as well as code; an output may be stale, so prefer
re-running the cell (or the extracted script) to trusting a saved output.

## Workflow

### 1. Brief

Establish, from the request or by asking:

- audience and what they already know (domain scientists, data scientists, managers);
- length and format (a 20-minute talk with 5 minutes of questions is 15–20 slides);
- presenters and who speaks which part;
- date, venue, and whether the deck must be shared before or after;
- the one sentence the audience should leave with.

Write this at the top of the talk's notes file, `<talk>/NOTES.md` in the talk
repo (create it if missing).

### 2. Evidence ledger

Before writing any slide, build a table in `NOTES.md` of the claims the talk
could make:

| Claim | Evidence | Source | Status |
|---|---|---|---|
| U-Net beats DINEOF on held-out gaps | RMSE table | `notebooks/eval.ipynb` cells 12–14 @ `abc123` | settled |
| Errors grow near the coast | maps only, no metric | issue #41 | tentative |
| Works for multi-variable input | not run | abstract | **open** |

Status is `settled` (reproducible result), `tentative` (shown but not checked or
still under discussion), or `open` (promised or hoped for, no result yet).
Slides make firm claims only from `settled` rows. A `tentative` row can appear
with its caveat said on the slide. An `open` row is either cut, framed as next
steps, or flagged to the user before the talk — never presented as a finding.

Check the abstract against the ledger and tell the user plainly about any
promise the evidence does not yet support.

### 3. Spine

Write the argument as a short list of beats, each with one job: the problem,
why it matters, the question, the approach, the main evidence, what it means,
what is next. Not every talk needs every beat, and a beat is not automatically
one slide. For a 20-minute talk aim for 15–20 slides; above 24, cut.

Prefer one decisive result shown well over a catalogue. Move robustness checks,
alternative models, and long tables to backup slides after the closing slide.

### 4. Figure plan

For each beat that needs evidence, decide the figure before drawing it, and
add it to a figure table in `NOTES.md`:

| Figure | What the audience should see | Data | From notebook | Script | Status |
|---|---|---|---|---|---|

Then make each one:

- One script per figure in `scripts/fig_*.py`, starting from
  `from talk_style import apply_style, FULL, HALF, WIDE, SERIES`.
- Port the plotting code from the notebook; do not screenshot notebook output.
- Slow steps (loading cloud data, running a model) go in a separate compute
  script that writes a small file to `data/`; the figure script reads only
  that. The docstring of each script names the source notebook, commit, and
  data source.
- Draw at slide size (`FULL`, `HALF`, `WIDE`) so text is readable from the back
  of the room. Direct labels instead of legends where possible. No figure
  title if the slide title already says it.
- Never change what the evidence shows when redrawing it — same data, units,
  uncertainty, and filtering as the source.
- Run each script and look at the PNG before using it.

### 5. Draft the deck

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
Cite sources on the slide with `::: {.refs}` or a references slide.

Writing on slides: plain, direct sentences. Avoid slogan-like phrasing,
stacked colons in titles, "not X but Y" constructions, and generic presentation
language. Units on every number.

### 6. Render and inspect

```bash
make figures   # scripts → figures/
make slides    # deck HTML
make pdf       # the file that will be presented
```

Look at every page of the PDF (rasterise pages or screenshot slides if you
cannot open it). Check:

- nothing clipped, overflowing, or overlapping the footer;
- text, axis labels, and table entries readable at projection size;
- each figure's point visible in a few seconds;
- a run of three or more slides with the same layout — vary or cut;
- claims on slides match the evidence ledger's status;
- the closing slide's QR code and links point to the right repo;
- slide count against the time budget.

Fix by editing content first (cut, split, shorten) and by CSS only as a last
resort. Never shrink core content below `.small` to make it fit.

### 7. Hand off

Report: the PDF and HTML paths, the commands run and their result, the
sources used, any `tentative` or `open` items still on slides, figures not yet
reproducible from a script, and anything you assumed. Update `NOTES.md` so the
next session can pick up.

---

Parts of the structure and the inspection checklist are adapted from
[alfredo-hs/quarto-talks](https://github.com/alfredo-hs/quarto-talks) (MIT).
