from casify import *


def main(dirname, save):
    # TODO: write code here
    import plotmath
    import numpy as np

    angle = 120
    A = (0, 0)
    B = (4, 0)
    C = (4 * np.cos(np.deg2rad(angle)), 4 * np.sin(np.deg2rad(angle)))
    ax = draw_triangle(
        asa=(120, 4, 30),
        show=False,
        radius=0.85,
        fontsize=20,
        label_angles=(True, True, False),
        label_sides=(True, False, False),
        vertex_labels=(False, "B", "C"),
        numerical_len=False,
    )

    ax.text(
        x=0 - 0.1,
        y=0 - 0.1,
        s=r"$A$",
        fontsize=20,
        va="top",
        ha="right",
    )

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
