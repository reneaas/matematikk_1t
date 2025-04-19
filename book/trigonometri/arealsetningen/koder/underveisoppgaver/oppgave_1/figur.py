from casify import *


def main(dirname, save):
    # TODO: write code here
    import plotmath
    import numpy as np

    ax = draw_triangle(
        sas=(2, 60, 4),
        show=False,
        radius=0.3,
        fontsize=20,
        label_angles=(False, False, False),
        label_sides=(True, False, False),
        vertex_labels=("A", "B", "C"),
        show_vertices=False,
    )

    angle = np.radians(60)
    h = 2 * np.sin(angle)
    x = 2 * np.cos(angle)
    ax.vlines(x=x, ymin=0, ymax=h, linestyle="--", color="black")

    dx = 0.1
    ax.text(
        x=x + dx,
        y=0.5 * h,
        s=r"$1$",
        fontsize=20,
        ha="left",
        va="center",
    )

    dx = dy = 0.2
    ax.plot([x, x + dx], [dy, dy], color="black")
    ax.plot([x + dx, x + dx], [0, dy], color="black")

    import matplotlib.pyplot as plt

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
