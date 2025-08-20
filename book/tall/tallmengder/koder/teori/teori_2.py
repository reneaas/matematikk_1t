import plotmath
import numpy as np
import matplotlib.pyplot as plt
import numpy as np


def main(dirname, save):
    # TODO: write code here

    x_min = -8
    x_max = 8

    x = np.linspace(x_min, x_max, 1024)

    a = -1
    b = 3

    xlim = (-3, 3)
    ylim = (-0.5, 3)

    fig, ax = plt.subplots(figsize=(8, 2))

    ax.spines["left"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.spines["bottom"].set_position("zero")
    ax.spines["top"].set_color("none")

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)

    ax.set_xlabel(r"$x$", fontsize=20, loc="right")

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim(*ylim)
    ax.set_xlim(*xlim)

    ax.annotate(
        text="Mengde",
        xy=(a + 0.5, 0),
        xytext=(a + 0.5, 2.5),
        fontsize=20,
        arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.annotate(
        text="Mengde",
        xy=(a + 1.5, 0),
        xytext=(a + 0.5, 2.5),
        fontsize=20,
        arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.annotate(
        text="Mengde",
        xy=(2.5, 0),
        xytext=(a + 0.5, 2.5),
        fontsize=20,
        arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.hlines(0, a, 10, color=plotmath.COLORS.get("blue"), alpha=0.7, lw=8)
    plt.xticks([a], [r"$a$"], fontsize=20)

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
