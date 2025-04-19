from casify import *
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here
    import plotmath
    import numpy as np

    ax = draw_triangle(
        asa=(60, 4, 60),
        show=False,
        radius=0.55,
        fontsize=20,
        label_angles=(True, True, False),
        label_sides=(True, False, False),
        vertex_labels=("A", "B", "C"),
        show_vertices=False,
    )

    ax.vlines(x=2, ymin=0, ymax=np.sqrt(4**2 - 2**2), linestyle="--", color="black")

    dx = 0.1
    ax.text(
        x=2 + dx,
        y=0.5 * np.sqrt(4**2 - 2**2),
        s="$h$",
        fontsize=20,
        ha="left",
        va="center",
    )

    dx = 0.4
    ax.plot([2, 2 + dx], [dx, dx], ls="--", color="black")
    ax.plot([2 + dx, 2 + dx], [0, dx], ls="--", color="black")

    plt.tight_layout()

    # NOTE: Automatically saves with correct file format and filename.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname, fname=fname
        )  # Lagrer figuren i `dirname`-directory
    else:
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
