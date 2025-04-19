from casify import *
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here
    import plotmath

    A = (0, 0)
    B = (1, 0)
    C = (1, 2)

    ax = draw_triangle(
        A,
        B,
        C,
        show=False,
        radius=0.3,
        fontsize=22,
        label_angles=(" ", True, False),
        label_sides=(True, True, True),
        vertex_labels=("A", "B", "C"),
    )

    plt.text(
        x=0.45,
        y=0.25,
        s="$63.43^\\circ$",
        fontsize=22,
        ha="center",
        va="center",
    )

    plt.tight_layout()
    # NOTE: Automatically saves with correct file format and filename.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname, fname=fname
        )  # Lagrer figuren i `dirname`-directory
    else:
        plt.show()


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
