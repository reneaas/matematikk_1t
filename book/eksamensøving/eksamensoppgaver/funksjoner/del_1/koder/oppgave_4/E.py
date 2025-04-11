import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    @np.vectorize
    def f(x):
        teller = x**2 - 1
        nevner = (x + 3) * (x - 2)
        if x != -3 and x != 2:
            return teller / nevner
        else:
            return None

    # List of functions and their labels.
    functions = []

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-8,
        xmax=8,
        ymin=-6,
        ymax=6,
        ticks=False,
    )

    x1 = -3
    x2 = 2
    x = np.linspace(-24, x1, 1024)
    y = f(x)
    ax.plot(x, y, color="teal", alpha=0.9, lw=2, label="E")

    x = np.linspace(x1, x2, 1024)
    y = f(x)
    ax.plot(x, y, color="teal", alpha=0.9, lw=2)

    x = np.linspace(x2, 24, 1024)
    y = f(x)

    ax.plot(x, y, color="teal", alpha=0.9, lw=2)

    ax.vlines(x=-3, ymin=-25, ymax=25, color="blue", ls="--")
    ax.vlines(x=2, ymin=-25, ymax=25, color="blue", ls="--")
    ax.hlines(y=1, xmin=-25, xmax=25, color="blue", ls="--")
    # ax.hlines(y=2, xmin=-25, xmax=25, color="blue", ls="--")
    # ax.vlines(x=-2, ymin=-25, ymax=25, color="blue", ls="--")

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
