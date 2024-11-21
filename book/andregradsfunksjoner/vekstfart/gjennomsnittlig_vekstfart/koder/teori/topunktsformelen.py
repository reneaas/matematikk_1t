import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)


def f(x):
    return 2 * x - 1


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


x1 = 1
y1 = f(x1)
ax.plot(x1, y1, color="black", alpha=0.7, marker="o")

ax.text(x1, y1 + 0.1, r"$(x_1, y_1)$", fontsize=16, ha="right", va="bottom")

x2 = 3
y2 = f(x2)

ax.plot(x2, y2, color="black", alpha=0.7, marker="o")
ax.text(x2, y2 + 0.1, r"$(x_2, y_2)$", fontsize=16, ha="right", va="bottom")

ax.plot([x1, x2], [y1, y1], linestyle="--", color="blue", alpha=0.7)
ax.plot([x2, x2], [y1, y2], linestyle="--", color="blue", alpha=0.7)

ax.text((x1 + x2) / 2, y1 - 0.3, r"$\Delta x$", fontsize=16, ha="center", va="center")
ax.text(x2 + 0.3, (y1 + y2) / 2, r"$\Delta y$", fontsize=16, ha="left", va="center")


plt.ylim(-2, 6)
plt.xlim(-2, 6)

plt.xticks([x1, x2], [r"$x_1$", r"$x_2$"], fontsize=16)

plt.yticks([y1, y2], [r"$y_1$", r"$y_2$"], fontsize=16)

plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/teori/topunktsformelen.svg")

plt.show()
