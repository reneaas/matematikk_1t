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

    def f(x):
        return x + 2

    fig, ax = plotmath.plot(
        functions=[f],
        fn_labels=True,
        xmin=-3,
        xmax=6,
        ymin=-1,
        ymax=6,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
    )

    print(f(4) - f(1))

    A = (1, f(1))
    B = (4, f(1))
    C = (4, f(4))

    ax.plot(*A, "o", color="black", markersize=8, label="$A$")
    ax.plot(*B, "o", color="black", markersize=8, label="$B$")
    ax.plot(*C, "o", color="black", markersize=8, label="$C$")

    plotmath.polygon(
        A,
        B,
        C,
        ax=ax,
    )

    dx = dy = 0.45
    x0, y0 = B
    plt.plot([x0 - dx, x0 - dx], [y0, y0 + dy], color="black", lw=1.5)
    plt.plot([x0, x0 - dx], [y0 + dy, y0 + dy], color="black", lw=1.5)

    ax.text(
        x=A[0],
        y=A[1],
        s="$A$",
        fontsize=20,
        ha="right",
        va="bottom",
    )

    ax.text(
        x=B[0],
        y=B[1],
        s="$B$",
        fontsize=20,
        ha="left",
        va="top",
    )

    ax.text(
        x=C[0] + 0.2,
        y=C[1],
        s="$C$",
        fontsize=20,
        ha="left",
        va="center",
    )

    ax.axis("equal")
    ax.axis("off")

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
