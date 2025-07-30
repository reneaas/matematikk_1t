import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import plotmath

plt.rc("text", usetex=True)


def f(x, a, b):
    return a * x + b


x_min = -8
x_max = 8


x = np.linspace(x_min, x_max, 1024)

a = 2  # Stigningstall graf 1
b = -1  # Konstantledd graf 1

c = -1  # Stigningstall graf 2
d = 3  # Konstantledd graf 2

x_skjæring = (d - b) / (a - c)
y_skjæring = a * x_skjæring + b


fig, ax = plt.subplots()
ax.plot(
    x, f(x, a=a, b=b), color=plotmath.COLORS.get("blue"), lw=2.5, label="$Ax + By = C$"
)
ax.plot(
    x, f(x, a=c, b=d), color=plotmath.COLORS.get("red"), lw=2.5, label="$Dx + Ey = F$"
)
ax.plot(x_skjæring, y_skjæring, "ko", markersize=8, alpha=0.7)
ax.vlines(x_skjæring, 0, y_skjæring, color="black", linestyle="--", alpha=0.5)
ax.hlines(y_skjæring, 0, x_skjæring, color="black", linestyle="--", alpha=0.5)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")


plt.annotate(
    text="Løsning av likningssystemet \n $(x_1, y_1)$",
    xy=(x_skjæring, y_skjæring),
    xytext=(1.7, 6),
    fontsize=16,
    arrowprops=dict(
        arrowstyle="->", lw=2, color="black", alpha=0.7, connectionstyle="arc3,rad=+0.2"
    ),
    horizontalalignment="center",
    verticalalignment="center",
)


plt.xticks([x_skjæring], labels=[r"$x_1$"], fontsize=16)
plt.yticks([y_skjæring], labels=[r"$y_1$"], fontsize=16)

plt.ylim(-4, 8)
plt.xlim(-2, 6)
plt.legend(fontsize=16)
plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/teori/grafisk_løsning.svg", transparent=True)

plt.show()
