import plotmath
import matplotlib.pyplot as plt


def main(dirname, save):
    fontsize = 20
    # List of functions and their labels.
    A = (0, 0)
    C = (0, 2)
    B = (3, 0)

    plotmath.plot_polygon(A, B, C, show_vertices=True)

    dx = dy = 0.1
    plt.text(
        x=A[0] - dx,
        y=A[1] - dy,
        s="$A$",
        fontsize=fontsize,
        ha="right",
        va="center",
    )

    plt.text(
        x=B[0] + dx,
        y=B[1] - dy,
        s="$B$",
        fontsize=fontsize,
        ha="left",
        va="center",
    )

    plt.text(
        x=C[0] - dx,
        y=C[1] + dy,
        s="$C$",
        fontsize=fontsize,
        ha="left",
        va="center",
    )

    plt.text(
        x=0.5 * (A[0] + B[0]),
        y=0.5 * (A[1] + B[1]) - dy,
        s="$c$",
        fontsize=fontsize,
        ha="center",
        va="top",
    )

    plt.text(
        x=0.5 * (A[0] + C[0]) - dx,
        y=0.5 * (A[1] + C[1]),
        s="$b$",
        fontsize=fontsize,
        ha="right",
        va="center",
    )

    plt.text(
        x=0.5 * (B[0] + C[0]),
        y=0.5 * (B[1] + C[1]) + dy,
        s="$a$",
        fontsize=fontsize,
        ha="left",
        va="bottom",
    )

    dx = dy = 0.2
    plt.plot([0, dx], [dy, dy], "k")
    plt.plot([dx, dx], [0, dy], "k")

    plt.axis("equal")
    plt.axis("off")

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
