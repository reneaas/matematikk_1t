import plotmath
import numpy as np


def main(dirname, save):

    # List of functions and their labels.

    @np.vectorize
    def f(x):
        if x != -2 and x != 2:
            return (x**2 - 1) / (x**2 - 4)
        else:
            return None

    xmin = -8
    xmax = 8
    ymin = -8
    ymax = 8

    functions = []
    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=xmin,
        xmax=xmax,
        ymin=ymin,
        ymax=ymax,
        ticks=False,
    )

    x1 = -1
    x2 = 1
    ax.plot(x1, 0, "ko", markersize=8, alpha=0.7)
    ax.plot(x2, 0, "ko", markersize=8, alpha=0.7)

    x_inf1 = -2
    x_inf2 = 2

    x = np.linspace(-20, x_inf1, 1024)
    y = f(x)
    ax.plot(
        x,
        y,
        label=r"$\mathrm{E}$",
        color=plotmath.COLORS.get("blue"),
        lw=2.5,
    )

    x = np.linspace(x_inf1, x_inf2, 1024)
    y = f(x)
    ax.plot(
        x,
        y,
        color=plotmath.COLORS.get("blue"),
        lw=2.5,
    )

    x = np.linspace(x_inf2, 20, 1024)
    y = f(x)
    ax.plot(
        x,
        y,
        color=plotmath.COLORS.get("blue"),
        lw=2.5,
    )

    ax.vlines(
        x=x_inf1,
        ymin=ymin,
        ymax=ymax,
        color=plotmath.COLORS.get("red"),
        linestyle="--",
    )

    ax.vlines(
        x=x_inf2,
        ymin=ymin,
        ymax=ymax,
        color=plotmath.COLORS.get("red"),
        linestyle="--",
    )

    ax.hlines(
        y=1,
        xmin=xmin,
        xmax=xmax,
        color=plotmath.COLORS.get("red"),
        linestyle="--",
    )

    ax.legend(fontsize=16)

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
