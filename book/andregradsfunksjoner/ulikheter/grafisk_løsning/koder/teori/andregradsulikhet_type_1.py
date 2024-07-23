import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

plt.rc("text", usetex=True)

def f(x, a, b, c):
    return a * x**2 + b*x + c


x_min = -8
x_max = 8


x = np.linspace(x_min, x_max, 1024)

a = 1
b = -1
c = -6

xlim = (-b/(2*a) - 6, -b/(2*a) + 6)
ylim = (-8, 8)

nrows = 1
ncols = 2
fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(10, 4))

# ax^2 + bx + c > 0 eller ax^2 + bx + c >= 0
j = 0


roots = sp.solve(f"{a} * x**2 + {b}*x + {c}", "x")
roots = [float(root.evalf()) for root in roots]
for i in range(2):
    ax[i].plot(x, f(x, a=a, b=b, c=c), color="teal", lw=2, alpha=0.7)
    for root in roots:
        ax[i].plot(root, 0, "ko", markersize=8, alpha=0.7)

    ax[i].spines["left"].set_position("zero")
    ax[i].spines["right"].set_color("none")
    ax[i].spines["bottom"].set_position("zero")
    ax[i].spines["top"].set_color("none")

    ax[i].plot(1, 0, ">k", transform=ax[i].get_yaxis_transform(), clip_on=False)
    ax[i].plot(0, 1, "^k", transform=ax[i].get_xaxis_transform(), clip_on=False)

    ax[i].set_xlabel(r"$x$", fontsize=16, loc="right")
    ax[i].set_ylabel(r"$f(x)$", fontsize=16, loc="top", rotation="horizontal")

    ax[i].set_xticks([])
    ax[i].set_yticks([])
    ax[i].set_ylim(*ylim)
    ax[i].set_xlim(*xlim)




j = 0
ax[j].text(
    s=r"$ax^2 + bx + c > 0$ eller $ax^2 + bx + c \geq 0$",
    x=-b/(2*a),
    y=6,
    fontsize=16,
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=2),
    horizontalalignment="center",
    verticalalignment="center",
)


ax[j].annotate(
    text="Løsningsmengde",
    xy=(roots[0] - 3, 0),
    xytext=(-b/(2*a), -8),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7, connectionstyle="arc3,rad=-0.3"),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].annotate(
    text="Løsningsmengde",
    xy=(roots[0] - 1, 0),
    xytext=(-b/(2*a), -8),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7, connectionstyle="arc3,rad=-0.3"),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].annotate(
    text="Løsningsmengde",
    xy=(roots[1] + 3, 0),
    xytext=(-b/(2*a), -8),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7, connectionstyle="arc3,rad=0.3"),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].annotate(
    text="Løsningsmengde",
    xy=(roots[1] + 1, 0),
    xytext=(-b/(2*a), -8),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7, connectionstyle="arc3,rad=0.3"),
    horizontalalignment="center",
    verticalalignment="center",
)


ax[0].hlines(0, -8, roots[0], color="red", alpha=0.3, lw=8)
ax[0].hlines(0, roots[1], 8, color="red", alpha=0.3, lw=8)



# ax + b < 0 eller ax + b <= 0
j = 1
ax[j].text(
    s=r"$ax^2 + bx + c < 0$ eller $ax^2 + bx + c \leq 0$",
    x=3,
    y=-7,
    fontsize=16,
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=2),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].annotate(
    text="Løsningsmengde",
    xy=(-b/(2*a), 0),
    xytext=(-b/(2*a), 3),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].annotate(
    text="Løsningsmengde",
    xy=(roots[0] + 0.5, 0),
    xytext=(-b/(2*a), 3),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].annotate(
    text="Løsningsmengde",
    xy=(roots[1] - 0.5, 0),
    xytext=(-b/(2*a), 3),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)


ax[1].hlines(0, roots[0], roots[1], color="red", alpha=0.3, lw=8)


plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/teori/andregradsulikhet_type_1.svg")

plt.show()
