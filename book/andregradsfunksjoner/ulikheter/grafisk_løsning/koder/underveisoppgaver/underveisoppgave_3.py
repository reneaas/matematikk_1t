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

a = 1
b = 1
c = 1

slope = -1
y_intercept = 4

x_symmetri = -b / (2 * a)

fig, ax = plt.subplots()
ax.plot(x, f(x, a, b, c), color=plotmath.COLORS.get("blue"), lw=2.5, label="$f$")
ax.plot(
    x,
    g(x, slope, y_intercept),
    color=plotmath.COLORS.get("red"),
    lw=2.5,
    label="$g$",
)

roots = sp.solve(f"{a}*x**2 + {b}*x + {c} - {slope}*x - {y_intercept}", "x")
roots = [float(root.evalf()) for root in roots]
roots = sorted(roots)

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
if 0 in xticks:
    xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-2, 9, 1))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

plt.ylim(-3, 9)
plt.xlim(int(x_symmetri) - dx, int(x_symmetri) + dx)

plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=16)
plt.tight_layout()

plt.savefig(
    "../../figurer/underveisoppgaver/underveisoppgave_3.svg",
    transparent=True,
)

plt.show()
