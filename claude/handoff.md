# Handoff: quarto-talk-template

Eli's personal Quarto templates: talk slides (`talk-revealjs`, neutral, modern,
science) and, from PR #3, posters (`poster-typst`, Typst, from the AGU26 poster). Design
decisions, and the traps behind odd-looking code, are in
`claude/notes/design.md` — read it before changing the theme.

## Next work: issues #4 and #5 (planned 2026-11-24)

- **#4** is the plan for the skill, renamed `science-talk-poster`: guided
  intake; storyline phases A–D (the user's own words → collect and analyse
  → findings menu → 2–4 storyline options, never one); `storyline-plan.md`
  and a separate, shareable `terms-and-style.md`; starter deck and poster;
  poster fixes from the AGU26 poster; free-form slides built from a
  description or sketch (8c). It has an **Order of work** section: the skill
  (storyline etc.) and the poster fixes can start now.
- **Talk engine is undecided** (revealjs vs a hand-written Typst slide
  format like the poster's). Eli felt stuck in a generic revealjs look and
  liked the control she had over the Typst poster. Decided by a comparison
  once #5 has about 3–5 reference talks; soft deadline early January 2027.
- **#5** collects reference talks and slides Eli likes (PDFs, screenshots,
  phone photos) in a gitignored `reference-talks/`; the agent writes a
  design note and draws wireframes, with no copies of others' slides in the
  repo, then Eli deletes the files.
- `example_science_talk.pdf` (someone else's talk; untracked) may still be
  in the repo root: never commit it; Eli is removing it.
- Real deadlines: AMS 2027 poster Jan 13, eScience talk Jan 21
  (SAFS-Varanasi-Internship/mindthegap-talks #2, #1).

## State (2026-11-12)

- v0.1 merged (PR #1). Example deck published at
  https://eeholmes.github.io/quarto-talk-template/ ; every PR runs a render,
  a local-link check and a standalone build.
- Extension `_extensions/talk/` (format `talk-revealjs`): slide types
  `.statement/.question/.visual/.quote/.math/.code/.dark/.closing`, blocks
  `.takeaway/.stats/.qr/.refs`; YAML `repo:`, `headings: sans|serif`
  (default sans, Eli's choice), `kicker`, `event`, `talk-url`. Footer is
  Quarto's own `footer:` (`"{{< meta repo >}}"` for the repo).
- Builds: `make figures | slides | pdf | standalone`. Eli usually presents
  from the PDF.
- `skills/science-talk/SKILL.md` is installed on the hub through
  `~/claude-config/common/skills.txt` (bootstrap links it from this checkout,
  so keep the checkout on `main`).
- Poster format (PR #3): example in `poster/`; the repo root `_quarto.yml` is
  what lets subfolder documents find `_extensions/`. Poster does not yet
  share `brand.scss`.
- Not checked: the Mermaid slide (hub Chromium 91 is too old); Eli to look in
  a real browser.

## Working principles

- Colours and fonts only in `brand.scss`; `talk.scss`, `talk.lua`,
  `title-slide.html` must stay identical in the NMFS variant so decks switch
  by changing `format:`.
- Verify by rendering and looking at screenshots/PDF pages, not by reading CSS.
  Screenshot recipe: Quarto's Chromium at
  `~/.local/share/quarto/chromium/*/chrome-linux/chrome --headless
  --screenshot ... "file://…/template.html#/<slide-id>"`.

## Related

- `nmfs-opensci/quarto-talk-template`: NMFS-branded variant, not started.
  Replace `brand.scss`, the colours/fonts in `talk_style.py`, `talk-dark-bg`
  in `_extension.yml`, and add a logo.
- `SAFS-Varanasi-Internship/mindthegap-talks`: created by Eli, empty (README,
  LICENSE). First real use: a 20-minute eScience Institute talk on Mind the
  Gap. Eli will open an issue there to start it.
- This repo uses the older `claude/` notes layout (created just before Eli's
  switch to `agent/` + `docs/design/`); fine to keep, move only if Eli asks.
