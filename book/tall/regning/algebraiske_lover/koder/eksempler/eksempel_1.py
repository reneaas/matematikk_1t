import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

plt.rc("text", usetex=True)


x_min = -1
x_max = 8


x = np.linspace(x_min, x_max, 1024)

x = 0
y = 3
z = 2

xlim = (-0.5, 6)
ylim = (-0.5, 2)

fig, ax = plt.subplots(figsize=(8, 2))


ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)


ax.set_xlabel(r"$x$", fontsize=20, loc="right")

plt.xticks([i for i in range(6)], fontsize=20)
ax.set_yticks([])
ax.set_ylim(*ylim)
ax.set_xlim(*xlim)


# ax.annotate(
#     text="Mengde",
#     xy=(a + 0.5, 0),
#     xytext=(0.5 * (a + b), 2.5),
#     fontsize=20,
#     arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
#     horizontalalignment="center",
#     verticalalignment="center",
# )


ax.hlines(0, x, z, color="blue", alpha=0.5, lw=8)
ax.hlines(0, z, z + y, color="green", alpha=0.5, lw=8)
plt.tick_params(axis="x", size=10)

plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/eksempler/eksempel_1b.svg")

plt.show()
