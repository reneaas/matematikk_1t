import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here

    fig, ax = plt.subplots(figsize=(8, 3))

    x = 1
    y = 2

    A = (0, 0)
    B = (x, 0)
    C = (x + y, 0)
    D = (2 * x + y, 0)

    F = (x, x)
    E = (x + y, x)

    plt.plot([A[0], D[0]], [A[1], D[1]], "k-", lw=2)
    plt.plot([A[0], F[0]], [A[1], F[1]], "k-", lw=2)
    plt.plot([B[0], F[0]], [B[1], F[1]], "k-", lw=2)
    plt.plot([C[0], E[0]], [C[1], E[1]], "k-", lw=2)
    plt.plot([D[0], E[0]], [D[1], E[1]], "k-", lw=2)
    plt.plot([E[0], F[0]], [E[1], F[1]], "k-", lw=2)

    plt.axis("equal")
    plt.axis("off")

    dx = dy = 0.1
    plt.text(
        x=0.5 * (A[0] + B[0]),
        y=-dy,
        s="$x$",
        fontsize=20,
        ha="center",
        va="top",
    )

    plt.text(
        x=0.5 * (B[0] + C[0]),
        y=-dy,
        s="$y$",
        fontsize=20,
        ha="center",
        va="top",
    )

    plt.text(
        x=0.5 * (C[0] + D[0]),
        y=-dy,
        s="$x$",
        fontsize=20,
        ha="center",
        va="top",
    )

    plt.text(
        x=B[0] + dx,
        y=0.5 * (B[1] + F[1]),
        s="$x$",
        fontsize=20,
        ha="left",
        va="center",
    )

    plt.text(
        x=C[0] - dx,
        y=0.5 * (B[1] + F[1]),
        s="$x$",
        fontsize=20,
        ha="right",
        va="center",
    )

    plt.text(
        x=0.5 * (F[0] + E[0]),
        y=F[1] + dy,
        s="$y$",
        fontsize=20,
        ha="center",
        va="bottom",
    )

    dx = dy = 0.15

    x0, y0 = B
    plt.plot(
        [x0 - dx, x0 - dx],
        [y0, y0 + dy],
        "k-",
        lw=1,
    )

    plt.plot(
        [x0 - dx, x0],
        [y0 + dy, y0 + dy],
        "k-",
        lw=1,
    )

    x0, y0 = C
    plt.plot(
        [x0 + dx, x0 + dx],
        [y0, y0 + dy],
        "k-",
        lw=1,
    )
    plt.plot(
        [x0, x0 + dx],
        [y0 + dy, y0 + dy],
        "k-",
        lw=1,
    )

    plt.tight_layout()

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
