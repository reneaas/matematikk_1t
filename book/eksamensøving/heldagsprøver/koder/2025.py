import matplotlib.pyplot as plt
import random
from PIL import Image
import matplotlib.cm as cm

# ——— Settings ———
fig, ax = plt.subplots()
# ax.set_facecolor("#1A1A1D")
ax.axis("off")

# ——— Color palette ———
colors = ["#FF6B6B", "#FFD93D", "#6BCB77", "#4D96FF"]
colors = ["royalblue", "red", "magenta", "green"]

# ——— Draw “2025” ———
for i, ch in enumerate("2025"):
    ax.text(
        0.1 + i * 0.22,
        0.55,
        ch,
        transform=ax.transAxes,
        ha="center",
        va="center",
        color=colors[i],
        fontdict={"size": 180, "weight": "bold"},
    )

# ——— Decorative dots ———
for _ in range(50):
    x = random.random()
    y = random.random()
    sz = random.uniform(100, 800)
    c = random.choice(colors)
    ax.scatter(x, y, s=sz, c=c, alpha=0.7, transform=ax.transAxes)


plt.tight_layout()
plt.savefig(
    "../figurer/2025.svg",
    transparent=True,
)
