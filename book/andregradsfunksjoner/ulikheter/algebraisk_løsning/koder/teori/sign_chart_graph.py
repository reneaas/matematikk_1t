import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

plt.rc("text", usetex=True)

def f(x, a, b, c):
    return a * x**2 + b*x + c


x_min = -10
x_max = 10

x = np.linspace(x_min, x_max, 1024)

a = 1
b = -1
c = -6

x_symmetri = -b/(2*a)

fig, ax = plt.subplots()
ax.plot(x, f(x, a, b, c), color="teal", lw=2, alpha=0.7, label="$f$")

roots = sp.solve(f"{a}*x**2 + {b}*x + {c}", "x")
roots = [float(root.evalf()) for root in roots]
roots = sorted(roots)
for root in roots:
    ax.plot(root, 0, "ko", markersize=8, alpha=0.7)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")


dx = 5
xticks = roots
xticks_labels = ["$x_1$", "$x_2$"]
plt.xticks(xticks, xticks_labels, fontsize=16)

plt.yticks([])
plt.ylim(-10, 14)
plt.xlim(x_symmetri - 5, x_symmetri + 5)


plt.legend(fontsize=16)
plt.tight_layout()

plt.savefig("../../figurer/teori/fortegnslinje_graf.svg")

plt.show()


