from casify import *


def main(dirname, save):
    # TODO: write code here
    import plotmath

    ax = draw_triangle(
        sss=(6, 10, 8),
        show=False,
        radius=1.2,
        fontsize=16,
        label_angles=(False, "v", "u"),
        label_sides=(True, True, True),
        vertex_labels=(False, False, False),
        numerical_len=False,
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
