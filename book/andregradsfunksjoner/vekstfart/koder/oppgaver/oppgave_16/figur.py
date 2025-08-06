import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    k = 2

    def f(x):
        return -x + k

    def g(x):
        return x + k

    def rf(x):
        return np.array((x, f(x)))

    def rg(x):
        return np.array((x, g(x)))

    # List of functions and their labels.
    functions = [f, g]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-(k + 1),
        xmax=k + 1,
        ymin=-1,
        ymax=k + 1,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    A = (-k, 0)
    B = (k, 0)
    C = (0, k)

    dx = dy = 0.2
    ds = np.sqrt(dx**2 + dy**2)

    angle1 = 45 + 180
    angle2 = angle1 + 90
    point1 = rf(C[0] + dx)
    vx, vy = point1
    v = point1 - np.array(C)
    vx, vy = v

    point2 = point1 - np.array((-vy, vx))

    ax.plot(*zip(point1, point2), "k-", lw=1.5)

    point1 = rg(C[0] - dx)
    vx, vy = point1
    v = point1 - np.array(C)
    vx, vy = v
    point2 = point1 - np.array((vy, -vx))
    ax.plot(*zip(point1, point2), "k-", lw=1.5)

    p = 0.5
    A = (-p * k, 0)
    B = (p * k, 0)
    C = (p * k, f(p * k))
    D = (-p * k, g(-p * k))

    plotmath.plot_polygon(
        A,
        B,
        C,
        D,
        ax=ax,
        alpha=0.7,
        color=plotmath.COLORS.get("skyblue"),
    )

    A = (-k, 0)
    B = (k, 0)
    C = (0, k)

    ax.plot(*A, "ko", markersize=8)
    ax.plot(*B, "ko", markersize=8)
    ax.plot(*C, "ko", markersize=8)

    ax.text(
        A[0] - 0.1,
        A[1] + 0.1,
        r"$A$",
        fontsize=20,
        color="black",
    )

    ax.text(
        B[0] + 0.1,
        B[1] + 0.1,
        r"$B$",
        fontsize=20,
        color="black",
    )

    ax.text(
        C[0] + 0.1,
        C[1] - 0.05,
        r"$C$",
        fontsize=20,
        color="black",
    )

    # ax.axis("equal")

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
