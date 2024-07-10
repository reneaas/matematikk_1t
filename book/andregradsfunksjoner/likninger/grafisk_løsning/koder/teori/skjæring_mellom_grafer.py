import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

plt.rc("text", usetex=True)

def f(x, a, b, c):
    return a*x**2 + b*x + c


x_min = -8
x_max = 8


x = np.linspace(x_min, x_max, 1024)

a = -1
b = 4
c = 2

fig, ax = plt.subplots()
ax.plot(x, f(x, a=a, b=b, c=c), color="teal", lw=2, alpha=0.7, label="$f(x) = ax^2 + bx + c$")
ax.plot(x, f(x, a=0, b=1, c=-2), color="purple", lw=2, alpha=0.7, label="$g(x) = rx + q$")
ax.plot((-1, 4), (-3, 2), "ko", markersize=8, alpha=0.7)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")



xytext = (2, -5)

plt.annotate(
    text=r"Skjæringspunkter",
    xy=(-1, -3),
    xytext=xytext,
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7, connectionstyle="arc3,rad=-0.2"),
    horizontalalignment="center",
    verticalalignment="center",
)

plt.annotate(
    text=r"Skjæringspunkter",
    xy=(4, 2),
    xytext=xytext,
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7, connectionstyle="arc3,rad=0.2"),
    horizontalalignment="center",
    verticalalignment="center",
)

ax.plot([-1, -1], [-3, -1], "--", color="black", alpha=0.7)
ax.plot([4, 4], [2, 0], "--", color="black", alpha=0.7)


xticks = [-1, 4]

plt.xticks(xticks, labels=[r"$x_1$", r"$x_2$"], fontsize=16)
plt.yticks([])

plt.ylim(-8, 8)
plt.xlim(-3, 6)
plt.legend(fontsize=14, loc="upper left")
plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/teori/skjæring_mellom_grafer.svg")

plt.show()
