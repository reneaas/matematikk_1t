import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here

    fig, ax = plt.subplots(figsize=(8, 2))

    step = 4
    dx = 2
    dy = 1
    A = (0, 0)
    B = (dx, 0)
    C = (dx, dy)
    D = (0, dy)

    x_mid = (A[0] + C[0]) / 2
    y_mid = (A[1] + C[1]) / 2

    plt.text(
        x=x_mid,
        y=y_mid,
        s="$ax^2 + bx + c$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plotmath.plot_polygon(
        *[A, B, C, D],
        color="teal",
        alpha=0.05,
        show_vertices=False,
    )

    plt.annotate(
        r"",
        xy=(step, 0.5 * dy),
        xytext=(C[0], 0.5 * dy),
        fontsize=20,
        ha="center",
        va="center",
        arrowprops=dict(arrowstyle="->", lw=1.5),
    )

    plt.text(
        x=0.5 * (C[0] + step),
        y=0.5 * dy,
        s="Fullstendig \nkvadraters \nmetode",
        fontsize=20,
        ha="center",
        va="bottom",
    )

    A = (step, 0)
    B = (step + dx, 0)
    C = (step + dx, dy)
    D = (step, dy)
    x_mid = (A[0] + C[0]) / 2
    y_mid = (A[1] + C[1]) / 2

    plt.text(
        x=x_mid,
        y=y_mid,
        s="$a(x - x_0)^2 + y_0$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plotmath.plot_polygon(
        *[A, B, C, D],
        color="blue",
        alpha=0.05,
        show_vertices=False,
    )

    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()

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
