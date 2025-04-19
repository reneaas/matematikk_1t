import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import plotmath

plt.rc("text", usetex=True)


def f(x, a, b, c):
    return a * x**2 + b * x + c


x_min = -8
x_max = 8


x = np.linspace(x_min, x_max, 1024)

# Koeffisienter for andregradsfunksjon 1
a1 = 1
b1 = -1
c1 = -6


# Koeffisienter for andregradsfunksjon 2
a2 = -2
b2 = 4
c2 = 3

xlim = (-b1 / (2 * a1) - 6, -b1 / (2 * a1) + 6)
ylim = (-8, 10)

nrows = 1
ncols = 2
fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(10, 4))

# ax^2 + bx + c > 0 eller ax^2 + bx + c >= 0
j = 0


roots = sp.solve(f"{a1} * x**2 + {b1}*x + {c1} - {a2}*x**2 - {b2}*x - {c2}", "x")
roots = [float(root.evalf()) for root in roots]
for i in range(2):
    ax[i].plot(
        x,
        f(x, a=a1, b=b1, c=c1),
        color=plotmath.COLORS.get("blue"),
        lw=2,
        alpha=0.7,
        label="$f$",
    )
    ax[i].plot(
        x,
        f(x, a=a2, b=b2, c=c2),
        color=plotmath.COLORS.get("red"),
        lw=2,
        alpha=0.7,
        label="$g$",
    )

    for root in roots:
        ax[i].plot(root, f(root, a1, b1, c1), "ko", markersize=8, alpha=0.7)
        ax[i].plot(root, 0, "k|", markersize=15, alpha=0.7)
        ax[i].vlines(
            root, 0, f(root, a1, b1, c1), color="black", alpha=0.5, linestyle="--"
        )

    ax[i].spines["left"].set_position("zero")
    ax[i].spines["right"].set_color("none")
    ax[i].spines["bottom"].set_position("zero")
    ax[i].spines["top"].set_color("none")

    ax[i].plot(1, 0, ">k", transform=ax[i].get_yaxis_transform(), clip_on=False)
    ax[i].plot(0, 1, "^k", transform=ax[i].get_xaxis_transform(), clip_on=False)

    ax[i].set_xlabel(r"$x$", fontsize=16, loc="right")
    ax[i].set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")

    ax[i].set_xticks([])
    ax[i].set_yticks([])
    ax[i].set_ylim(*ylim)
    ax[i].set_xlim(*xlim)


j = 0

ax[j].annotate(
    text="Løsningsmengde",
    xy=(roots[0] - 3, 0),
    xytext=(-b1 / (2 * a1), -8),
    fontsize=16,
    arrowprops=dict(
        arrowstyle="->", lw=2, color="black", alpha=0.7, connectionstyle="arc3,rad=-0.3"
    ),
    horizontalalignment="center",
    verticalalignment="center",
)

# ax[j].annotate(
#     text="Løsningsmengde",
#     xy=(roots[0] - 1, 0),
#     xytext=(-b/(2*a), -8),
#     fontsize=16,
#     arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7, connectionstyle="arc3,rad=-0.3"),
#     horizontalalignment="center",
#     verticalalignment="center",
# )

# ax[j].annotate(
#     text="Løsningsmengde",
#     xy=(roots[1] + 3, 0),
#     xytext=(-b/(2*a), -8),
#     fontsize=16,
#     arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7, connectionstyle="arc3,rad=0.3"),
#     horizontalalignment="center",
#     verticalalignment="center",
# )

ax[j].annotate(
    text="Løsningsmengde",
    xy=(roots[1] + 1, 0),
    xytext=(-b1 / (2 * a1), -8),
    fontsize=16,
    arrowprops=dict(
        arrowstyle="->", lw=2, color="black", alpha=0.7, connectionstyle="arc3,rad=0.3"
    ),
    horizontalalignment="center",
    verticalalignment="center",
)


ax[0].hlines(0, -8, roots[0], color="red", alpha=0.3, lw=8)
ax[0].hlines(0, roots[1], 8, color="red", alpha=0.3, lw=8)


j = 1
# ax[j].annotate(
#     text="Løsningsmengde",
#     xy=(-b/(2*a), 0),
#     xytext=(-b/(2*a), 6),
#     fontsize=16,
#     arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
#     horizontalalignment="center",
#     verticalalignment="center",
# )

ax[j].annotate(
    text="Løsningsmengde",
    xy=(roots[0] + 0.5, 0),
    xytext=(-b1 / (2 * a1) - 0.5, 8),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].annotate(
    text="Løsningsmengde",
    xy=(roots[1] - 0.5, 0),
    xytext=(-b1 / (2 * a1) - 0.5, 8),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)


ax[1].hlines(0, roots[0], roots[1], color="red", alpha=0.3, lw=8)


fig.legend(
    [r"$f$", r"$g$"],
    fontsize=16,
    loc="outside lower right",
    frameon=True,
    # bbox_to_anchor=(-b/(2*a), 8),
    fancybox=True,
    shadow=True,
    ncol=2,
)


plt.tight_layout()

# Lagrer figuren i vektorformat
# plt.savefig("../../figurer/teori/andregradsulikhet_f_vs_andregradsfunksjon.svg")

plt.show()
