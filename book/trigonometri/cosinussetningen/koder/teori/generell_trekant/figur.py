from casify import *


def main(dirname, save):
    # TODO: write code here
    import plotmath

    ax = draw_triangle(
        asa=(20, 2, 110),
        show=False,
        radius=0.3,
        fontsize=20,
        label_angles=(" ", " ", " "),
        label_sides=("c", "a", "b"),
        vertex_labels=("A", False, "C"),
        numerical_len=False,
        show_vertices=False,
    )

    dx = 0.05
    ax.text(
        x=2 + dx,
        y=0,
        s="$B$",
        fontsize=20,
        ha="left",
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
