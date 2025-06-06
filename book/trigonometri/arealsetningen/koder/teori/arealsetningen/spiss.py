from casify import *
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here
    import plotmath
    import numpy as np

    ax = draw_triangle(
        sas=(1, 50, 2),
        show=False,
        radius=0.25,
        fontsize=22,
        label_angles=(" ", " ", " "),
        label_sides=(False, False, False),
        vertex_labels=("A", "B", "C"),
        show_vertices=False,
    )

    angle = 5 * np.pi / 18
    hypotenuse = np.sqrt(np.cos(angle) ** 2 + np.sin(angle) ** 2)
    h = hypotenuse * np.sin(angle)
    x = hypotenuse * np.cos(angle)
    # ax.vlines(x=x, ymin=0, ymax=h, linestyle="--", color="black")

    dx = dy = 0.05

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
