import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here

    A = (0, 0)
    B = (4, 0)
    C = (3, 2)

    plotmath.plot_polygon(
        A,
        B,
        C,
        alpha=0.1,
    )

    plt.axis("off")
    plt.axis("equal")
    plt.tight_layout()

    plt.text(
        x=A[0] - 0.1,
        y=A[1] - 0.1,
        s="$A$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.text(
        x=B[0] + 0.1,
        y=B[1] - 0.1,
        s="$B$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.text(
        x=C[0],
        y=C[1] + 0.1,
        s="$C$",
        fontsize=20,
        ha="left",
        va="center",
    )

    plt.vlines(
        x=C[0],
        ymin=0,
        ymax=C[1],
        color="black",
        linestyle="--",
        linewidth=1.5,
    )

    dx = dy = 0.2
    plt.plot(
        [C[0] + dx, C[0] + dx],
        [0, dy],
        color="black",
        linestyle="-",
        linewidth=1.5,
    )

    plt.plot(
        [C[0], C[0] + dx],
        [dy, dy],
        color="black",
        linestyle="-",
        linewidth=1.5,
    )

    plt.text(
        x=C[0] - 0.2,
        y=0.5 * C[1],
        s="$h$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.text(
        x=0.5 * (A[0] + B[0]),
        y=-0.2,
        s="$c$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.text(
        x=0.5 * (A[0] + C[0]),
        y=0.5 * (A[1] + C[1]) + 0.2,
        s="$a$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.text(
        x=0.5 * (B[0] + C[0]) + 0.1,
        y=0.5 * (B[1] + C[1]) + 0.2,
        s="$b$",
        fontsize=20,
        ha="center",
        va="center",
    )

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
