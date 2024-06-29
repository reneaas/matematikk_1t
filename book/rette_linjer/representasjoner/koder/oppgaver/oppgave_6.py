import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)

def f(x):
    return -2*x + 3

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


plt.xticks([])
plt.yticks([])

plt.ylim(-4, 5)
plt.xlim(-2, 5)

plt.scatter(1, 1, color="black", s=50)

plt.scatter(2, -1, color="black", s=50)

plt.text(
    x=1.1,
    y=1,
    s=r"$(x_1, 1)$",
    fontsize=16,
    ha="left",
)


plt.text(
    x=2.1,
    y=-1,
    s=r"$(2, -1)$",
    fontsize=16,
    ha="left",
)

plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/oppgaver/oppgave_6.svg")

plt.show()
