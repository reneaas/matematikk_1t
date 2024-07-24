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
b = -4
c = 0

x_symmetri = -b/(2*a)

fig, ax = plt.subplots()
ax.plot(x, f(x, a, b, c), color="teal", lw=2, alpha=0.7, label="$f$")
ax.plot(x, f(x, a=0, b=1, c=-2), color="mediumorchid", lw=2, alpha=0.7, label="$g$")

roots = sp.solve(f"{a}*x**2 + {b}*x + {c}", "x")
roots = [float(root.evalf()) for root in roots]
roots = sorted(roots)
# for root in roots:
#     ax.plot(root, 0, "ko", markersize=8, alpha=0.7)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")


dx = 5
xticks = list(np.arange(x_symmetri - dx + 1, x_symmetri + dx, 1))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-4, 6, 1))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

plt.ylim(-5, 6)
plt.xlim(x_symmetri - 5, x_symmetri + 5)


plt.legend(fontsize=16)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

plt.savefig("../../figurer/eksempler/eksempel_1_grafer.svg")

plt.show()


