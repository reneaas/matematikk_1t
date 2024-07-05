import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)

def f(x, a, b, c):
    return a*x**2 + b*x + c


a = -8
b = 8


x = np.linspace(a, b, 1024)

fig, ax = plt.subplots()
ax.plot(x, f(x, a=1, b=-1, c=-2), color="teal", lw=2, alpha=0.7, label="$f(x)$")
ax.plot(x, f(x, a=0, b=3, c=-5), color="purple", lw=2, alpha=0.7, label="$g(x)$")

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")




xticks = list(np.arange(-3, 5, 1))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-4, 6, 2))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

# plt.xticks([])
# plt.yticks([])

plt.ylim(-6, 6)
plt.xlim(-4, 5)

plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=16)
plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/eksempler/eksempel_2.svg")

plt.show()
