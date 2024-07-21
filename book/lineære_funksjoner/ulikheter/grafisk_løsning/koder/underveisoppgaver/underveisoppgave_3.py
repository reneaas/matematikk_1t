import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)

def f(x, a, b):
    return a*x + b

x_min = -10
x_max = 10

x = np.linspace(x_min, x_max, 1024)

a = 3
b = -1

c = 1
d = 1

x_sol = (-b + d) / (a - c)
y_sol = f(x_sol, a, b)

fig, ax = plt.subplots()
ax.plot(x, f(x, a, b), color="teal", lw=2, alpha=0.7, label="$f$")
ax.plot(x, f(x, c, d), color="purple", lw=2, alpha=0.7, label="$g$")

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")

xticks = list(np.arange(-5, 4, 1))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-4, 6, 1))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

plt.ylim(-5, 6)
plt.xlim(-6, 4)



plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=16, fancybox=True, framealpha=0.8, edgecolor='black', facecolor='white', loc=(0.8, 0.5))
plt.tight_layout()

plt.savefig("../../figurer/underveisoppgaver/underveisoppgave_3.svg")

plt.show()
