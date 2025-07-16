import plotmath
import numpy as np
import matplotlib.pyplot as plt


def make_circle(center, radius, num_points=1024):
    theta = np.linspace(0, 2 * np.pi, num_points)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)

    return x, y


def main(dirname, save):
    # TODO: write code here

    center = (2, 4)
    radius = 5
    x, y = make_circle(center, radius)

    A = (2, 9)
    B = (5, 0)
    C = (-3, 4)

    def f(x):
        slope = (B[1] - A[1]) / (B[0] - A[0])
        return slope * (x - A[0]) + A[1]

    def g(x):
        slope = (C[1] - A[1]) / (C[0] - A[0])
        return slope * (x - A[0]) + A[1]

    def h(x):
        slope = (C[1] - B[1]) / (C[0] - B[0])
        return slope * (x - B[0]) + B[1]

    fig, ax = plotmath.plot(
        functions=[f, g, h],
        fn_labels=False,
        xmin=-10,
        xmax=10,
        ymin=-10,
        ymax=10,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        domain=False,
    )

    ax.plot(x, y, lw=2, color="black", alpha=0.7)

    ax.text(
        x=A[0] + 0.2,
        y=A[1] + 0.3,
        s="$A$",
        fontsize=20,
        ha="center",
        va="bottom",
    )

    ax.text(
        x=B[0] + 0.2,
        y=B[1] + 0.2,
        s="$B$",
        fontsize=20,
        ha="center",
        va="bottom",
    )

    ax.text(
        x=C[0] + 0.3,
        y=C[1] + 0.1,
        s="$C$",
        fontsize=20,
        ha="left",
        va="center",
    )

    ax.plot(*A, "o", color="black", markersize=8)
    ax.plot(*B, "o", color="black", markersize=8)
    ax.plot(*C, "o", color="black", markersize=8)

    ax.axis("equal")
    ax.set_xlim((-4, 8))
    ax.set_ylim((-2, 10))

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
    main(dirname=dirname, save=False)
