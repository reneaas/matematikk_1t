import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return (x - 3) ** 2 - 1

    def make_tangent_fn(f, a, h=2**-8):
        slope = f(a + h) - f(a - h)
        slope *= 0.5 / h
        intercept = f(a) - slope * a
        print(f"{slope = }")
        print(f"{intercept = }")

        def tangent(x):
            return f(a) + slope * (x - a)

        return tangent

    def make_secant_fn(f, x1, x2):
        y1 = f(x1)
        y2 = f(x2)
        slope = (y2 - y1) / (x2 - x1)
        intercept = y1 - slope * x1

        def secant(x):
            return slope * x + intercept

        return secant

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=["$p$"],
        xmin=-4,
        xmax=7,
        ymin=-6,
        ymax=3,
        ticks=False,
    )

    x1 = 2
    x2 = 7 / 8
    x = np.linspace(-10, 10, 1024)
    tangent1 = make_tangent_fn(f=f, a=x1)
    tangent2 = make_tangent_fn(f=f, a=x2)
    ax.plot(x, tangent1(x), color="blue", lw=2, alpha=0.7)
    ax.plot(x, tangent2(x), color="red", lw=2, alpha=0.7)

    dx = 0.2
    dy = 0.5

    ax.plot([])

    # # Annotate points
    # dx = 0.2
    # ax.text(
    #     x=0 - dx,
    #     y=f(0),
    #     s="$(0, 4)$",
    #     fontsize=16,
    #     va="center",
    #     ha="right",
    # )

    # ax.text(
    #     x=x1 + dx,
    #     y=f(x1),
    #     s="$(3, f(3))$",
    #     fontsize=16,
    #     ha="left",
    #     va="center",
    # )

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
    main(dirname=dirname, save=False)
