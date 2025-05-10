import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here

    # Create a star consisting of 12 equilateral triangles
    fig, ax = plt.subplots()
    ax.set_aspect("equal")

    angles = np.linspace(0, 2 * np.pi, 7)
    origin = (0, 0)
    r = 1

    points = []
    for angle in angles:
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        points.append((x, y))

    # plotmath.plot_polygon(
    #     *points,
    #     show_vertices=False,
    #     ls="--",
    # )

    for angle1, angle2 in zip(angles[:-1], angles[1:]):
        A = (r * np.cos(angle1), r * np.sin(angle1))
        B = (r * np.cos(angle2), r * np.sin(angle2))

        plotmath.plot_polygon(
            origin,
            A,
            B,
            show_vertices=False,
            ls="--",
        )

    for angle1, angle2 in zip(angles[:-1], angles[1:]):
        A = (r * np.cos(angle1), r * np.sin(angle1))
        B = (r * np.cos(angle2), r * np.sin(angle2))
        h = np.sqrt(3) * r
        C = (
            h * np.cos(0.5 * (angle1 + angle2)),
            h * np.sin(0.5 * (angle1 + angle2)),
        )

        ax.plot(*zip(A, C), lw=1.5, color="black")
        ax.plot(*zip(B, C), lw=1.5, color="black")

        ax.fill(
            [A[0], B[0], C[0]],
            [A[1], B[1], C[1]],
            color=plotmath.COLORS.get("blue"),
            alpha=0.05,
            lw=1.5,
            zorder=1,
        )

        # ax.plot([A[0], C[0]], [A[1], C[1]], ls="-", lw=2, color="black")
        # ax.plot([B[0], C[0]], [B[1], C[1]], ls="-", lw=2, color="black")
        # ax.plot(*zip(A, C), ls="-", lw=2, color="black")
        # ax.plot(*zip(A, B), ls="-", lw=2, color="black")

    ax.axis("off")
    ax.axis("equal")

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
