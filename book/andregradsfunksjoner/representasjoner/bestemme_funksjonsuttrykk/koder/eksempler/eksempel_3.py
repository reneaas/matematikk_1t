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
ax.plot(x, f(x, a=-1, b=1, c=2), color="teal", lw=2, alpha=0.7)

roots = sp.solve("-x**2 + x + 2", "x")
for root in roots:
    ax.plot(root, 0, "ko", markersize=8, alpha=0.7)


ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$f(x)$", fontsize=16, loc="top", rotation="horizontal")




xticks = list(np.arange(-4, 6, 1))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-6, 8, 2))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

# plt.xticks([])
# plt.yticks([])

plt.ylim(-8, 8)
plt.xlim(-5, 6)

plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/eksempler/eksempel_1.svg")

plt.show()