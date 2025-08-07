import plotmath
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def main(dirname, save):
    # TODO: write code here

    plt.rc("text", usetex=True)

    a = 1
    b = 0.35

    rect_1 = patches.Rectangle(
        xy=(0, 0),
        width=a - b,
        height=a - b,
        fill=True,
        edgecolor="black",
        facecolor=plotmath.COLORS.get("blue"),
        alpha=0.4,
        lw=2,
    )
    rect_2 = patches.Rectangle(
        xy=(a - b, 0),
        width=b,
        height=a - b,
        fill=True,
        edgecolor="black",
        facecolor=plotmath.COLORS.get("blue"),
        alpha=0.4,
        lw=2,
    )
    rect_3 = patches.Rectangle(
        xy=(0, a - b),
        width=a - b,
        height=b,
        fill=True,
        edgecolor="black",
        facecolor=plotmath.COLORS.get("blue"),
        alpha=0.4,
        lw=2,
    )

    rect_4 = patches.Rectangle(
        xy=(a - b, a - b),
        width=b,
        height=b,
        fill=True,
        edgecolor="black",
        facecolor="gray",
        alpha=0.4,
        lw=2,
    )

    plt.gca().add_patch(rect_1)
    plt.gca().add_patch(rect_2)
    plt.gca().add_patch(rect_3)
    plt.gca().add_patch(rect_4)

    plt.text(
        x=-0.3,
        y=0.5 * a,
        s="$a$",
        fontsize=20,
        color="black",
        ha="center",
        va="center",
    )

    plt.annotate(
        "",
        xy=(-0.2, 0),
        xycoords="data",
        xytext=(-0.2, a),
        textcoords="data",
        arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="black"),
    )

    plt.annotate(
        "",
        xy=(-0.1, a - b),
        xycoords="data",
        xytext=(-0.1, a),
        textcoords="data",
        arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="black"),
    )

    plt.text(
        x=-0.05,
        y=a - 0.5 * b,
        s="$b$",
        fontsize=20,
        color="black",
        ha="center",
        va="center",
    )

    plt.text(
        x=0.5 * a,
        y=-0.1,
        s="$a$",
        fontsize=20,
        color="black",
        ha="center",
        va="center",
    )

    plt.annotate(
        "",
        xy=(0, -0.05),
        xycoords="data",
        xytext=(a, -0.05),
        textcoords="data",
        arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="black"),
    )

    plt.text(
        x=a - 0.5 * b,
        y=a + 0.1,
        s="$b$",
        fontsize=20,
        color="black",
        ha="center",
        va="center",
    )

    plt.annotate(
        "",
        xy=(a - b, a + 0.05),
        xycoords="data",
        xytext=(a, a + 0.05),
        textcoords="data",
        arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="black"),
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
