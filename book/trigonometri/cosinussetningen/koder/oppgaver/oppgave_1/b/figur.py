from casify import *


def main(dirname, save):
    # TODO: write code here
    import plotmath

    ax = draw_triangle(
        sas=(4, 70, 6),
        show=False,
        fontsize=16,
        label_angles=(False, False, True),
        label_sides=(True, True, "x"),
        vertex_labels=("A", "B", "C"),
        numerical_len=True,
        show_vertices=False,
        color=plotmath.COLORS.get("common"),
        alpha=0.1,
    )

    # NOTE: Automatically saves with correct file format and filename.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname,
            fname=fname,
            transparent=True,
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
