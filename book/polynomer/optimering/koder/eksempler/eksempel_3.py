import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -(x**2) + 9

    # List of functions and their labels.
    functions = []

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-1,
        xmax=4,
        ymin=-2,
        ymax=10,
        ticks=False,
    )

    x = np.linspace(0, 3, 1024)
    y = f(x)

    x0 = 2.5
    A = [0, 0]
    B = [x0, 0]
    C = [x0, f(x0)]
    D = [0, f(x0)]

    plt.plot(*A, "ko", markersize=8, alpha=0.7)
    plt.plot(*B, "ko", markersize=8, alpha=0.7)
    plt.plot(*C, "ko", markersize=8, alpha=0.7)
    plt.plot(*D, "ko", markersize=8, alpha=0.7)

    plt.fill(
        [A[0], B[0], C[0], D[0]],
        [A[1], B[1], C[1], D[1]],
        color="teal",
        alpha=0.2,
    )

    plt.plot([A[0], B[0]], [A[1], B[1]], color="black", lw=2)
    plt.plot([B[0], C[0]], [B[1], C[1]], color="black", lw=2)
    plt.plot([C[0], D[0]], [C[1], D[1]], color="black", lw=2)
    plt.plot([D[0], A[0]], [D[1], A[1]], color="black", lw=2)

    dx = dy = 0.2
    ax.text(
        x=x0 + dx,
        y=f(x0),
        s="$(a, f(a))$",
        fontsize=16,
        color="black",
        ha="left",
        va="bottom",
    )

    ax.plot(x, y, color="teal", lw=2, alpha=0.7, label="$f(x) = -x^2 + 9$")

    plt.legend(fontsize=16)

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
