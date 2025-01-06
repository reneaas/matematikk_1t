import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -((x - 3) ** 2) + 1

    def make_secant_fn(f, x1, x2):
        y1 = f(x1)
        y2 = f(x2)
        slope = (y2 - y1) / (x2 - x1)

        def secant(x):
            return y1 + slope * (x - x1)

        return secant

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-1,
        xmax=6,
        ymin=-5,
        ymax=3,
        ticks=False,
    )

    x = np.linspace(-10, 10, 1024)
    x1 = 1
    x2 = 3
    secant1 = make_secant_fn(f=f, x1=x1, x2=x2)

    ax.plot(x1, f(x1), "ko", markersize=8, alpha=0.7)
    ax.plot(x2, f(x2), "ko", markersize=8, alpha=0.7)
    ax.plot(x, secant1(x), color="blue", lw=2, alpha=0.7)

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
