import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here

    A = (0, 0)
    B = (2, 0)
    C = (1, np.sqrt(3))

    plotmath.plot_polygon(
        A,
        B,
        C,
        alpha=0,
    )

    M = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2

    ax = plt.gca()
    ax.plot(*zip(M, C), color="black", lw=1.5, ls="--")

    dx = dy = 0.2
    plt.plot([1 - dx, 1 - dx], [0, dy], color="black", lw=1.5, ls="-")
    plt.plot([1, 1 - dx], [dy, dy], color="black", lw=1.5, ls="-")

    ax.text(
        x=0.5 * (A[0] + B[0]),
        y=0.5 * (A[1] + B[1]) - 0.1,
        s="$2$",
        fontsize=20,
        ha="center",
        va="top",
    )

    ax.text(
        x=0.5 * (A[0] + C[0]) - 0.2,
        y=0.5 * (A[1] + C[1]),
        s="$2$",
        fontsize=20,
        ha="center",
        va="center",
    )

    ax.text(
        x=0.5 * (B[0] + C[0]) + 0.2,
        y=0.5 * (B[1] + C[1]),
        s="$2$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.axis("equal")
    plt.axis("off")

    # NOTE: Automatically saves with correct file format and filename.
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
