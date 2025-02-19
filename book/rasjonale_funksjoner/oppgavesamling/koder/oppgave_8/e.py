import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    @np.vectorize
    def f(x):
        if x != 2:
            return (x + 3) ** 2 / (x - 2)
        else:
            return None

    def g(x):
        return x + 8

    # List of functions and their labels.
    functions = []

    xmin = -20
    xmax = 20
    ymin = -20
    ymax = 30

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=xmin,
        xmax=xmax,
        ymin=ymin,
        ymax=ymax,
        ticks=False,
    )
    x1 = 2
    x = np.linspace(xmin, x1, 1024)
    y = f(x)
    ax.plot(x, y, color="teal", alpha=0.7, lw=2, label="$f$")
    x = np.linspace(x1, xmax, 1024)
    y = f(x)
    ax.plot(x, y, color="teal", alpha=0.7, lw=2)

    x = np.linspace(xmin, xmax, 1024)
    y = g(x)

    ax.plot(x, y, linestyle="--", color="blue", lw=1.5)

    dx = dy = 0.5
    ax.text(
        x=8,
        y=13 + dy,
        s="$y = x + 8$",
        fontsize=16,
        va="top",
        ha="left",
        color="blue",
    )

    ax.vlines(
        x=x1, ymin=ymin, ymax=ymax, linestyle="--", color="red", lw=1.5, alpha=0.8
    )

    ax.text(
        x=x1 + dx,
        y=-5,
        s="$x = 2$",
        fontsize=16,
        va="center",
        ha="left",
        color="red",
    )

    ax.plot(-3, 0, "ko", markersize=8, alpha=0.7)
    ax.text(
        x=-3,
        y=-3 * dy,
        s="$(-3, 0)$",
        fontsize=16,
        va="top",
        ha="center",
    )

    # ax.set_yticks(yticks)
    # ax.set_yticklabels(yticklabels, fontsize=16)

    ax.legend(fontsize=16)

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname, fname=fname
        )  # Lagrer figuren i `dirname`-directory

    if not save:

        plotmath.show()


if __name__ == "__main__":

    import pathlib

    # Get the directory where the script is located
    current_dir = str(pathlib.Path(__file__).resolve().parent)

    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break

    dirname = "/".join(parts)

    # NOTE: Set `save=True` to save figure. `save=False` to display figure.
    main(dirname=dirname, save=True)
