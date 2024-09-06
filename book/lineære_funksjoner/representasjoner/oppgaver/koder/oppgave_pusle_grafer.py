import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)


def f(x):
    return -x + 2


def g(x):
    return 2 * x - 4


def h(x):
    return 0.5 * x - 4


def r(x):
    return -2 * x + 2


a = -10
b = 10


x = np.linspace(a, b, 1024)

functions = [f, g, h, r]
colors = ["teal", "purple", "blue", "red"]

for func, color in zip(functions, colors):
    fig, ax = plt.subplots()
    ax.plot(x, func(x), color=color, lw=2, alpha=0.7)

    ax.spines["left"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["bottom"].set_position("zero")
    ax.spines["top"].set_color("none")

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    ax.set_xlabel(r"$x$", fontsize=16, loc="right")
    ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")

    xticks = list(np.arange(-4, 5, 1))
    xticks.remove(0)
    plt.xticks(xticks, fontsize=16)

    yticks = list(np.arange(-6, 7, 1))
    yticks.remove(0)
    plt.yticks(yticks, fontsize=16)

    plt.ylim(-7, 7)
    plt.xlim(-5, 5)

    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()

    # Lagrer figuren i vektorformat
    plt.savefig(f"../figurer/oppgave_1_{func.__name__}.svg")
    plt.close()

plt.show()
