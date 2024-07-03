import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)

def f(x):
    return -x + 3



a = -5
b = 7

x = np.linspace(a, b, 1024)

fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].plot(x, f(x), color="teal", lw=2, alpha=0.7)

ax[0].spines["left"].set_position("zero")
ax[0].spines["right"].set_color("none")
ax[0].spines["bottom"].set_position("zero")
ax[0].spines["top"].set_color("none")

ax[0].plot(1, 0, ">k", transform=ax[0].get_yaxis_transform(), clip_on=False)
ax[0].plot(0, 1, "^k", transform=ax[0].get_xaxis_transform(), clip_on=False)

ax[0].set_xlabel(r"$x$", fontsize=16, loc="right")
ax[0].set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")


xticks = list(np.arange(-2, 5, 1))
xticks.remove(0)
ax[0].set_xticks(xticks)

yticks = list(np.arange(-2, 6, 1))
yticks.remove(0)
ax[0].set_yticks(yticks)

ax[0].set_xlim(-3, 5)
ax[0].set_ylim(-2, 6)

ax[0].tick_params(labelsize=16)

ax[0].grid(True, linestyle="--", alpha=0.6)


def get_circ(x, y, r):
    theta = np.linspace(0, 2*np.pi, 1024)
    x_circ = r * np.cos(theta) + x
    y_circ = r * np.sin(theta) + y
    return x_circ, y_circ


ax[1].plot(*get_circ(0, 0, 2), color="teal", lw=2, alpha=0.7)
ax[1].spines["left"].set_position("zero")
ax[1].spines["right"].set_color("none")
ax[1].spines["bottom"].set_position("zero")
ax[1].spines["top"].set_color("none")

ax[1].plot(1, 0, ">k", transform=ax[1].get_yaxis_transform(), clip_on=False)
ax[1].plot(0, 1, "^k", transform=ax[1].get_xaxis_transform(), clip_on=False)

ax[1].set_xlabel(r"$x$", fontsize=16, loc="right")
ax[1].set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")


xticks = list(np.arange(-2, 3, 1))
xticks.remove(0)
ax[1].set_xticks(xticks)

yticks = list(np.arange(-2, 3, 1))
yticks.remove(0)
ax[1].set_yticks(xticks)

ax[1].set_aspect("equal")

ax[1].set_xlim(-2.5, 2.5)
ax[1].set_ylim(-2.5, 2.5)

ax[1].tick_params(labelsize=16)

ax[1].grid(True, linestyle="--", alpha=0.6)

# plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/eksempler/funksjonsbegrepet/funksjonsgraf_vs_kurve.svg")

plt.show()
