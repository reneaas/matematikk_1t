import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    @np.vectorize
    def f(x):
        teller = x**2 + 1
        nevner = (x + 2) * (x - 2)
        if nevner != 0:
            return teller / nevner - 1
        else:
            return None

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=["D"],
        xmin=-10,
        xmax=10,
        ymin=-10,
        ymax=10,
        ticks=False,
    )

    ax.vlines(x=-2, ymin=-25, ymax=25, color=plotmath.COLORS.get("red"), ls="--", lw=2)
    ax.vlines(x=2, ymin=-25, ymax=25, color=plotmath.COLORS.get("red"), ls="--", lw=2)
    # ax.hlines(y=2, xmin=-25, xmax=25, color=plotmath.COLORS.get("red"), ls="--")
    # ax.vlines(x=-2, ymin=-25, ymax=25, color=plotmath.COLORS.get("red"), ls="--")

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
