import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return 8 / (x**2 + 4)

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=[],
        fn_labels=False,
        xmin=-0.5,
        xmax=7,
        ymin=-0.5,
        ymax=3,
        ticks=False,
    )

    x = np.linspace(0, 8, 1024)
    y = f(x)
    ax.plot(x, y, color=plotmath.COLORS.get("blue"), lw=2.5, label="$f$")

    k = 2.6
    A = (0, 0)
    B = (k, 0)
    C = (k, f(k))
    D = (0, f(k))

    points = [A, B, C, D]
    plotmath.plot_polygon(*points, ax=ax, alpha=0.1, show_vertices=True)

    dx = dy = 0.1

    ax.text(
        x=C[0],
        y=C[1] + dy,
        s="$(r, f(r))$",
        fontsize=16,
        va="bottom",
        ha="left",
    )

    xticks = [i for i in range(1, 7)]
    xticklabels = [f"${i}$" for i in xticks]
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels, fontsize=16)

    ax.legend(fontsize=16)
    ax.grid(False)

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
