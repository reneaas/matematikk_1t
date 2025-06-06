import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)

def f(x):
    return -2*x + 3


a = -4
b = 6


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
ax.set_ylabel(r"$f(x)$", fontsize=16, loc="top", rotation="horizontal")


x_vals = [i for i in range(-1, 4)]
y_vals = [f(i) for i in x_vals]

for i in range(len(x_vals)):
    ax.plot(x_vals[i], y_vals[i], color="black", alpha=0.7, marker="o")
    ax.text(x_vals[i], y_vals[i] + 0.1, f"({x_vals[i]}, {y_vals[i]})", fontsize=16, ha="right", va="top")



xticks = list(np.arange(-1, 4, 1))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-4, 8, 2))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

plt.ylim(-6, 8)
plt.xlim(-2, 4)

plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/underveisoppgaver/underveisoppgave_2.svg")

plt.show()
