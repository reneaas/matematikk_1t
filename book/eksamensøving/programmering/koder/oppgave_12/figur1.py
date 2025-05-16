import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    fig, ax = plt.subplots(figsize=(8, 8))
    a = 1  # side length of each small triangle
    n_stories = 5  # number of “stories”

    # equal scaling, no axes
    ax.set_aspect("equal")
    ax.axis("off")

    # height of an equilateral triangle of side a
    h = a * np.sqrt(3) / 2

    # build rows: j=1→1 up-triangle, j=2→3 triangles (up,down,up), etc.
    for j in range(1, n_stories + 1):
        row_count = 2 * j - 1
        row_length = j * a
        x_offset = (n_stories * a - row_length) / 2
        y = (n_stories - j) * h

        for k in range(row_count):
            x = x_offset + k * (a / 2)
            if k % 2 == 0:
                # upright triangle
                tri = [
                    (x, y),
                    (x + a, y),
                    (x + a / 2, y + h),
                ]
            else:
                # inverted triangle
                tri = [
                    (x + a / 2, y),
                    (x, y + h),
                    (x + a, y + h),
                ]
            # close loop and draw
            ax.plot(*zip(*(tri + [tri[0]])), color="black", lw=1)

    plt.tight_layout()

    # save or show
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(dirname=dirname, fname=fname)
    else:
        plotmath.show()


if __name__ == "__main__":
    import pathlib

    current_dir = str(pathlib.Path(__file__).resolve().parent)
    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break
    dirname = "/".join(parts)
    main(dirname=dirname, save=True)
