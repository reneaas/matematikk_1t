import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions

    def make_circle(radius, x0, y0):
        theta = np.linspace(0, 2 * np.pi, 1024)
        x = radius * np.cos(theta) + x0
        y = radius * np.sin(theta) + y0
        return x, y

    # List of functions and their labels.
    functions = []

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-7,
        xmax=7,
        ymin=-7,
        ymax=7,
        ticks=False,
    )

    x, y = make_circle(radius=5, x0=0, y0=0)
    ax.plot(x, y, label=r"$x^2 + y^2 = 25$", color=plotmath.COLORS.get("blue"), lw=2.5)

    x = np.linspace(-10, 10, 1024)
    y = x - 1

    ax.plot(x, y, label=r"$x - y = 1$", color=plotmath.COLORS.get("red"), lw=2.5)

    ax.legend(fontsize=16)

    ax.axis("equal")

    xticks = [i for i in range(-7, 8, 1)]
    if 0 in xticks:
        xticks.remove(0)

    xtickslabels = [f"${i}$" for i in xticks]

    yticks = [i for i in range(-5, 6, 1)]
    if 0 in yticks:
        yticks.remove(0)

    ytickslabels = [f"${i}$" for i in yticks]

    ax.set_xticks(xticks)
    ax.set_xticklabels(xtickslabels, fontsize=16)

    ax.set_yticks(yticks)
    ax.set_yticklabels(ytickslabels, fontsize=16)

    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)

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
