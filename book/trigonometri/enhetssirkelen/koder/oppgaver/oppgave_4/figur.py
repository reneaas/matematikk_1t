import plotmath
import matplotlib.pyplot as plt
import numpy as np
from casify import *


def main(dirname, save):

    def make_circle(radius):
        theta = np.linspace(0, 2 * np.pi, 1024)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        return x, y

    def make_circle_arc(radius, start, end):
        theta = np.linspace(start, end, 1024)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        return x, y

    fig, ax = plotmath.plot(
        functions=[],
        fn_labels=False,
        ticks=False,
        grid=False,
    )

    ax.set_xlabel("$x$", loc="right", fontsize=16)
    ax.set_ylabel("$y$", loc="top", fontsize=16)

    r = 1

    x, y = make_circle(radius=r)
    ax.plot(x, y, color="teal", lw=2)

    angle = 150
    A = (0, 0)
    B = (1, 0)
    C = (np.cos(np.deg2rad(angle)), np.sin(np.deg2rad(angle)))
    points = [A, B, C]
    plotmath.plot_polygon(
        *points,
        ax=ax,
        show_vertices=False,
    )

    x, y = make_circle_arc(radius=0.1, start=0, end=np.deg2rad(angle))
    ax.plot(x, y, color="black", lw=1)

    ax.text(
        x=0.15,
        y=0.15,
        s="$150^\\circ$",
        fontsize=16,
        ha="center",
        va="center",
    )

    ax.plot(
        *C,
        "ko",
        markersize=8,
        alpha=0.7,
    )

    ax.text(
        *C,
        s=r"$P \left(-\frac{\sqrt{3}}{2}, \frac{1}{2} \right)$",
        fontsize=18,
        ha="right",
        va="bottom",
    )

    plt.axis("equal")

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
