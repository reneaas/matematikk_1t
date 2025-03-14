import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)

def f(x):
    return -x + 3


def get_circ(x, y, r):
    theta = np.linspace(0, 2*np.pi, 1024)
    x_circ = r * np.cos(theta) + x
    y_circ = r * np.sin(theta) + y
    return x_circ, y_circ


a = -5
b = 7

x = np.linspace(a, b, 1024)

fig, ax = plt.subplots()
ax.plot(x, f(x), color="teal", lw=2, alpha=0.7)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")


plt.axvline(x=4, color="purple", linestyle="-", lw=2, alpha=0.7)
plt.axhline(y=2, color="blue", linestyle="-", lw=2, alpha=0.7)



xticks = list(np.arange(-1, 6, 1))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-2, 5, 1))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

plt.ylim(-3, 5)
plt.xlim(-2, 6)

plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/eksempler/rette_linjer.svg")

plt.show()
