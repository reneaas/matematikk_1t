import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here

    fig, ax = plt.subplots(figsize=(4, 3))

    a = 2
    b = 4
    c = 3
    d = 1

    # Rectangle 1
    A = (0, 0)
    B = (a, 0)
    C = (a, c)
    D = (0, c)
    plotmath.plot_polygon(
        A,
        B,
        C,
        D,
        color=plotmath.COLORS.get("blue"),
        alpha=0.3,
    )

    # Rectangle 2
    A = (a, 0)
    B = (a + b, 0)
    C = (a + b, c)
    D = (a, c)

    plotmath.plot_polygon(
        A,
        B,
        C,
        D,
        color=plotmath.COLORS.get("red"),
        alpha=0.3,
    )

    # Rectangle 3
    A = (0, c)
    B = (0, c + d)
    C = (a, c + d)
    D = (a, c)
    plotmath.plot_polygon(
        A,
        B,
        C,
        D,
        color=plotmath.COLORS.get("green"),
        alpha=0.3,
    )

    # Rectangle 4
    A = (a, c)
    B = (a, c + d)
    C = (a + b, c + d)
    D = (a + b, c)

    plotmath.plot_polygon(
        A,
        B,
        C,
        D,
        color="gray",
        alpha=0.3,
    )

    plt.text(
        x=0 - 0.2,
        y=c / 2,
        s=r"$c$",
        fontsize=14,
        ha="right",
        va="center",
    )

    plt.text(
        x=0.5 * a,
        y=-0.2,
        s=r"$a$",
        fontsize=14,
        ha="center",
        va="top",
    )

    plt.text(
        x=a + 0.5 * b,
        y=-0.2,
        s=r"$b$",
        fontsize=14,
        ha="center",
        va="top",
    )

    plt.text(
        x=0 - 0.2,
        y=c + 0.5 * d,
        s=r"$d$",
        fontsize=14,
        ha="right",
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
