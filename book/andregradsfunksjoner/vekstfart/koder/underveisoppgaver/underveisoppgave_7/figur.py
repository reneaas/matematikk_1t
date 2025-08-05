import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -((x + 1) ** 2) + 4

    def f_derivative(x):
        return -2 * (x + 1)

    def make_tangent_fn(f, x0):
        slope = f_derivative(x0)
        intercept = f(x0) - slope * x0
        print(f"y = {slope}x + {intercept}")

        def tangent(x):
            return f(x0) + f_derivative(x0) * (x - x0)

        return tangent

    # List of functions and their labels.
    functions = [f]

    xmin = -6
    xmax = 4
    ymin = -3
    ymax = 9
    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=xmin,
        xmax=xmax,
        ymin=ymin,
        ymax=ymax,
        ticks=False,
        grid=False,
    )

    x1 = -2
    x2 = 1

    tangent1 = make_tangent_fn(f, x1)
    tangent2 = make_tangent_fn(f, x2)

    x = np.linspace(xmin, xmax, 1024)
    ax.plot(x, tangent1(x), linestyle="-", color="gray", alpha=1, lw=2.5)
    ax.plot(
        x,
        tangent2(x),
        linestyle="-",
        color=plotmath.COLORS.get("red"),
        alpha=1,
        lw=2.5,
    )

    ax.plot(x1, f(x1), "ko", markersize=8, alpha=0.7)
    ax.plot(x2, f(x2), "ko", markersize=8, alpha=0.7)

    ax.text(
        x1,
        f(x1),
        f"$({x1}, f({x1}))$",
        fontsize=18,
        verticalalignment="bottom",
        horizontalalignment="right",
    )

    ax.text(
        x=x2 + 0.1,
        y=f(x2) + 2,
        s="$y = -4x + 4$",
        fontsize=18,
        color="red",
    )

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname,
            fname=fname,
            transparent=True,
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
