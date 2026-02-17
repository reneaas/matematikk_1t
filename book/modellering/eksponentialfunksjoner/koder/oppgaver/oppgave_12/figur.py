import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here
    fig, ax = plt.subplots(figsize=(8, 2))
    s = 1
    step = 1
    for i in range(1, 10):
        A = (step * i + s * i, 0)
        B = (step * i + s * (i + 1), 0)
        C = (step * i + s * (i + 1), s)
        D = (step * i + s * i, s)

        plotmath.plot_polygon(
            *[A, B, C, D],
            alpha=0.2,
        )

        s = 0.7 * s

    plt.axis("equal")
    plt.axis("off")

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
