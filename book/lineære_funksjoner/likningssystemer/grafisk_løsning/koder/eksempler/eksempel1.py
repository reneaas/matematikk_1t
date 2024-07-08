import numpy as np
import matplotlib.pyplot as plt

# plt.rc("text", usetex=True)

def f(x):
    return x + 1

def g(x):
    return 1 - x

a = -7
b = 7

x = np.linspace(a, b, 1024)

fig, ax = plt.subplots()
ax.plot(x, f(x), color="teal", lw=2, alpha=0.7)
ax.plot(x, g(x), color="red", lw=2, alpha=0.7)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")

xticks = list(np.arange(-5, 6, 1))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-2, 7, 1))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

plt.ylim(-3, 7)
plt.xlim(-6, 6)

plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("/home/eva/matematikk_1t/book/rette_linjer/likningssystemer/figurer/eksempler/eksempel1.svg")

plt.show()
