import numpy as np
import matplotlib.pyplot as plt
import plotmath

plt.rc("text", usetex=True)


def f(x):
    return -3 * x + 2


a = -10
b = 10

x = np.linspace(a, b, 1024)

fig, ax = plt.subplots()
ax.plot(x, f(x), color=plotmath.COLORS.get("blue"), lw=2.5)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")

xticks = list(np.arange(-3, 4, 1))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-4, 5, 1))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

plt.ylim(-5, 5)
plt.xlim(-4, 4)


plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

plt.savefig("../../figurer/underveisoppgaver/underveisoppgave_2.svg", transparent=True)

plt.show()
