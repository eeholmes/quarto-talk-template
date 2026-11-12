"""Example figure: one series of bars, sized for one of two columns (synthetic data).

Run from anywhere: python scripts/fig_example_bars.py
Writes figures/fig_example_bars.png.
"""

from pathlib import Path

import matplotlib.pyplot as plt

from talk_style import HALF, SERIES, apply_style

OUT = Path(__file__).resolve().parents[1] / "figures" / "fig_example_bars.png"

apply_style()
methods = ["Method A", "Method B", "Method C"]
rmse = [0.42, 0.31, 0.24]

fig, ax = plt.subplots(figsize=HALF)
bars = ax.bar(methods, rmse, color=SERIES[0], width=0.6)
ax.bar_label(bars, fmt="%.2f", padding=4, fontsize=10)
ax.set_ylim(0, 0.5)
ax.set_ylabel("Error (RMSE)")
ax.set_title("Lower is better")

OUT.parent.mkdir(exist_ok=True)
fig.savefig(OUT)
print(f"wrote {OUT}")
