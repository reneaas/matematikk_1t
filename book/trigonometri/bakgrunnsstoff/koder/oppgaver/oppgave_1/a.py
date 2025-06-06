from casify import *
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here
    import plotmath

    ax = draw_triangle(
        asa=(90, 1, 60),
        show=True if save is False else False,
        radius=0.3,
        fontsize=20,
        label_angles=(True, True, False),
        label_sides=(False, False, False),
        vertex_labels=("A", "B", "C"),
        show_vertices=False,
    )

    plt.tight_layout()
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
