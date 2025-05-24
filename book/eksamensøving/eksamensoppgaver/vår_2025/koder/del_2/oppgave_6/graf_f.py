import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return (x - 1) / ((x + 2) * (x - 2))

    # List of functions and their labels.
    functions = []

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-10,
        xmax=10,
        ymin=-4,
        ymax=4,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    color = plotmath.COLORS.get("blue")
    x1 = -2
    x2 = 2
    x = np.linspace(-25, x1, 1024)
    y = f(x)
    ax.plot(x, y, color=color, lw=2.5, label="$f$")

    x = np.linspace(x1, x2, 1024)
    y = f(x)
    ax.plot(x, y, color=color, lw=2.5)

    x = np.linspace(x2, 25, 1024)
    y = f(x)
    ax.plot(x, y, color=color, lw=2.5)

    color = plotmath.COLORS.get("red")
    ax.hlines(0, xmin=-10, xmax=10, color=color, lw=2, ls="--")
    ax.vlines(x1, ymin=-10, ymax=10, color=color, lw=2, ls="--")
    ax.vlines(x2, ymin=-10, ymax=10, color=color, lw=2, ls="--")

    ax.xaxis.label.set_fontsize(22)
    ax.yaxis.label.set_fontsize(22)
    ax.legend(fontsize=22)

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
