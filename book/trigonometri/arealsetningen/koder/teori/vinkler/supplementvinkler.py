from casify import *
import matplotlib.pyplot as plt


def make_circle_arc(center, radius, start_angle, end_angle, n=100):
    import numpy as np

    angles = np.linspace(start_angle, end_angle, n)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y


def main(dirname, save):
    # TODO: write code here
    import plotmath
    import matplotlib.pyplot as plt
    import numpy as np

    ax = draw_triangle(
        sas=(2, 120, 2),
        show=False,
        radius=0.5,
        fontsize=22,
        label_angles=("v", False, False),
        label_sides=(False, False, False),
        vertex_labels=(False, False, False),
        alpha=0.05,
    )

    draw_triangle(
        (0, 0),
        (-1, 0),
        (-1, 3**0.5),
        show=False,
        radius=0.25,
        fontsize=22,
        label_angles=(" ", False, False),
        label_sides=(False, False, False),
        vertex_labels=(False, False, False),
        alpha=0.05,
    )

    plt.text(
        x=-0.35,
        y=0.2,
        s=r"$u$",
        fontsize=20,
        ha="center",
        va="center",
    )

    # angle = 120 * np.pi / 180
    # h = 2 * np.sin(angle)
    # x = 2 * np.cos(angle)
    # ax.vlines(x=x, ymin=0, ymax=h, linestyle="--", color="black")
    # ax.hlines(y=0, xmin=0, xmax=x, linestyle="--", color="black")

    dx = dy = 0.1
    # ax.text(
    #     x=x - dx,
    #     y=0.5 * h,
    #     s=r"$h$",
    #     fontsize=20,
    #     ha="right",
    #     va="center",
    # )

    # ax.text(
    #     x=1,
    #     y=-dy,
    #     s=r"$g$",
    #     fontsize=20,
    #     ha="center",
    #     va="top",
    # )

    # dx = dy = 0.2
    # ax.plot([x, x + dx], [dy, dy], ls="--", color="black")
    # ax.plot([x + dx, x + dx], [dy, 0], ls="--", color="black")

    # x, y = make_circle_arc(
    #     center=(0, 0),
    #     radius=0.5**2,
    #     start_angle=np.pi,
    #     end_angle=120 * np.pi / 180,
    # )

    # ax.plot(x, y, color="black", lw=1)

    plt.title(r"Supplementvinkler", fontsize=20, loc="left")
    plt.tight_layout()

    # NOTE: Automatically saves with correct file format and filename.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname, fname=fname
        )  # Lagrer figuren i `dirname`-directory
    else:
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
