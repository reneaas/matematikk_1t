import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)


def f(x):
    return -2 * x - 4


def g(x):
    return -2 * x + 2


def h(x):
    return -x + 2


def r(x):
    return x + 2


a = -10
b = 10

xmin, xmax = -7, 7
ymin, ymax = -9, 9

x = np.linspace(a, b, 1024)

fig, ax = plt.subplots()
ax.plot(x, f(x), color="purple", lw=2, alpha=0.7, label="$f$")
ax.plot(x, g(x), color="blue", lw=2, alpha=0.7, label="$g$")
ax.plot(x, h(x), color="red", lw=2, alpha=0.7, label="$h$")
ax.plot(x, r(x), color="teal", lw=2, alpha=0.7, label="$r$")


ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")


plt.ylim(ymin, ymax)
plt.xlim(xmin, xmax)
plt.xticks([])
plt.yticks([])

plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=16, loc="lower left")
plt.tight_layout()

# Lagrer figuren i vektorformat
fname = __file__.split("/")[-1].replace(".py", ".svg")
plt.savefig(f"../../figurer/oppgaver/{fname}")
plt.show()
