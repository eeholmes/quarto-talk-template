# Agent instructions

Edit `AGENTS.md`, not `CLAUDE.md` (which only contains `@AGENTS.md`).

This repo is Eli Holmes's personal Quarto revealjs talk template. Read
`claude/handoff.md` first, then `README.md`.

## Rules for changing the theme

- **Colours and fonts go in `_extensions/talk/brand.scss` only.** `talk.scss`
  uses `$talk-*` variables and no literal colours, so the NMFS-branded variant
  (`nmfs-opensci/quarto-talk-template`) can replace `brand.scss` alone and keep
  every class working. A deck must render in either variant by changing
  `format:`.
- **Keep `talk_style.py` in step with `brand.scss`** (ink, accent, fonts).
- **New markup goes in both variants** or it breaks the switch. Document it in
  the README "Writing slides" block and show it in `template.qmd`.
- **Changing the series palette:** re-run a colour-blind check on the new list
  before committing; the current one passes adjacent-pair CVD ΔE ≥ 8 and 3:1
  contrast on white.

## Building a talk with this theme

Follow `skills/science-talk/SKILL.md`.

## Verifying

Render `template.qmd` and look at the slides, not just the HTML. Run the figure
scripts in a clean venv with only `requirements.txt` installed.
