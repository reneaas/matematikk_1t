import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import plotmath

plt.rc("text", usetex=True)


def f(x, a, b, c):
    return a * x**2 + b * x + c


def g(x, slope, y_intercept):
    return f(x, a=0, b=slope, c=y_intercept)


x_min = -10
x_max = 10

x = np.linspace(x_min, x_max, 1024)

# Andregradsfunksjon
a = 1
b = 5
c = 1

# Lineær funksjon
slope = -1
y_intercept = -4

x_symmetri = -b / (2 * a)

fig, ax = plt.subplots()
ax.plot(x, f(x, a, b, c), color=plotmath.COLORS.get("blue"), lw=2.5, label="$f$")
ax.plot(
    x, g(x, slope, y_intercept), color=plotmath.COLORS.get("red"), lw=2.5, label="$g$"
)

roots = sp.solve(f"{a}*x**2 + {b}*x + {c} - {slope}*x - {y_intercept}", "x")
roots = [float(root.evalf()) for root in roots]
roots = sorted(roots)
for root in roots:
    ax.plot(root, f(root, a, b, c), "ko", markersize=8, alpha=0.7)
    ax.plot(root, 0, "k|", markersize=15, alpha=0.7)
    ax.vlines(root, 0, f(root, a, b, c), color="black", alpha=0.5, linestyle="--")

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")


dx = 6
xticks = list(np.arange(int(x_symmetri) - dx + 1, int(x_symmetri) + dx, 1))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-5, 7, 1))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

plt.ylim(-6, 7)
plt.xlim(int(x_symmetri) - dx, int(x_symmetri) + dx)


plt.annotate(
    text="Løsningsmengde",
    xy=(roots[0] + 0.5, 0),
    xytext=(x_symmetri + 0.5, 4),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)


plt.annotate(
    text="Løsningsmengde",
    xy=(roots[1] - 0.5, 0),
    xytext=(x_symmetri + 0.5, 4),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax.hlines(0, roots[0], roots[1], color="red", alpha=0.3, lw=8)

plt.legend(fontsize=16)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

plt.savefig(
    "../../figurer/eksempler/eksempel_3.svg",
    transparent=True,
)

plt.show()
