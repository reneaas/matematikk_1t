import numpy as np
import matplotlib.pyplot as plt

# plt.rc("text", usetex=True)


def f(x):
    return -x + 1


def g(x):
    return -2*x + 1


a = -50
b = 50

xmin, xmax = -5, 5
ymin, ymax = -5, 5

x = np.linspace(a, b, 1024)

fig, ax = plt.subplots()
ax.plot(x, f(x), color="teal", lw=2, alpha=0.7, label="$f$")
ax.plot(x, g(x), color="purple", lw=2, alpha=0.7, label="$g$")

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")

xticks = list(np.arange(xmin + 1, xmax, 1))
if 0 in xticks:
    xticks.remove(0)
plt.xticks(xticks, fontsize=16)
#plt.xticks([])         uten ticks

yticks = list(np.arange(ymin + 1, ymax, 1))
if 0 in yticks:
    yticks.remove(0)
plt.yticks(yticks, fontsize=16)
#plt.yticks([])         uten ticks

plt.ylim(ymin, ymax)
plt.xlim(xmin, xmax)

plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=16)
plt.tight_layout()

# Lagrer figuren i vektorformat
fname = __file__.split("/")[-1].replace(".py", ".svg")
plt.savefig(f"../../figurer/oppgaver/{fname}")
plt.show()
