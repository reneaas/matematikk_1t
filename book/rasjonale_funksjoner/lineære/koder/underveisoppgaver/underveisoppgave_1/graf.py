import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    @np.vectorize
    def f(x, vertical_asymptote=1, horisontal_asymptote=2, zero=-2):
        if x == vertical_asymptote:
            return None
        else:
            return horisontal_asymptote * (x - zero) / (x - vertical_asymptote)

    # List of functions and their labels.
    functions = []

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-9,
        xmax=9,
        ymin=-9,
        ymax=9,
        ticks=True,
    )

    vertical_asymptote = -1
    horisontal_asymptote = 2
    zero = 3

    x1 = np.linspace(-10, vertical_asymptote, 1024)
    x2 = np.linspace(vertical_asymptote, 10, 1024)

    ax.plot(
        x1,
        f(
            x1,
            vertical_asymptote=vertical_asymptote,
            horisontal_asymptote=horisontal_asymptote,
            zero=zero,
        ),
        color=plotmath.COLORS.get("blue"),
        lw=2.5,
        label="$f$",
    )
    ax.plot(
        x2,
        f(
            x2,
            vertical_asymptote=vertical_asymptote,
            horisontal_asymptote=horisontal_asymptote,
            zero=zero,
        ),
        color=plotmath.COLORS.get("blue"),
        lw=2.5,
    )

    ax.hlines(
        y=horisontal_asymptote,
        xmin=-10,
        xmax=10,
        linestyle="--",
        lw=2,
        color=plotmath.COLORS.get("red"),
    )
    ax.vlines(
        x=vertical_asymptote,
        ymin=-12,
        ymax=12,
        linestyle="--",
        lw=2,
        color=plotmath.COLORS.get("red"),
    )

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
