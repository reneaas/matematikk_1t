import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -((x - 1) ** 2) + 4

    def make_tangent_fn(f, a):
        slope = 0.5 * (f(a + 1) - f(a - 1))

        def tangent(x):
            return f(a) + slope * (x - a)

        return tangent

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-4,
        xmax=6,
        ymin=-4,
        ymax=14,
        ticks=False,
    )

    tangent1 = make_tangent_fn(f, -1)
    x = np.linspace(-10, 10, 1024)

    tangent2 = make_tangent_fn(f, 3)

    ax.plot(-1, 0, "ko", markersize=8, alpha=0.7)
    ax.plot(3, 0, "ko", markersize=8, alpha=0.7)
    ax.plot(x, tangent1(x), lw=2, alpha=0.7, ls="--", color="blue")
    ax.plot(x, tangent2(x), lw=2, alpha=0.7, ls="--", color="red")

    ax.text(
        x=-2,
        y=4,
        s="$y = 4x + 4$",
        fontsize=16,
        color="blue",
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
