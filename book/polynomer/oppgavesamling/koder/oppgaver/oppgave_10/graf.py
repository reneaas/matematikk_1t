import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return x**3 - 32 * x

    # List of functions and their labels.
    functions = []

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-1,
        xmax=np.sqrt(32) + 1,
        ymin=-80,
        ymax=6,
        ticks=False,
    )

    x = np.linspace(0, np.sqrt(32), 1024)

    x0 = 2
    A = [0, 0]
    B = [x0, 0]
    C = [x0, f(x0)]

    ax.fill([A[0], B[0], C[0]], [A[1], B[1], C[1]], color="teal", alpha=0.1)
    ax.plot([A[0], B[0]], [A[1], B[1]], color="black", lw=1.5, alpha=0.7)
    ax.plot([B[0], C[0]], [B[1], C[1]], color="black", lw=1.5, alpha=0.7)
    ax.plot([C[0], A[0]], [C[1], A[1]], color="black", lw=1.5, alpha=0.7)

    ax.plot(*A, "ko", markersize=8, alpha=0.7)
    ax.plot(*B, "ko", markersize=8, alpha=0.7)
    ax.plot(*C, "ko", markersize=8, alpha=0.7)

    dx = dy = 0.1
    ax.text(
        x=C[0] - dx,
        y=C[-1] - dy,
        s="$(2, f(2))$",
        fontsize=16,
        ha="right",
        va="top",
    )

    dx = dy = 0.1
    ax.text(
        x=B[0],
        y=B[-1] + 5 * dy,
        s="$(2, 0)$",
        fontsize=16,
        ha="center",
        va="bottom",
    )

    ax.plot(x, f(x), color="teal", lw=2, alpha=0.7)

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
