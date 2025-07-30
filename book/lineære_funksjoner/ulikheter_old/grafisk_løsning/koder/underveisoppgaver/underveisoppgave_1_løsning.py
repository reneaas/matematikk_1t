import numpy as np
import matplotlib.pyplot as plt
import plotmath

plt.rc("text", usetex=True)


def f(x):
    return x - 3


a = -7
b = 10

x = np.linspace(a, b, 1024)

fig, ax = plt.subplots()
ax.plot(x, f(x), color=plotmath.COLORS.get("blue"), lw=2.5)
ax.plot(3, 0, "ko", markersize=8, alpha=0.7)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$f(x)$", fontsize=16, loc="top", rotation="horizontal")

xticks = list(np.arange(-1, 7, 1))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-4, 6, 1))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

plt.ylim(-5, 6)
plt.xlim(-2, 7)

plt.annotate(
    text="Løsningsmengde",
    xy=(3 - 0.1, 0),
    xytext=(2, 5),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)


plt.annotate(
    text="Løsningsmengde",
    xy=(1, 0),
    xytext=(2, 5),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

plt.annotate(
    text="Løsningsmengde",
    xy=(-1.5, 0),
    xytext=(2, 5),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

plt.annotate(
    text="Nullpunkt er inkludert!",
    xy=(3, 0),
    xytext=(4, -3),
    fontsize=16,
    arrowprops=dict(
        arrowstyle="->", lw=2, color="black", alpha=0.7, connectionstyle="arc3,rad=0.2"
    ),
    horizontalalignment="center",
    verticalalignment="center",
)

ax.hlines(0, 3, -4, color=plotmath.COLORS.get("skyblue"), alpha=0.6, lw=8)


plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

plt.savefig(
    "../../figurer/underveisoppgaver/underveisoppgave_1_løsning.svg", transparent=True
)

plt.show()
