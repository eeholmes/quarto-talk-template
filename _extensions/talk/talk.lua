-- talk.lua — small additions to Quarto revealjs for the talk theme.
--
--   headings: serif | sans          (YAML) heading face; default set in brand.scss
--   # Section title                 a dark section-divider slide (automatic)
--   ## Slide title {.dark}          any slide on the dark background
--   ![Caption](figures/x.png){script="scripts/x.py"}
--                                   appends "Code: scripts/x.py" to the caption,
--                                   linked to code-base-url + path
--   repo: github.com/org/repo       (YAML) the talk's repository, shown without https://
--   ::: {.qr}                       QR code for repo (figures/qr-repo.svg, made by
--   :::                             scripts/qr_code.py) with the link under it
--
-- Dark slides get reveal's background-color (so they print to PDF correctly)
-- from talk-dark-bg in _extension.yml, plus data-state="talk-dark" so CSS can
-- recolour the footer and slide number.

local code_base_url = ""
local dark_bg = "#0F1C26"
local repo = nil          -- "github.com/org/repo"
local qr_file = "figures/qr-repo.svg"

local function repo_link()
  local url = repo:match("^https?://") and repo or ("https://" .. repo)
  local shown = repo:gsub("^https?://", "")
  return pandoc.Link({ pandoc.Str(shown) }, url)
end

local function get_meta(meta)
  if meta["code-base-url"] then
    code_base_url = pandoc.utils.stringify(meta["code-base-url"])
  end
  if meta.repo then
    repo = pandoc.utils.stringify(meta.repo)
    if not meta["code-base-url"] then
      local url = repo:match("^https?://") and repo or ("https://" .. repo)
      code_base_url = url:gsub("/$", "") .. "/blob/main/"
    end
  end
  if meta["qr-file"] then
    qr_file = pandoc.utils.stringify(meta["qr-file"])
  end
  if meta["talk-dark-bg"] then
    dark_bg = pandoc.utils.stringify(meta["talk-dark-bg"])
  end
  -- Heading face: `headings: serif` or `headings: sans` in the deck's YAML.
  if meta.headings then
    local h = pandoc.utils.stringify(meta.headings)
    local tracking = (h == "serif") and "0em" or "-0.02em"
    if h == "serif" or h == "sans" then
      quarto.doc.include_text("in-header", "<style>html:root{--talk-font-heading:var(--talk-font-heading-" .. h ..
        ");--talk-heading-tracking:" .. tracking .. "}</style>")
    end
  end
  -- Title slide gets its own state so CSS can hide the footer and slide number.
  local attrs = meta["title-slide-attributes"] or pandoc.MetaMap({})
  local state = attrs["data-state"] and pandoc.utils.stringify(attrs["data-state"]) or ""
  attrs["data-state"] = pandoc.MetaString((state .. " talk-titlepage"):gsub("^ ", ""))
  meta["title-slide-attributes"] = attrs
  return meta
end

local function add_state(attr, state)
  local existing = attr.attributes["data-state"]
  if existing and existing ~= "" then
    attr.attributes["data-state"] = existing .. " " .. state
  else
    attr.attributes["data-state"] = state
  end
end

local function make_dark(attr)
  add_state(attr, "talk-dark")
  if not attr.attributes["background-color"] then
    attr.attributes["background-color"] = dark_bg
  end
end

local function Header(h)
  if h.level == 1 then
    h.classes:insert("talk-section")
    make_dark(h.attr)
    return h
  end
  if h.level == 2 and h.classes:includes("dark") then
    make_dark(h.attr)
    return h
  end
end

-- ::: {.qr} ::: (empty) -> the repo QR code with the link beneath it.
local function Div(div)
  if not div.classes:includes("qr") or #div.content > 0 then
    return nil
  end
  if not repo then
    return pandoc.Para({ pandoc.Str("[.qr needs repo: in the YAML header]") })
  end
  local alt = "QR code linking to " .. repo:gsub("^https?://", "")
  div.content = pandoc.Blocks({
    pandoc.Plain({ pandoc.Image({}, qr_file, "", { alt = alt, class = "qr-img" }) }),
    pandoc.Plain({ repo_link() }),
  })
  return div
end

-- Must run at pre-ast (set in _extension.yml): later, Quarto has already turned
-- #fig- figures into its own node type and the link silently doesn't appear.
local function Figure(fig)
  local script = nil
  fig.content:walk({
    Image = function(img)
      if img.attributes.script then
        script = script or img.attributes.script
        img.attributes.script = nil
      end
      return img
    end,
  })
  fig.content = fig.content:walk({
    Image = function(img)
      img.attributes.script = nil
      return img
    end,
  })
  if not script then
    return nil
  end
  local link = pandoc.Link({ pandoc.Code(script) }, code_base_url .. script)
  local addition = pandoc.Span(
    { pandoc.Str("Code:"), pandoc.Space(), link },
    { class = "talk-code" }
  )
  local caption = fig.caption.long
  if #caption > 0 and caption[#caption].content then
    caption[#caption].content:extend({ pandoc.Space(), addition })
  else
    caption:insert(pandoc.Plain({ addition }))
  end
  fig.caption.long = caption
  return fig
end

return {
  { Meta = get_meta },
  { Header = Header, Figure = Figure, Div = Div },
}
