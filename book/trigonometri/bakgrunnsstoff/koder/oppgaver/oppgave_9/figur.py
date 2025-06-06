from casify import *


def main(dirname, save):
    # TODO: write code here
    import plotmath
    import matplotlib.pyplot as plt

    ax = draw_triangle(
        asa=(60, 4, 30),
        show=False,
        radius=0.35,
        fontsize=20,
        label_angles=(False, True, False),
        label_sides=(False, True, False),
        vertex_labels=("A", "B", "C"),
    )

    draw_triangle(
        asa=(60, 2, 30),
        show=False,
        radius=0.35,
        fontsize=20,
        label_angles=(False, False, False),
        label_sides=(False, False, True),
        vertex_labels=(False, False, "E"),
    )

    ax.text(
        x=2 + 0.1,
        y=0,
        s="$D$",
        fontsize=20,
        ha="left",
        va="bottom",
    )

    ax.annotate(
        "",
        xy=(0, -0.5),
        xycoords="data",
        xytext=(4, -0.5),
        textcoords="data",
        arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="black"),
    )

    ax.text(
        x=2,
        y=-0.6,
        s="$4$",
        fontsize=20,
        ha="center",
        va="top",
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
