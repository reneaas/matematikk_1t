import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)

def f(x, a, b, c):
    return a*x**2 + b*x + c


a = -8
b = 8


x = np.linspace(a, b, 1024)

fig, ax = plt.subplots()
ax.plot(x, f(x, a=1, b=-1, c=-6), color="teal", lw=2, alpha=0.7)
ax.plot(x, f(x, a=-1, b=-4, c=-4), color="orange", lw=2, alpha=0.7)
ax.plot(x, f(x, a=4, b=-3, c=1), color="purple", lw=2, alpha=0.7)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")




# xticks = list(np.arange(-1, 4, 1))
# xticks.remove(0)
# plt.xticks(xticks, fontsize=16)

# yticks = list(np.arange(-6, 6, 2))
# yticks.remove(0)
# plt.yticks(yticks, fontsize=16)

plt.xticks([])
plt.yticks([])

plt.ylim(-8, 8)
plt.xlim(-8, 8)

plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/teori/intro_tre_andregradsfunksjoner.svg")

plt.show()
