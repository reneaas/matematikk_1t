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

fig, ax = plt.subplots()
ax.plot(x, f(x, a=a, b=b), color="teal", lw=2, alpha=0.7, label="$f(x) = ax + b$")
ax.plot((-b/a), (0), "ko", markersize=8, alpha=0.7)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$f(x)$", fontsize=16, loc="top", rotation="horizontal")



plt.annotate(
    text="Nullpunkt \n Skjæring med $x$-aksen \n Skjæring med linja $y = 0$",
    xy=(-b/a, 0),
    xytext=(2.2, 5),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7, connectionstyle="arc3,rad=+0.4"),
    horizontalalignment="center",
    verticalalignment="center",
)




plt.xticks([-b/a], labels=[r"$x_1$"], fontsize=16)
plt.yticks([])

plt.ylim(-4, 8)
plt.xlim(-2, 6)
plt.legend(fontsize=16, loc="lower right")
plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/teori/nullpunkter.svg")

plt.show()
