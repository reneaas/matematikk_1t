import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

plt.rc("text", usetex=True)

def f(x, a, b):
    return a*x + b




x_min = -8
x_max = 8


x = np.linspace(x_min, x_max, 1024)

a = 1
b = -1

y = 3

fig, ax = plt.subplots()
ax.plot(x, f(x, a=a, b=b), color="teal", lw=2, alpha=0.7, label="$f(x) = ax + b$")
ax.plot(((y-b)/a), y, "ko", markersize=8, alpha=0.7)
ax.hlines(y, x_min, x_max, color="red", linestyle="-", alpha=0.7, label="$y = k$")
ax.vlines(((y-b)/a), 0, y, color="black", linestyle="--", alpha=0.7)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")



plt.annotate(
    text="Skjæringen mellom $f(x) = ax + b$ og $y = k$",
    xy=((y-b)/a, y),
    xytext=(3, 6),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7, connectionstyle="arc3,rad=-0.2"),
    horizontalalignment="center",
    verticalalignment="center",
)




plt.xticks([(y-b)/a], labels=[r"$x_1$"], fontsize=16)
plt.yticks([])

plt.ylim(-4, 8)
plt.xlim(-2, 6)
plt.legend(fontsize=16)
plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/teori/skjæring_lineær_fn_horisontal_linje.svg")

plt.show()
