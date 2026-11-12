"""Example figure: three seasonal series with direct labels (synthetic data).

Run from anywhere: python scripts/fig_example_lines.py
Writes figures/fig_example_lines.png at full slide width.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from talk_style import FULL, SERIES, apply_style

OUT = Path(__file__).resolve().parents[1] / "figures" / "fig_example_lines.png"

apply_style()
rng = np.random.default_rng(1)
day = np.arange(365)
series = {
    "Coastal": 0.55 + 0.30 * np.cos(2 * np.pi * (day - 10) / 365),
    "Shelf": 0.38 + 0.16 * np.cos(2 * np.pi * (day - 20) / 365),
    "Open ocean": 0.22 + 0.06 * np.cos(2 * np.pi * (day - 30) / 365),
}

fig, ax = plt.subplots(figsize=FULL)
for (name, y), color in zip(series.items(), SERIES):
    y = y + rng.normal(0, 0.008, day.size)
    ax.plot(day, y, color=color)
    ax.annotate(name, (day[-1], y[-20:].mean()), xytext=(6, 0), textcoords="offset points",
                va="center", color=plt.rcParams["text.color"], fontsize=10)

ax.set_xlim(0, 365)
ax.set_ylim(0, 1)
ax.set_xticks([0, 91, 182, 273, 365], ["Jan", "Apr", "Jul", "Oct", "Jan"])
ax.set_ylabel("Fraction of pixels missing")
ax.set_title("Missing data peaks in winter, most at the coast")
ax.spines["right"].set_visible(False)

OUT.parent.mkdir(exist_ok=True)
fig.savefig(OUT)
print(f"wrote {OUT}")
