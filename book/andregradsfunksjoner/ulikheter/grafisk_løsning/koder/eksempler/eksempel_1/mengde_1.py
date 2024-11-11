import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

plt.rc("text", usetex=True)


x_min = -10
x_max = 10

x = np.linspace(x_min, x_max, 1024)

a = 1
b = -4
c = 3

x_symmetri = -b / (2 * a)

fig, ax = plt.subplots(figsize=(8, 1))


ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
# ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
# ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")

ax.hlines(y=0, xmin=-6, xmax=-1, lw=5, color="red", alpha=0.5)

ax.hlines(y=0, xmin=1, xmax=6, lw=5, color="red", alpha=0.5)


xticks = [i for i in range(-5, 6)]
plt.xticks(xticks, fontsize=16)
plt.yticks([])

plt.ylim(-2, 2)
plt.xlim(-6, 6)


# plt.annotate(
#     text="Løsningsmengde",
#     xy=(roots[0] - 1, 0),
#     xytext=(x_symmetri, -4),
#     fontsize=16,
#     arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
#     horizontalalignment="center",
#     verticalalignment="center",
# )

# plt.annotate(
#     text="Løsningsmengde",
#     xy=(roots[0] - 3, 0),
#     xytext=(x_symmetri, -4),
#     fontsize=16,
#     arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
#     horizontalalignment="center",
#     verticalalignment="center",
# )

# plt.annotate(
#     text="Løsningsmengde",
#     xy=(roots[1] + 1, 0),
#     xytext=(x_symmetri, -4),
#     fontsize=16,
#     arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
#     horizontalalignment="center",
#     verticalalignment="center",
# )

# plt.annotate(
#     text="Løsningsmengde",
#     xy=(roots[1] + 3, 0),
#     xytext=(x_symmetri, -4),
#     fontsize=16,
#     arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
#     horizontalalignment="center",
#     verticalalignment="center",
# )


# ax.hlines(0, -10, roots[0], color="red", alpha=0.3, lw=8)
# ax.hlines(0, roots[1], 10, color="red", alpha=0.3, lw=8)

# plt.grid(False, linestyle="--", alpha=0.6)
plt.tight_layout()

plt.savefig("../../../figurer/eksempler/eksempel_1/mengde_1.svg")

plt.show()
