import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here
    fig, ax = plt.subplots(figsize=(8, 8))
    A = (0, 0)
    angle1 = -60
    angle2 = angle1 - 60
    a = 1
    n_triangles = 1

    n_stories = 5

    for i in range(n_stories):
        n_triangles = 2 * i + 1

        for j in range(n_triangles):
            A = (i * a + a * np.cos(angle), i * a + a * np.sin(angle))
            B = (a * np.cos(angle1), a * np.sin(angle1))
            C = (a * np.cos(angle2), a * np.sin(angle2))

            ax.plot(*zip(A, B, C, A), color="black", lw=1)

        # Update the angle and length for the next triangle
        angle += 60
        a *= 0.5

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
