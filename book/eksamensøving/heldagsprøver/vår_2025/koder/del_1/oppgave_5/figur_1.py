import plotmath
import matplotlib.pyplot as plt
import numpy as np
from casify import *


def main(dirname, save):

    fig, ax = plotmath.plot(
        functions=[],
        fn_labels=False,
        ticks=False,
        grid=False,
    )

    def make_circle(radius):
        theta = np.linspace(0, 2 * np.pi, 1024)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        return x, y

    ax.set_xlabel("$x$", loc="right", fontsize=16)
    ax.set_ylabel("$y$", loc="top", fontsize=16)

    # ax.set_xlabel("$\\cos u$", loc="right", fontsize=16)
    # ax.set_ylabel("$\\sin u$", loc="top", fontsize=16)

    r = 1

    x, y = make_circle(radius=r)
    ax.plot(x, y, color="teal", lw=2)

    ax = draw_triangle(
        (0, 0),
        (1, 0),
        (-0.5, np.sqrt(3) / 2),
        radius=0.35,
        show=False,
        label_angles=(True, False, False),
        label_sides=(False, False, False),
        vertex_labels=(False, False, False),
        numerical_len=False,
        axis_off=False,
    )

    ax.text(
        x=-0.5,
        y=np.sqrt(3) / 2,
        s=r"$P\left(-\frac{1}{2}, \frac{\sqrt{3}}{2}\right)$",
        fontsize=22,
        va="bottom",
        ha="right",
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
