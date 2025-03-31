import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here

    import matplotlib.patches as patches

    alpha = 0.2

    a = 1
    b = 0.4

    A = (0, 0)
    B = (a - b, 0)
    C = (a - b, a)
    D = (0, a)

    plotmath.plot_polygon(
        A,
        B,
        C,
        D,
        color="teal",
        alpha=alpha,
    )

    A = (a - b, 0)
    B = (a, 0)
    C = (a, b)
    D = (a - b, b)

    plotmath.plot_polygon(
        A,
        B,
        C,
        D,
        color="teal",
        alpha=0,
    )

    A = (a - b, b)
    B = (a, b)
    C = (a, a)
    D = (a - b, a)

    plotmath.plot_polygon(
        A,
        B,
        C,
        D,
        color="teal",
        alpha=alpha,
    )

    dx = dy = 0.1
    plt.text(
        x=-dx,
        y=0.5 * a,
        s="$a$",
        fontsize=20,
        color="black",
        ha="center",
        va="center",
    )

    plt.text(
        x=0.5 * (a - b),
        y=a + dy,
        s="$a-b$",
        fontsize=20,
        color="black",
        ha="center",
        va="center",
    )

    plt.text(
        x=0.5 * (a + a - b),
        y=a + dy,
        s="$b$",
        fontsize=20,
        color="black",
        ha="center",
        va="center",
    )

    plt.text(
        x=a + dy,
        y=(b + 0.5 * (a - b)),
        s="$a - b$",
        fontsize=20,
        color="black",
        ha="left",
        va="center",
    )

    plt.text(
        x=a + dy,
        y=0.5 * b,
        s="$b$",
        fontsize=20,
        color="black",
        ha="left",
        va="center",
    )

    plt.text(
        x=(a - b) + 0.5 * b,
        y=-dy,
        s="$b$",
        fontsize=20,
        color="black",
        ha="center",
        va="center",
    )

    plt.text(
        x=0.5 * (a - b),
        y=-dy,
        s="$b-a$",
        fontsize=20,
        color="black",
        ha="center",
        va="center",
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
