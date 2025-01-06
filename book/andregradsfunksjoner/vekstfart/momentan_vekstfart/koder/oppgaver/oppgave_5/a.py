import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -0.5 * (x - 1) * (x + 3)

    def make_tangent_fn(a, h=1e-5):
        y0 = f(a)
        y2 = f(a + h)
        y1 = f(a - h)

        slope = 0.5 * (y2 - y1) / h
        intercept = y0 - slope * a

        print(slope)
        print(intercept)

        def tangent(x):
            return y0 + slope * (x - a)

        return tangent

    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-6,
        xmax=6,
        ymin=-6,
        ymax=6,
        ticks=False,
    )

    x = np.linspace(-10, 10, 1024)

    x1 = 1
    tangent1 = make_tangent_fn(a=x1)

    ax.plot(x, tangent1(x), color="blue", lw=2, alpha=0.7)
    ax.plot(-3, 0, "ko", markersize=8, alpha=0.7)
    ax.plot(x1, f(x1), "ko", markersize=8, alpha=0.7)

    dx = 0.2
    dy = 0.2
    ax.text(
        x=-3,
        y=0,
        s="$(-3, 0)$",
        fontsize=16,
        ha="right",
        va="bottom",
    )

    ax.text(
        x=1,
        y=3,
        s="$y = -2x + 2$",
        color="blue",
        fontsize=18,
    )

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
