import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here

    fig, ax = plt.subplots(figsize=(3, 3))
    a = 2

    A = (-0.5 * a, 0)
    B = (0.5 * a, 0)
    C = (0, np.sqrt(3) * 0.5 * a)

    ax.plot(*zip(A, B, C, A), color="black", lw=1)

    # plotmath.plot_polygon(
    #     A,
    #     B,
    #     C,
    #     alpha=0,
    # )

    a = a / 2
    A = (-0.5 * a, np.sqrt(3) * 0.5 * a)
    B = (0.5 * a, np.sqrt(3) * 0.5 * a)
    C = (0, 0)

    # plotmath.plot_polygon(
    #     A,
    #     B,
    #     C,
    #     alpha=0,
    # )

    ax.plot(*zip(A, B, C, A), color="black", lw=1)

    for i in range(10):
        h = np.sqrt(3) * 0.5 * a
        h = A[1]
        a = a / 2
        if i % 2 == 0:
            A = (-0.5 * a, h - np.sqrt(3) * 0.5 * a)
            B = (0.5 * a, h - np.sqrt(3) * 0.5 * a)
            C = (0, h)

            ax.plot(*zip(A, B, C, A), color="black", lw=1)
        else:
            A = (-0.5 * a, h + np.sqrt(3) * 0.5 * a)
            B = (0.5 * a, h + np.sqrt(3) * 0.5 * a)
            C = (0, h)

            ax.plot(*zip(A, B, C, A), color="black", lw=1)

    plt.axis("off")
    plt.axis("equal")
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
