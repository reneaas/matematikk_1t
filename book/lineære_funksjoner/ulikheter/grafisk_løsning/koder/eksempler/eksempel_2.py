import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)

def f(x, a, b):
    return a*x + b

x_min = -10
x_max = 10

x = np.linspace(x_min, x_max, 1024)

a = 2
b = 1
y = 3

fig, ax = plt.subplots()
ax.plot(x, f(x, a, b), color="teal", lw=2, alpha=0.7, label="$f(x) = 2x + 1$")
ax.hlines(y, -10, 10, color="purple", alpha=0.7, lw=2, label="$y = 3$")
ax.plot(((y - b)/a), y, "ko", markersize=8, alpha=0.7)
ax.plot(((y - b)/a), 0, "k|", markersize=15, alpha=0.7)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$f(x)$", fontsize=16, loc="top", rotation="horizontal")

xticks = list(np.arange(-3, 6, 1))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-4, 6, 1))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

plt.ylim(-5, 6)
plt.xlim(-4, 6)


plt.annotate(
    text="Løsningsmengde",
    xy=((y - b)/a-0.1, 0),
    xytext=(-2, 4),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

plt.annotate(
    text="Løsningsmengde",
    xy=((y - b)/a-2, 0),
    xytext=(-2, 4),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

plt.annotate(
    text="Løsningsmengde",
    xy=(-3.5, 0),
    xytext=(-2, 4),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax.hlines(0, -5, (y-b)/a, color="red", alpha=0.3, lw=8)

plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=16, fancybox=True, framealpha=0.8, edgecolor='black', facecolor='white', loc='upper right')
plt.tight_layout()

plt.savefig("../../figurer/eksempler/eksempel_2.svg")

plt.show()
