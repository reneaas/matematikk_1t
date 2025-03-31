import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    @np.vectorize
    def f(x):
        if x != 1:
            return 3 * (x - 2) / (x - 1)
        else:
            return None

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=[],
        fn_labels=False,
        xmin=-8,
        xmax=10,
        ymin=-4,
        ymax=9,
        ticks=True,
    )

    x_inf = 1
    x = np.linspace(-24, x_inf, 1024)
    y = f(x)

    ax.plot(x, y, color="teal", alpha=0.7, lw=2)

    x = np.linspace(x_inf, 24, 1024)
    y = f(x)
    ax.plot(x, y, color="teal", alpha=0.7, lw=2)

    ax.hlines(y=3, xmin=-25, xmax=25, color="blue", ls="--")
    ax.vlines(x=1, ymin=-25, ymax=25, color="blue", ls="--")

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
