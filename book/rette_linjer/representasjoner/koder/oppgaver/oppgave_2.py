import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)

def f(x):
    return 2*x - 3


def g(x):
    return -0.5*x + 1




a = -5
b = 7

x = np.linspace(a, b, 1024)

fig, ax = plt.subplots()
ax.plot(x, f(x), color="teal", lw=2, alpha=0.7)
ax.plot(x, g(x), color="purple", lw=2, alpha=0.7)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")


xticks = list(np.arange(-1, 5, 1))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-3, 5, 1))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

plt.ylim(-4, 5)
plt.xlim(-2, 5)

plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Lagrer to versjoner av figuren.
plt.savefig("../../figurer/oppgaver/oppgave_2.png") 
plt.savefig("../../figurer/oppgaver/oppgave_2.pdf")
plt.savefig("../../figurer/oppgaver/oppgave_2.svg")

plt.show()
