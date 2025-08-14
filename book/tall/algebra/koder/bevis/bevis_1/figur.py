import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here

    fig, ax = plt.subplots(figsize=(8, 3))

    a = 2
    b = 4
    c = 2.5

    A = (0, 0)
    B = (b, 0)
    C = (b, a)
    D = (0, a)

    plotmath.plot_polygon(
        A,
        B,
        C,
        D,
        color=plotmath.COLORS.get("blue"),
        alpha=0.3,
    )

    A = (b, 0)
    B = (b + c, 0)
    C = (b + c, a)
    D = (b, a)

    plotmath.plot_polygon(
        A,
        B,
        C,
        D,
        color=plotmath.COLORS.get("red"),
        alpha=0.3,
    )

    plt.text(
        x=0 - 0.2,
        y=a / 2,
        s=r"$a$",
        fontsize=25,
        ha="right",
        va="center",
    )

    plt.text(
        x=0.5 * b,
        y=-0.2,
        s=r"$b$",
        fontsize=25,
        ha="center",
        va="top",
    )

    plt.text(
        x=b + 0.5 * c,
        y=-0.2,
        s=r"$c$",
        fontsize=25,
        ha="center",
        va="top",
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
