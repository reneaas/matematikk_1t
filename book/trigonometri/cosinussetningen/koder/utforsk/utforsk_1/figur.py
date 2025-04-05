import plotmath
import numpy as np
import matplotlib.pyplot as plt
from casify import *


def make_circle_arc(center, radius, start_angle, end_angle, num_points=1024):
    # start_angle = np.radians(start_angle)
    # end_angle = np.radians(end_angle)
    angles = np.linspace(start_angle, end_angle, num_points)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y


def main(dirname, save):
    # TODO: write code here

    A = (0, 0)
    B = (5, 0)
    C = (-2, 4)
    D = (C[0], 0)

    BC = np.sqrt((B[0] - C[0]) ** 2 + (B[1] - C[1]) ** 2)
    AB = np.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)
    AC = np.sqrt((A[0] - C[0]) ** 2 + (A[1] - C[1]) ** 2)
    angle = np.arccos((AB**2 + AC**2 - BC**2) / (2 * AB * AC))

    ax = draw_triangle(
        A,
        B,
        C,
        show=False,
        radius=1,
        fontsize=20,
        label_angles=(" ", False, False),
        label_sides=(False, False, False),
        vertex_labels=(False, False, False),
        numerical_len=False,
        show_vertices=False,
        alpha=0.05,
    )

    x, y = make_circle_arc(
        center=A,
        radius=0.5,
        start_angle=np.pi,
        end_angle=angle,
    )

    ax.plot(x, y, color="black", lw=1, ls="-")

    ax.text(
        x=A[0] + 0.4,
        y=A[1] + 0.4,
        s="$v$",
        fontsize=20,
        ha="left",
        va="bottom",
    )

    ax.text(
        x=A[0] - 0.5,
        y=A[1] + 0.3,
        s="$u$",
        fontsize=20,
        ha="right",
        va="bottom",
    )

    dx = dy = 0.1
    ax.text(
        x=A[0],
        y=A[1] - dy,
        s="$A$",
        fontsize=20,
        ha="center",
        va="top",
    )

    ax.text(
        x=B[0] + dx,
        y=B[1],
        s="$B$",
        fontsize=20,
        ha="left",
        va="center",
    )

    ax.text(
        x=C[0] - dx,
        y=C[1] + dy,
        s="$C$",
        fontsize=20,
        ha="right",
        va="bottom",
    )

    ax.text(
        x=D[0] - dx,
        y=D[1] - dy,
        s="$D$",
        fontsize=20,
        ha="right",
        va="top",
    )

    dx = dy = 0.2

    ax.text(
        x=0.5 * (A[0] + B[0]),
        y=0.5 * (A[1] + B[1]) - dy,
        s="$c$",
        fontsize=20,
        ha="center",
        va="top",
    )

    ax.text(
        x=0.5 * (B[0] + C[0]) + dx,
        y=0.5 * (B[1] + C[1]) + dy,
        s="$a$",
        fontsize=20,
        ha="left",
        va="center",
    )

    ax.text(
        x=0.5 * (A[0] + C[0]) + dx,
        y=0.5 * (A[1] + C[1]) - dy,
        s="$b$",
        fontsize=20,
        ha="left",
        va="bottom",
    )

    ax.vlines(
        x=C[0],
        ymin=0,
        ymax=C[1],
        color="black",
        ls="--",
        alpha=0.7,
    )

    ax.hlines(
        y=0,
        xmin=C[0],
        xmax=0,
        color="black",
        ls="--",
        alpha=0.7,
    )

    dx = dy = 0.2
    ax.text(
        x=C[0] - dx,
        y=0.5 * C[1],
        s="$y$",
        fontsize=20,
        ha="right",
        va="center",
    )

    ax.text(
        x=0.5 * C[0],
        y=-dy,
        s="$x$",
        fontsize=20,
        ha="center",
        va="top",
    )

    dx = dy = 0.3
    ax.plot(
        [C[0] + dx, C[0] + dx],
        [0, dy],
        color="black",
        ls="-",
        lw=1,
    )

    ax.plot(
        [C[0], C[0] + dx],
        [dy, dy],
        color="black",
        ls="-",
        lw=1,
    )

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
