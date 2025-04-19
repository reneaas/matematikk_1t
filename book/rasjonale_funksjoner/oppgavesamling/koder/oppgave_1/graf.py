import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    @np.vectorize
    def f(x):
        if x != -1:
            return -2 * (x - 3) / (x + 1)

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
    x1 = -1
    x = np.linspace(xmin, x1, 1024)
    y = f(x)
    ax.plot(x, y, color=plotmath.COLORS.get("blue"), lw=2.5, label="$f$")
    x = np.linspace(x1, xmax, 1024)
    y = f(x)
    ax.plot(x, y, color=plotmath.COLORS.get("blue"), lw=2.5)

    ax.hlines(
        y=-2,
        xmin=xmin,
        xmax=xmax,
        linestyle="--",
        color=plotmath.COLORS.get("red"),
        lw=2,
    )
    ax.vlines(
        x=x1,
        ymin=ymin,
        ymax=ymax,
        linestyle="--",
        color=plotmath.COLORS.get("red"),
        lw=2,
    )

    xticks = [i for i in range(xmin + 1, xmax)]
    if 0 in xticks:
        xticks.remove(0)

    xticklabels = [f"${i}$" if i % 2 == 0 else "" for i in xticks]

    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels, fontsize=16)

    yticks = [i for i in range(ymin + 1, ymax)]
    if 0 in yticks:
        yticks.remove(0)

    yticklabels = [f"${i}$" if i % 2 == 0 else "" for i in yticks]

    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels, fontsize=16)

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
