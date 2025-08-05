import plotmath
import matplotlib.pyplot as plt
import numpy as np


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return (x + 1) ** 2 - 3

    dfdx = lambda x: 2 * (x + 1)

    x0 = 1

    slope = dfdx(x0)

    def T(x):
        return slope * (x - x0) + f(x0)

    # List of functions and their labels.
    functions = [f, T]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-5,
        xmax=4,
        ymin=-6,
        ymax=8,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    x = np.linspace(-10, 10, 1024)
    color = plotmath.COLORS.get("red")
    ax.plot(x0, f(x0), "ko", markersize=10, alpha=0.7)
    ax.text(
        x0 + 0.2,
        f(x0),
        f"$(x_0, f(x_0))$",
        fontsize=25,
        va="center",
        ha="left",
    )

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(25)  # Set to desired font size

    ax.yaxis.label.set_size(25)  # Set y-axis label font size
    ax.xaxis.label.set_size(25)  # Set x-axis label font size
    ax.legend(fontsize=25)

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
