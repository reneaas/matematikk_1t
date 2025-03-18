from casify import *


def main(dirname, save):
    # TODO: write code here
    import plotmath
    import numpy as np

    angle = 150
    r = 10
    A = (0, 0)
    B = (r, 0)
    C = (r * np.cos(np.deg2rad(angle)), r * np.sin(np.deg2rad(angle)))
    points = [A, B, C]

    ax = draw_triangle(
        *points,
        show=False,
        radius=3,
        fontsize=16,
        label_angles=(False, True, True),
        label_sides=(False, True, False),
        vertex_labels=(False, False, False),
        numerical_len=True,
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
