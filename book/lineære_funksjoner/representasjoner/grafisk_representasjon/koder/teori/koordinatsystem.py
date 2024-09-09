import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)


a = -5
b = 7

x = np.linspace(a, b, 1024)

fig, ax = plt.subplots()
ax.plot(3, 2, color="black", alpha=0.7, marker="o")
ax.plot([3, 3], [0, 2], color="blue", lw=1.5, linestyle="--", alpha=0.7)
ax.plot([0, 3], [2, 2], color="blue", lw=1.5, linestyle="--", alpha=0.7)
ax.text(3, 2.1, r"$(3, 2)$", fontsize=16, ha="center", va="bottom")


ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")


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
plt.savefig("../../figurer/teori/koordinatsystem.svg")

plt.show()
