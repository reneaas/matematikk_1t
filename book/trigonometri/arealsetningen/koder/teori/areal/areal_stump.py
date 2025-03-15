from casify import *


def main(dirname, save):
    # TODO: write code here
    import plotmath
    import numpy as np

    ax = draw_triangle(
        sas=(2, 120, 2),
        show=False,
        radius=0.5,
        fontsize=22,
        label_angles=(False, False, False),
        label_sides=(False, False, False),
        vertex_labels=(False, False, False),
    )

    angle = 120 * np.pi / 180
    h = 2 * np.sin(angle)
    x = 2 * np.cos(angle)
    ax.vlines(x=x, ymin=0, ymax=h, linestyle="--", color="black")
    ax.hlines(y=0, xmin=0, xmax=x, linestyle="--", color="black")

    dx = dy = 0.1
    ax.text(
        x=x - dx,
        y=0.5 * h,
        s=r"$h$",
        fontsize=20,
        ha="right",
        va="center",
    )

    ax.text(
        x=1,
        y=-dy,
        s=r"$g$",
        fontsize=20,
        ha="center",
        va="top",
    )

    dx = dy = 0.2
    ax.plot([x, x + dx], [dy, dy], ls="--", color="black")
    ax.plot([x + dx, x + dx], [dy, 0], ls="--", color="black")

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
