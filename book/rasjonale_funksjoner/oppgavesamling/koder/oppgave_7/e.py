import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    @np.vectorize
    def f(x):
        if x != 4:
            return (x - 2) / (x - 4)

    # List of functions and their labels.
    functions = []

    xmin = -10
    xmax = 10
    ymin = -10
    ymax = 10

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=xmin,
        xmax=xmax,
        ymin=ymin,
        ymax=xmax,
        ticks=False,
    )
    x1 = 4
    x = np.linspace(xmin, x1, 1024)
    y = f(x)
    ax.plot(x, y, color=plotmath.COLORS.get("blue"), lw=2.5, label="$f$")
    x = np.linspace(x1, xmax, 1024)
    y = f(x)
    ax.plot(x, y, color=plotmath.COLORS.get("blue"), lw=2.5)

    ax.hlines(
        y=1,
        xmin=xmin,
        xmax=xmax,
        linestyle="--",
        color=plotmath.COLORS.get("red"),
        lw=1,
    )
    dx = dy = 0.5
    ax.text(
        x=-5,
        y=1 + dy,
        s="$y = 1$",
        fontsize=16,
        va="bottom",
        ha="center",
        color="blue",
    )

    ax.vlines(
        x=x1,
        ymin=ymin,
        ymax=ymax,
        linestyle="--",
        color=plotmath.COLORS.get("red"),
        lw=2,
    )

    ax.text(
        x=x1 + dx,
        y=-5,
        s="$x = 4$",
        fontsize=16,
        va="center",
        ha="left",
        color="red",
    )

    # Draw hole at x = -2
    ax.plot(-2, f(-2), marker="x", color="red", markersize=15)
    ax.text(
        x=-2,
        y=f(-2) - 1,
        s=r"$(-2, \frac{2}{3})$",
        fontsize=16,
        va="top",
        ha="center",
        color="red",
    )

    ax.plot(2, 0, "ko", markersize=8, alpha=0.7)
    ax.text(
        x=2,
        y=-dy,
        s="$(2, 0)$",
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
