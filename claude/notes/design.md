# Design decisions (Eli, 2026-11-12)

- **Quarto revealjs**, not PowerPoint, MyST or xaringan: plain text under
  version control, figures from scripts, speaker notes, publishes to Pages.
- **Talks live in per-project talk repos** (e.g. `mindthegap-talks`), never in
  the technical repo, and not one repo for all talks: GitHub access is per
  repo and Eli often adds collaborators.
- **Two variants, same markup.** Eli switches between a neutral look and NOAA
  branding. `brand.scss` holds every colour/font; `talk.scss`, `talk.lua` and
  `title-slide.html` must stay identical across variants so a deck switches by
  changing `format:`.
- **Figure workflow copies the AGU26 poster** (`fish-pace/2026-go-bgc-hackweek/poster`):
  one script per figure, shared style module, `make figures` separate from
  rendering, figures committed, caption links to the script.

## Things that look odd but are deliberate

- `talk.lua` runs `at: pre-ast`; later, Quarto has replaced figures with its own
  node type and the "Code:" caption link silently disappears (learned on the poster).
- Dark slides get reveal's `data-background-color` from `talk-dark-bg` in
  `_extension.yml` (duplicating `$talk-section-bg` in `brand.scss`; keep them
  equal). An earlier version coloured the page body through `data-state`, which
  looked right on screen but made every page dark in PDF: in print mode reveal
  leaves the last slide's state on the body. `data-state="talk-dark"` is still
  set, only to recolour the footer and slide number.
- The title slide gets `data-state="talk-titlepage"` (added in `talk.lua`) so
  CSS can hide the footer, slide number and menu button there.
- Quarto moves a heading's classes onto the slide `<section>`, so CSS targets
  `section.talk-section > h1`, not `h1.talk-section`.
- Web fonts are in `talk-fonts/` (copied next to the rendered HTML by
  `format-resources`, which copies a folder whole); the TTFs for matplotlib are
  in `mpl-fonts/` so they are not copied into every deck. `format-resources`
  with individual files flattens them into the deck folder, hence the folder.
- Rendering a deck leaves a `talk-fonts/` folder beside it; it is gitignored.
- Series palette `#00809A #D9732B #5A4FC4 #42A35E #C2417A #9C7A00` was chosen
  with a colour-blind validator: adjacent-pair CVD ΔE ≥ 8.2, all ≥ 3:1 on
  white. The green had to sit between violet and magenta; next to ochre or
  magenta in other orders it failed.
- On the hub, `quarto render ... --output-dir _site` prints an error removing
  `.quarto/` after the output is written; the output is complete.
- `make pdf` uses headless Chrome's print-to-PDF on `?print-pdf`, not
  decktape: decktape could not be installed on the hub. Output is 13 pages at
  16:9, checked by eye.
- Screenshots on the hub come from Quarto's Chromium 91 (`quarto install
  chromium`). It is too old for Mermaid 11 (no `structuredClone`), so Mermaid
  slides show the source there; check them in a current browser.
  `mermaid-format: svg` also failed to render on the hub.

## Added 2026-11-12 (second round, from alfredo-hs/quarto-talks)

- **Eli's usual input** is an abstract plus ongoing notes, discussion threads
  and Jupyter notebooks; `skills/science-talk/SKILL.md` is built around that
  (evidence ledger with settled / tentative / open claims, figure plan that
  ports notebook plots to scripts).
- **Talks are usually presented from the PDF**, so the skill bans reliance on
  fragments, animation, video or live code. `make standalone` (one offline
  HTML) is an option, not the default.
- **Heading face: sans (Inter Display) is the default**, chosen by Eli after
  comparing both on 2026-11-12. A deck can still set `headings: serif`
  (Source Serif 4 Display); `$talk-headings-default` in `brand.scss` sets the
  default.
- **Footer** is Quarto's own `footer:`. A filter cannot change it (Quarto
  reads it before any Lua filter runs, even `pre-ast`), so use the meta
  shortcode: `footer: "{{< meta repo >}}"`.
- **QR code** comes from `scripts/qr_code.py` (segno) reading `repo:`; the
  `::: {.qr}` div is filled in by `talk.lua`. Committed as `figures/qr-repo.svg`.
- **Maths uses KaTeX**, not MathJax: with MathJax, `embed-resources` +
  `self-contained-math` still loaded MathJax from a CDN and showed raw TeX
  offline. KaTeX embedded correctly (checked with networking blocked).
- **Font names must stay quoted** in the CSS variables (`inspect()` in
  `talk.scss`): Sass drops the quotes and an unquoted `Source Serif 4 Display`
  is invalid CSS, so the serif silently fell back to sans.
