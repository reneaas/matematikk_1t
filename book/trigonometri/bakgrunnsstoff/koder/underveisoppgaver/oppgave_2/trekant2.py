from casify import *
import numpy as np


def scaling_matrix(s):
    return np.array([[s, 0], [0, s]])


def main(dirname, save):
    # TODO: write code here
    import plotmath
    import sympy

    # T = np.einsum("ij,jk->ik", rotation_matrix(np.pi / 2), reflection_matrix())
    # T = np.einsum(
    #     "ij,jk,kl->il",
    #     rotation_matrix(np.pi / 2),
    #     reflection_matrix(),
    #     scaling_matrix(0.5),
    # )

    T = scaling_matrix(2)

    A = (0, 0)
    B = (1, 0)
    C = (1, 2)

    B = (B[1], B[0])
    C = (C[1], C[0])

    A = np.array(A)
    B = np.array(B)
    C = np.array(C)

    A = np.einsum("ij,j->i", T, A)
    B = np.einsum("ij,j->i", T, B)
    C = np.einsum("ij,j->i", T, C)

    ax = draw_triangle(
        A,
        B,
        C,
        show=True if save is False else False,
        radius=0.5,
        fontsize=16,
        label_angles=(False, False, True),
        label_sides=(False, False, True),
        vertex_labels=("D", "E", "F"),
    )

    # NOTE: Automatically saves with correct file format and filename.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname, fname=fname
        )  # Lagrer figuren i `dirname`-directory


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
