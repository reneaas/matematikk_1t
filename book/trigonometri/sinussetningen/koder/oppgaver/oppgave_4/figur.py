import plotmath
import numpy as np
import matplotlib.pyplot as plt


def rotation_matrix(theta):
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])


def make_circle_arc(center, radius, start_angle, end_angle, num_points=1024):
    start_angle = np.radians(start_angle)
    end_angle = np.radians(end_angle)
    angles = np.linspace(start_angle, end_angle, num_points)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y


def main(dirname, save):
    # TODO: write code here

    A = (0, 0)
    AD = 3 * np.sqrt(10)
    D = (AD * np.cos(np.pi / 4), AD * np.sin(np.pi / 4))
    AB = 2 * np.sqrt(5)
    B = (AB, 0)
    BC = np.sqrt(29)

    xi = 48.37
    beta = 108.43
    angle = np.radians(xi)
    C = (B[0] + BC * np.cos(angle), B[1] + BC * np.sin(angle))

    chi = 180 - beta
    angle = xi + chi
    # angle = 111.8 + 85.23
    CD = 3

    D = (C[0] + CD * np.cos(np.radians(angle)), C[1] + CD * np.sin(np.radians(angle)))

    points = (A, B, C, D)
    plotmath.plot_polygon(
        *points,
        ax=None,
        show_vertices=True,
        alpha=0.03,
    )

    plt.plot([B[0], D[0]], [B[1], D[1]], color="black", lw=1, ls="--")
    midpoint = ((B[0] + D[0]) / 2, (B[1] + D[1]) / 2)
    plt.text(
        x=midpoint[0] - 0.5,
        y=midpoint[1],
        s="$5 \\sqrt{2}$",
        fontsize=16,
        ha="center",
        va="center",
    )

    AB_midtpoint = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
    plt.text(
        x=AB_midtpoint[0],
        y=AB_midtpoint[1] - 0.5,
        s="$2 \\sqrt{5}$",
        fontsize=16,
        ha="center",
        va="center",
    )

    angle = angle + 180
    x, y = make_circle_arc(center=D, radius=1, start_angle=angle, end_angle=angle - 45)

    plt.text(
        x=D[0] + 0.2,
        y=D[1] - 1.3,
        s="$45^\\circ$",
        fontsize=16,
        ha="center",
        va="center",
    )

    CD_midpoint = ((C[0] + D[0]) / 2, (C[1] + D[1]) / 2)
    plt.text(
        x=CD_midpoint[0] + 0.3,
        y=CD_midpoint[1] + 0.2,
        s="$3$",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.plot(x, y, color="black", lw=1)

    x, y = make_circle_arc(center=A, radius=1, start_angle=0, end_angle=45)
    plt.plot(x, y, color="black", lw=1)
    plt.text(
        x=A[0] + 1.4,
        y=A[1] + 0.5,
        s="$45^\\circ$",
        fontsize=16,
        ha="center",
        va="center",
    )

    # label vertices

    dx = dy = 0.3
    plt.text(
        x=A[0] - dx,
        y=A[1] - dy,
        s="$A$",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.text(
        x=B[0] + dx,
        y=B[1] - dy,
        s="$B$",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.text(
        x=C[0] + dx,
        y=C[1] - dy,
        s="$C$",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.text(
        x=D[0] + dx,
        y=D[1] + dy,
        s="$D$",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.axis("off")
    plt.axis("equal")

    # NOTE: Automatically saves with correct file format and filename.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname,
            fname=fname,
            transparent=True,
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
