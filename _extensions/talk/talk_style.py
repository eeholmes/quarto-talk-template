"""Matplotlib style that matches the talk theme.

Lives in the extension so `quarto add` updates it with the CSS, and a branded
variant swaps it together with brand.scss. Figure scripts import it through the
small shim in scripts/talk_style.py.

Figures are drawn at the size they appear on a 1600 x 900 slide, so a font
size in points here is what the audience sees. Slide body text is 34 px.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager
from cycler import cycler

HERE = Path(__file__).resolve().parent

# Keep in step with brand.scss.
INK = "#17212B"
INK_SOFT = "#4A5563"
MUTED = "#6B7684"
RULE = "#DCE1E7"
ACCENT = "#006D82"
HIGHLIGHT = "#C25E14"

# Categorical series, in fixed order. Validated colour-blind safe on white
# (adjacent-pair CVD dE >= 8, all >= 3:1 contrast). Never cycle past six:
# fold extra series into "Other" or use small multiples.
SERIES = ["#00809A", "#D9732B", "#5A4FC4", "#42A35E", "#C2417A", "#9C7A00"]

# Single-hue sequential and two-pole diverging colormaps.
SEQUENTIAL = "GnBu"
DIVERGING = "RdBu_r"

# Slide geometry, in inches at DPI. The content area of a 1600 x 900 slide with
# a 5% margin is about 1520 x 690 px under a title.
DPI = 200
FULL = (15.2 / 2, 6.4 / 2)  # full width under a title -> 1520 x 640 px
HALF = (7.4 / 2, 6.4 / 2)  # one of two columns
WIDE = (15.2 / 2, 4.6 / 2)  # full width, short (leaves room for text)


def _register_fonts():
    for ttf in sorted((HERE / "mpl-fonts").glob("*.ttf")):
        font_manager.fontManager.addfont(str(ttf))


def apply_style():
    """Set matplotlib defaults for slide figures."""
    _register_fonts()
    plt.rcParams.update(
        {
            "figure.dpi": DPI,
            "savefig.dpi": DPI,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.05,
            "savefig.transparent": False,
            "figure.facecolor": "white",
            "figure.constrained_layout.use": True,
            "font.family": "Inter",
            "font.size": 11,
            "text.color": INK,
            "axes.titlesize": 12,
            "axes.titleweight": 600,
            "axes.titlelocation": "left",
            "axes.titlepad": 8,
            "axes.labelsize": 10.5,
            "axes.labelcolor": INK_SOFT,
            "axes.edgecolor": MUTED,
            "axes.linewidth": 0.8,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "axes.grid.axis": "y",
            "grid.color": RULE,
            "grid.linewidth": 0.6,
            "axes.axisbelow": True,
            "axes.prop_cycle": cycler(color=SERIES),
            "xtick.color": MUTED,
            "ytick.color": MUTED,
            "xtick.labelcolor": INK_SOFT,
            "ytick.labelcolor": INK_SOFT,
            "xtick.labelsize": 9.5,
            "ytick.labelsize": 9.5,
            "xtick.major.size": 3,
            "ytick.major.size": 0,
            "lines.linewidth": 2,
            "lines.markersize": 5,
            "patch.linewidth": 0,
            "legend.frameon": False,
            "legend.fontsize": 9.5,
            "image.cmap": SEQUENTIAL,
        }
    )
