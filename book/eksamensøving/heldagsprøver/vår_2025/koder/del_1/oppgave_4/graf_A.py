import plotmath
import numpy as np


def main(dirname, save):

    # List of functions and their labels.

    xmin = -10
    xmax = 10
    ymin = -10
    ymax = 10

    functions = []
    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=xmin,
        xmax=xmax,
        ymin=ymin,
        ymax=ymax,
        ticks=False,
    )

    horisontal_asymptote = 1
    x_inf = -1
    x_zero = 1

    ax.plot(x_zero, 0, "ko", markersize=8, alpha=0.7)

    @np.vectorize
    def f(x):
        if x != x_inf:
            return horisontal_asymptote * (x - x_zero) / (x - x_inf)
        else:
            return None

    x = np.linspace(-20, x_inf, 1024)
    y = f(x)
    ax.plot(x, y, label=r"$\mathrm{A}$", color="teal", lw=2.5, alpha=0.8)

    x = np.linspace(x_inf, 20, 1024)
    y = f(x)
    ax.plot(x, y, color="teal", lw=2.5, alpha=0.8)

    ax.vlines(
        x=x_inf,
        ymin=ymin,
        ymax=ymax,
        color="blue",
        linestyle="--",
    )

    ax.hlines(
        y=horisontal_asymptote,
        xmin=xmin,
        xmax=xmax,
        color="blue",
        linestyle="--",
    )
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
