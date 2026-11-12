# Handoff: quarto-talk-template

Eli's personal Quarto revealjs talk theme (neutral, modern, science). Built
2026-11-12 on branch `initial-template`. Design decisions and the reasons for
them are in `claude/notes/design.md`.

## State

- Extension `_extensions/talk/` (format `talk-revealjs`), example deck
  `template.qmd`, two example figure scripts, Makefile, Pages workflow.
- Renders on the hub with Quarto 1.7.34. Figure scripts run in a clean venv
  from `requirements.txt` alone.
- Checked by eye: screenshots of every slide and the PDF (Chromium 91 from
  `quarto install chromium`). Mermaid slide not checked: that Chromium is too
  old for Mermaid; Eli to check in a real browser.
- Pages enabled by Eli (2026-11-12); publishes on merge to `main`. PRs get a
  render + link-check + self-contained build.
- Second round added: `.question/.quote/.visual/.math/.code/.closing`,
  `headings: sans|serif`, `repo:` + `::: {.qr}`, `make standalone`, and
  `skills/science-talk/SKILL.md`. Default heading face: sans (Eli, 2026-11-12).

## Related

- `nmfs-opensci/quarto-talk-template`: NMFS-branded variant, not started. It
  should replace only `brand.scss`, `talk_style.py` colours/fonts, and add a logo.
- `SAFS-Varanasi-Internship/mindthegap-talks`: first real use (eScience talk).
