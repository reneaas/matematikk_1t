import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return 0.5 * (x + 1) ** 2 + 1

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

    def make_secant_fn(x1, x2):
        y1 = f(x1)
        y2 = f(x2)
        slope = (y2 - y1) / (x2 - x1)
        intercept = y1 - slope * x1

        print(slope)
        print(intercept)

        def secant(x):
            return y1 + slope * (x - x1)

    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=["$h$"],
        xmin=-6,
        xmax=4,
        ymin=-2,
        ymax=8,
        ticks=False,
    )

    x = np.linspace(-10, 10, 1024)

    x1 = 1
    tangent1 = make_tangent_fn(a=x1)

    ax.plot(x, tangent1(x), color="blue", lw=2, alpha=0.7)
    ax.plot(x1, f(x1), "ko", markersize=8, alpha=0.7)

    x1 = -3
    tangent2 = make_tangent_fn(a=x1)
    ax.plot(x, tangent2(x), color="red", lw=2, alpha=0.7)
    ax.plot(x1, f(x1), "ko", markersize=8, alpha=0.7)

    dx = 0.2
    dy = 0.2
    ax.text(
        x=x1,
        y=f(x1) + dy,
        s="$(-3, h(-3))$",
        fontsize=16,
        ha="left",
        va="bottom",
    )

    ax.text(
        x=-5.5,
        y=2,
        s="$y = -2x + 3$",
        color="red",
        fontsize=18,
    )

    ax.hlines(y=f(-3), xmin=1, xmax=2, linestyle="--", color="blue", alpha=0.7)
    ax.vlines(x=2, ymin=f(-3), ymax=f(-3) + 2, linestyle="--", color="blue", alpha=0.7)

    ax.text(
        x=0.5 * (1 + 2),
        y=f(-3) - dy,
        s="$1$",
        fontsize=16,
        ha="center",
        va="top",
        color="blue",
    )

    ax.text(
        x=2 + dx,
        y=0.5 * (2 * f(-3) + 2),
        s="$2$",
        fontsize=16,
        ha="left",
        va="center",
        color="blue",
    )

    ax.plot(-1, 2 * (-1) + 1, "ko", markersize=8, alpha=0.7)
    ax.text(
        x=-1 - dy,
        y=2 * (-1) + 1,
        s="$(-1, -1)$",
        fontsize=16,
        ha="right",
        va="center",
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
