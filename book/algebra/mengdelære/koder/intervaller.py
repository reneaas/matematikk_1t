import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)


x_min = -7
x_max = 7

x = np.linspace(x_min, x_max, 1024)

fig, ax = plt.subplots()
# ax.plot(x, f(x), color="teal", lw=2, alpha=0.7)

ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
# ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")

color="teal"
a = 1
b = 3
dx = 0.2
dy = 0.05

ax.plot([a, a], [dy, -dy], color, lw=1.5, alpha=0.7)
ax.plot([a, a + dx], [dy, dy], color, lw=1.5, alpha=0.7)
ax.plot([a, a + dx], [-dy, -dy], color, lw=1.5, alpha=0.7)

ax.plot([a, b], [0, 0], color, lw=2.5, alpha=0.7)

ax.plot([b, b-dx], [0, dy], color, lw=1.5, alpha=0.7)
ax.plot([b, b-dx], [0, -dy], color, lw=1.5, alpha=0.7)



xticks = list(np.arange(-5, 6, 1))
plt.xticks(xticks, fontsize=16)

plt.yticks([])

plt.ylim(-0.5, 0.5)
plt.xlim(-6, 6)

# plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Lagrer figuren i vektorformat
# plt.savefig("../../figurer/oppgaver/oppg_1.svg")

plt.show()
