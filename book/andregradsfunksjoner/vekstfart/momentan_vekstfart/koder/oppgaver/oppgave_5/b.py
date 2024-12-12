import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    def g(x):
        return (x - 2) ** 2 - 1

    def make_tangent_fn(a, h=1e-5):
        y0 = g(a)
        y2 = g(a + h)
        y1 = g(a - h)

        slope = 0.5 * (y2 - y1) / h
        intercept = y0 - slope * a

        print(slope)
        print(intercept)

        def tangent(x):
            return y0 + slope * (x - a)

        return tangent

    functions = [g]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-2,
        xmax=5,
        ymin=-3,
        ymax=6,
        ticks=False,
    )

    x = np.linspace(-10, 10, 1024)

    x1 = 2
    tangent1 = make_tangent_fn(a=x1)

    ax.plot(x, tangent1(x), color="blue", lw=2, alpha=0.7)
    ax.plot(x1, g(x1), "ko", markersize=8, alpha=0.7)

    dx = 0.2
    dy = 0.2
    ax.text(
        x=x1,
        y=g(x1) - dy,
        s="$(2, g(2))$",
        fontsize=16,
        ha="center",
        va="top",
    )

    x1 = 0
    tangent2 = make_tangent_fn(a=x1)
    ax.plot(x, tangent2(x), color="red", lw=2, alpha=0.7)
    ax.plot(x1, g(x1), "ko", markersize=8, alpha=0.7)

    ax.text(
        x=0.5,
        y=3,
        s="$y = -4x + 3$",
        color="red",
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
