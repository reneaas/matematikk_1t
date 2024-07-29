import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

plt.rc("text", usetex=True)

def f(x, a, b, c):
    return a*x**2 + b*x + c


a = -8
b = 8


x = np.linspace(a, b, 1024)

fig, ax = plt.subplots()
ax.plot(x, f(x, a=1, b=-1, c=2), color="teal", lw=2, alpha=0.7, label="$f$")

x_vals = [0, 1, 2]
y_vals = [f(x, a=1, b=-1, c=2) for x in x_vals]
for x_val, y_val in zip(x_vals, y_vals):
    ax.plot(x_val, y_val, "ko", markersize=8, alpha=0.7)


ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")




xticks = list(np.arange(-4, 6, 1))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-0, 8, 1))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

# plt.xticks([])
# plt.yticks([])

plt.ylim(-1, 8)
plt.xlim(-5, 6)

plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=16)
plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/eksempler/eksempel_1.svg")

plt.show()
