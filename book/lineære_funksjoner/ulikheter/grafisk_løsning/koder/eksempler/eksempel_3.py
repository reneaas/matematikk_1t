import numpy as np
import matplotlib.pyplot as plt
import plotmath

plt.rc("text", usetex=True)


def f(x, a, b):
    return a * x + b


x_min = -10
x_max = 10

x = np.linspace(x_min, x_max, 1024)

a = -3
b = -1

c = 1
d = 3

x_sol = (-b + d) / (a - c)
y_sol = f(x_sol, a, b)

fig, ax = plt.subplots()
ax.plot(
    x, f(x, a, b), color=plotmath.COLORS.get("blue"), lw=2.5, label="$f(x)= -3x - 1$"
)
ax.plot(x, f(x, c, d), color=plotmath.COLORS.get("red"), lw=2.5, label="$g(x)= x + 3$")
ax.plot(x_sol, y_sol, "ko", markersize=8, alpha=0.7)
ax.plot(x_sol, 0, "k|", markersize=15, alpha=0.7)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")

xticks = list(np.arange(-5, 4, 1))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-4, 6, 1))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

plt.ylim(-5, 6)
plt.xlim(-6, 4)


plt.annotate(
    text="Løsningsmengde",
    xy=(x_sol - 0.1, 0),
    xytext=(-3, 4),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

plt.annotate(
    text="Løsningsmengde",
    xy=(x_sol - 2, 0),
    xytext=(-3, 4),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

plt.annotate(
    text="Løsningsmengde",
    xy=(-5.5, 0),
    xytext=(-3, 4),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax.hlines(0, -10, x_sol, color=plotmath.COLORS.get("skyblue"), alpha=0.6, lw=8)

plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(
    fontsize=14,
    fancybox=True,
    framealpha=0.8,
    edgecolor="black",
    facecolor="white",
    loc=(0.65, 0.5),
)
plt.tight_layout()

plt.savefig("../../figurer/eksempler/eksempel_3.svg", transparent=True)

plt.show()
