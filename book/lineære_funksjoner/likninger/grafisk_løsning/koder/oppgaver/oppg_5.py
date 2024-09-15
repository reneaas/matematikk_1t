import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)


def f(x):
    return -2 * x + 6


def make_graph(
    functions: list[callable],
    x_min: float = -10,
    x_max: float = 10,
    xlabel: str = r"$x$",
    ylabel: str = r"$y$",
    labels: list[str] = None,
) -> tuple[plt.Figure, plt.Axes]:

    x = np.linspace(x_min, x_max, 1024)

    default_colors = [
        "teal",
        "purple",
        "red",
        "green",
        "blue",
        "orange",
        "olive",
        "magenta",
        "black",
    ]

    fig, ax = plt.subplots()

    if labels:
        for color, func, label in zip(default_colors, functions, labels):
            ax.plot(x, func(x), lw=2, alpha=0.7, color=color, label=label)
        ax.legend(fontsize=16)
    else:
        for color, func in zip(default_colors, functions):
            ax.plot(x, func(x), lw=2, alpha=0.7, color=color)

    ax.spines["left"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["bottom"].set_position("zero")
    ax.spines["top"].set_color("none")

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    ax.set_xlabel(xlabel, fontsize=16, loc="right")
    ax.set_ylabel(ylabel, fontsize=16, loc="top", rotation="horizontal")

    return fig, ax


fig, ax = make_graph(functions=[f], labels=["$f$", "$g$"])


xticks = list(np.arange(-4, 5, 1))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-5, 4, 1))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

plt.ylim(-6, 4)
plt.xlim(-5, 5)

plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Lagrer figuren i vektorformat
# plt.savefig("../../figurer/oppgaver/oppg_5.svg")

plt.show()
