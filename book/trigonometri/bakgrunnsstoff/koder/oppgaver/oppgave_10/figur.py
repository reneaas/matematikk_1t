from casify import *


def main(dirname, save):
    # TODO: write code here
    import plotmath
    import matplotlib.pyplot as plt

    ax = draw_triangle(
        asa=(60, 10, 30),
        show=False,
        radius=0.8,
        fontsize=20,
        label_angles=(False, True, False),
        label_sides=(False, "y", "x"),
        vertex_labels=("A", "B", "C"),
    )

    r = 5 / 2
    h = 5 * 3**0.5 / 2
    ax.vlines(
        x=r,
        ymin=0,
        ymax=h,
        color="black",
        linestyle="--",
    )

    dx = dy = 0.5
    ax.plot([r, r + dx], [dy, dy], color="black", linestyle="--")
    ax.plot([r + dx, r + dx], [+0, dy], color="black", linestyle="--")

    ax.text(
        x=r,
        y=0 - 0.5 * dy,
        s="$D$",
        fontsize=20,
        ha="center",
        va="top",
    )

    ax.plot(r, 0, "ko", markersize=8, alpha=0.7)

    ax.text(
        x=r + 0.5 * dx,
        y=0.5 * h,
        s="$z$",
        fontsize=20,
        ha="left",
        va="center",
    )

    plt.annotate(
        "",
        xy=(0, -1),
        xycoords="data",
        xytext=(10, -1),
        textcoords="data",
        arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="black"),
    )

    ax.text(
        x=0.5 * 10,
        y=-1.5,
        s="$10$",
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
