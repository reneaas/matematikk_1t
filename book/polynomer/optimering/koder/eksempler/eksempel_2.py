import plotmath
import matplotlib.pyplot as plt
import numpy as np


def main(dirname, save):

    dx = 0.6
    x = 4
    y = 1
    dx = 0.4 * x

    A = (0, 0)
    B = (x, 0)
    C = (x, y)
    D = (0, y)

    # Lines
    plt.plot([A[0], B[0]], [A[1], B[1]], color="black", lw=2)
    plt.plot([B[0], C[0]], [B[1], C[1]], color="black", lw=2)
    plt.plot([C[0], D[0]], [C[1], D[1]], color="black", lw=2)
    plt.plot([D[0], A[0]], [D[1], A[1]], color="black", lw=2)

    plt.text(
        x=0.5 * (A[0] + B[0]),
        y=0.5 * (A[1] + B[1]) - 0.1,
        s="$x$",
        fontsize=20,
        color="black",
    )

    plt.text(
        x=0.5 * (B[0] + C[0]) + 0.2,
        y=0.5 * (B[1] + C[1]),
        s="$y$",
        fontsize=20,
        color="black",
    )

    plt.axis("off")
    plt.xlim(-0.3, 4.3)
    plt.ylim(-0.1, 1.1)
    plt.tight_layout()

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname, fname=fname
        )  # Lagrer figuren i `dirname`-directory

    if not save:

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
