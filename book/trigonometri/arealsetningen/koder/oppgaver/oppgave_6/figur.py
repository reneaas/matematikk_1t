import plotmath
import numpy as np
import matplotlib.pyplot as plt


def make_circle(center, radius, num_points=1024):
    angles = np.linspace(0, 2 * np.pi, num_points)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y


def draw_right_angle(A, dx=0.1, dy=0.1):
    ax = plt.gca()
    x, y = A
    ax.plot([x, x + dx], [y + dy, y + dy], color="black")
    ax.plot([dx, dx], [y, y + dy], color="black")

    return ax


def draw_circle_arc(center, radius, start_angle, end_angle, num_points=100):
    ax = plt.gca()
    start_angle = np.radians(start_angle)
    end_angle = np.radians(end_angle)
    angles = np.linspace(start_angle, end_angle, num_points)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    ax.plot(x, y, color="black")


def main(dirname, save):
    # TODO: write code here

    angle = -30
    angle = np.radians(angle)
    a = 1
    A = (0, 0)
    D = (0, a)
    C = (3**0.5 * a, a)
    B = (3**0.5 * a + 3**0.5 * a * np.cos(angle), a + 3**0.5 * a * np.sin(angle))

    points = [A, B, C, D]
    plotmath.plot_polygon(
        *points,
        show_vertices=True,
    )

    dx = dy = 0.05
    plt.text(
        x=A[0] - dx,
        y=A[1] - dy,
        s="$A$",
        fontsize=20,
        va="top",
        ha="right",
    )

    plt.text(
        x=B[0] + dx,
        y=B[1] - dy,
        s="$B$",
        fontsize=20,
        va="top",
        ha="left",
    )

    plt.text(
        x=C[0] + dx,
        y=C[1] + dy,
        s="$C$",
        fontsize=20,
        va="bottom",
        ha="left",
    )

    plt.text(
        x=D[0] - dx,
        y=D[1] + dy,
        s="$D$",
        fontsize=20,
        va="bottom",
        ha="right",
    )

    draw_right_angle(D, dx=0.15, dy=-0.15)

    x, y = zip(A, C)
    plt.plot(x, y, ls="--", color="black")

    draw_circle_arc(
        center=C,
        radius=0.2,
        start_angle=180,
        end_angle=180 + 150,
    )

    plt.text(
        x=C[0],
        y=C[1] - 5 * dy,
        s=r"$150^\circ$",
        fontsize=20,
        va="top",
        ha="center",
    )

    plt.text(
        x=0.5 * (A[0] + C[0]),
        y=0.5 * (A[1] + C[1]) + dy,
        s="$2a$",
        fontsize=20,
        va="bottom",
        ha="center",
    )

    plt.text(
        x=-dx,
        y=0.5 * (A[1] + D[1]),
        s="$a$",
        fontsize=20,
        va="center",
        ha="right",
    )

    plt.text(
        x=0.5 * (C[0] + B[0]),
        y=0.5 * (C[1] + B[1]) + dy,
        s="$\\sqrt{3} a$",
        fontsize=20,
        va="bottom",
        ha="left",
    )

    plt.axis("equal")
    plt.axis("off")

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
