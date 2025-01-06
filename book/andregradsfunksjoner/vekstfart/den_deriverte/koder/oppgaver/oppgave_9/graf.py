import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -(x**2) + 3 * x + 1

    def make_tangent_fn(f, a, h=1e-5):
        slope = (f(a + h) - f(a - h)) / (2 * h)

        def tangent(x):
            return f(a) + slope * (x - a)

        return tangent

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=["$f$"],
        xmin=-1,
        xmax=4.5,
        ymin=-4,
        ymax=6,
        ticks=False,
    )

    x = np.linspace(-10, 10, 1024)
    x1 = 1
    tangent1 = make_tangent_fn(f=f, a=x1)
    ax.plot(x, tangent1(x), color="blue", linestyle="-", lw=1)
    ax.plot(x1, f(x1), "ro", markersize=8, alpha=0.7)
    ax.text(
        x=x1,
        y=f(x1) + 0.1,
        s="$(1, f(1))$",
        fontsize=16,
        va="bottom",
        ha="right",
    )

    x2 = 3
    tangent2 = make_tangent_fn(f=f, a=x2)
    ax.plot(x, tangent2(x), color="blue", linestyle="-", lw=1)
    ax.plot(x2, f(x2), "ro", markersize=8, alpha=0.7)
    ax.text(
        x=x2 + 0.1,
        y=f(x2),
        s="$(3, f(3))$",
        fontsize=16,
        va="bottom",
        ha="left",
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
