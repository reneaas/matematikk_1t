import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return x**3 - 3 * x + 4

    def g(x):
        return -3 * x + 4

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-5,
        xmax=5,
        ymin=-3,
        ymax=9,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=False,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    x = [i for i in range(-4, 5)]
    x.remove(0)
    xlabels = [f"${i}$" if i % 2 == 0 else "" for i in x]

    y = [i for i in range(-2, 9)]
    y.remove(0)
    ylabels = [f"${i}$" if i % 2 == 0 else "" for i in y]

    ax.set_xticks(x)
    ax.set_xticklabels(xlabels, fontsize=16)
    ax.set_yticks(y)
    ax.set_yticklabels(ylabels, fontsize=16)

    ax.hlines(y=6, xmin=-10, xmax=10, color=plotmath.COLORS.get("red"), lw=2)
    ax.hlines(y=2, xmin=-10, xmax=10, color=plotmath.COLORS.get("red"), lw=2)

    x = np.linspace(-10, 10, 1024)
    ax.plot(x, g(x), color=plotmath.COLORS.get("red"), lw=2)

    ax.plot(0, 4, "ko", markersize=8, alpha=0.8)
    ax.plot(-1, 6, "ko", markersize=8, alpha=0.8)
    ax.plot(1, 2, "ko", markersize=8, alpha=0.8)

    ax.grid(True, ls="--", alpha=0.8)

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
