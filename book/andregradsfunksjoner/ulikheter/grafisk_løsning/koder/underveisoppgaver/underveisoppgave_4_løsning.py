import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

plt.rc("text", usetex=True)

def f(x, a, b, c):
    return a * x**2 + b*x + c




x_min = -10
x_max = 10

x = np.linspace(x_min, x_max, 1024)

# Andregradsfunksjon
a = 0.5
b = 1
c = -3

# Lineær funksjon
p = -2
q = -4
r = -3

x_symmetri = -b/(2*a)

fig, ax = plt.subplots()
ax.plot(x, f(x, a, b, c), color="teal", lw=2, alpha=0.7, label="$f$")
ax.plot(x, f(x, p, q, r), color="mediumorchid", lw=2, alpha=0.7, label="$g$")

roots = sp.solve(f"{a}*x**2 + {b}*x + {c} - {p}*x**2 - {q}*x - {r}", "x")
roots = [float(root.evalf()) for root in roots]
roots = sorted(roots)
for root in roots:
    ax.plot(root, f(root, a, b, c), "ko", markersize=8, alpha=0.7)
    ax.plot(root, 0, "k|", markersize=15, alpha=0.7)
    ax.vlines(root, 0, f(root, a, b, c), color="black", alpha=0.5, linestyle="--")

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")


dx = 6
xticks = list(np.arange(int(x_symmetri) - dx + 1, int(x_symmetri) + dx, 1))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-5, 6, 1))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

plt.ylim(-6, 6)
plt.xlim(int(x_symmetri) - dx, int(x_symmetri) + dx)


plt.annotate(
    text="Løsningsmengde",
    xy=(roots[0] + 0.5, 0),
    xytext=(x_symmetri - 1, 4),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)


plt.annotate(
    text="Løsningsmengde",
    xy=(roots[1] - 0.5, 0),
    xytext=(x_symmetri - 1, 4),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax.hlines(0, roots[0], roots[1], color="red", alpha=0.3, lw=8)

plt.legend(fontsize=16)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

plt.savefig("../../figurer/underveisoppgaver/underveisoppgave_4_løsning.svg")

plt.show()


