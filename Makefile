# make           run the figure scripts, then render the slides
# make figures   only the figure scripts (they write to figures/)
# make slides    only render, using the figures already in figures/
# make pdf       PDF copy of the slides via headless Chrome/Chromium
#                (`quarto install chromium` once if you have neither)
# make standalone  one self-contained HTML file (fonts, figures, maths inlined;
#                 ~10 MB) for presenting or emailing without internet
# make preview   live preview while editing

PYTHON ?= python
DECK ?= $(firstword $(wildcard *.qmd))
SCRIPTS := $(filter-out scripts/talk_style.py,$(wildcard scripts/*.py))
HTML := $(DECK:.qmd=.html)
CHROME ?= $(firstword $(wildcard $(HOME)/.local/share/quarto/chromium/*/chrome-linux/chrome) $(shell command -v google-chrome chromium chromium-browser 2>/dev/null))

.PHONY: all figures slides pdf standalone preview clean

all: figures slides

figures:
	@for s in $(SCRIPTS); do echo "== $$s"; $(PYTHON) $$s || exit 1; done

slides:
	quarto render $(DECK)

pdf: slides
	"$(CHROME)" --headless --no-sandbox --disable-gpu --virtual-time-budget=10000 \
	  --print-to-pdf="$(abspath $(DECK:.qmd=.pdf))" --print-to-pdf-no-header \
	  "file://$(abspath $(HTML))?print-pdf"

standalone:
	quarto render $(DECK) -M embed-resources:true -M self-contained-math:true -o $(notdir $(DECK:.qmd=-standalone.html))

preview:
	quarto preview $(DECK)

clean:
	rm -f $(HTML) $(DECK:.qmd=.pdf) $(DECK:.qmd=-standalone.html)
