import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -x * (x - 3) ** 3

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-0.5,
        xmax=3.5,
        ymin=-4,
        ymax=10,
        ticks=False,
        domain=[0, 3],
    )

    x0 = 2
    A = [0, 0]
    B = [x0, 0]
    C = [x0, f(x0)]

    ax.plot(*A, "ko", markersize=8, alpha=0.7)
    ax.plot(*B, "ko", markersize=8, alpha=0.7)
    ax.plot(*C, "ko", markersize=8, alpha=0.7)

    ax.fill(
        [A[0], B[0], C[0]],
        [A[1], B[1], C[1]],
        color="skyblue",
        alpha=0.4,
    )

    ax.plot([A[0], B[0]], [A[1], B[1]], color="black", lw=1.5)
    ax.plot([B[0], C[0]], [B[1], C[1]], color="black", lw=1.5)
    ax.plot([C[0], A[0]], [C[1], A[1]], color="black", lw=1.5)

    ax.text(
        x=x0 + 0.05,
        y=f(x0),
        s="$(2, f(2))$",
        fontsize=16,
        color="black",
        ha="left",
        va="bottom",
    )

    ticks = [i for i in range(1, 4, 1)]
    try:
        ticks.remove(0)
    except:
        pass
    ax.set_xticks(ticks)
    ax.tick_params(axis="x", labelsize=16)
    ax.grid(False)

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
