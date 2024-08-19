import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)


def f(x):
    return 2 * x - 4


def g(x):
    return 2 * x + 4


def h(x):
    return -x - 4


def r(x):
    return -x + 4


a = -10
b = 10


x = np.linspace(a, b, 1024)

fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(10, 8))

i, j = (0, 0)
ax[0, 0].plot(x, f(x), color="teal", lw=2, alpha=0.7, label="$f(x) = 2x - 4$")
ax[0, 1].plot(x, g(x), color="blue", lw=2, alpha=0.7, label="$g(x) = 2x + 4$")
ax[1, 0].plot(x, h(x), color="purple", lw=2, alpha=0.7, label="$h(x) = -x - 4$")
ax[1, 1].plot(x, r(x), color="red", lw=2, alpha=0.7, label="$r(x) = -x + 4$")


xticks = list(np.arange(-8, 10, 2))
yticks = list(np.arange(-8, 10, 2))
xticks.remove(0)
yticks.remove(0)
for i in range(2):
    for j in range(2):

        ax[i, j].spines["left"].set_position("zero")
        ax[i, j].spines["right"].set_color("none")
        ax[i, j].spines["bottom"].set_position("zero")
        ax[i, j].spines["top"].set_color("none")

        ax[i, j].plot(
            1, 0, ">k", transform=ax[i, j].get_yaxis_transform(), clip_on=False
        )
        ax[i, j].plot(
            0, 1, "^k", transform=ax[i, j].get_xaxis_transform(), clip_on=False
        )

        ax[i, j].set_xlabel(r"$x$", fontsize=16, loc="right")
        ax[i, j].set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")

        ax[i, j].set_xticks(xticks)
        ax[i, j].set_yticks(yticks)

        ax[i, j].grid(True, linestyle="--", alpha=0.6)
        ax[i, j].set_ylim(-10, 10)
        ax[i, j].set_xlim(-10, 10)
        ax[i, j].legend(fontsize=16)


plt.tight_layout()


try:
    plt.savefig("book/lineære_funksjoner/intro/figurer/lineære_funksjoner.svg")
    plt.close()
except:
    plt.savefig("../figurer/lineære_funksjoner.svg")
    plt.show()
