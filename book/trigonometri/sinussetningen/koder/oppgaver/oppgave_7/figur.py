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
    AB = 8
    B = (AB, 0)
    BC = 6
    psi = np.radians(107.03)
    C = (B[0] + BC * np.cos(psi), B[1] + BC * np.sin(psi))
    CD = 4
    xi = np.radians(107.03 + 86.42)
    # D = (C[0] + CD * np.cos(xi), C[1] + CD * np.sin(xi))
    AD = 5
    D = (AD * np.cos(np.pi / 3), AD * np.sin(np.pi / 3))

    plt.plot([B[0], D[0]], [B[1], D[1]], color="black", lw=1, ls="--")

    # label AB
    # midpoint = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
    # plt.text(
    #     x=midpoint[0],
    #     y=midpoint[1] - 0.5,
    #     s="$8$",
    #     fontsize=16,
    #     ha="center",
    #     va="center",
    # )

    # label BD
    # midpoint = ((B[0] + D[0]) / 2, (B[1] + D[1]) / 2)
    # plt.text(
    #     x=midpoint[0],
    #     y=midpoint[1] + 0.5,
    #     s="$7$",
    #     fontsize=16,
    #     ha="center",
    #     va="center",
    # )

    # label AD
    midpoint = ((A[0] + D[0]) / 2, (A[1] + D[1]) / 2)
    plt.text(
        x=midpoint[0] - 0.5,
        y=midpoint[1],
        s="$5$",
        fontsize=16,
        ha="center",
        va="center",
    )

    # label CD
    # midpoint = ((C[0] + D[0]) / 2, (C[1] + D[1]) / 2)
    # plt.text(
    #     x=midpoint[0],
    #     y=midpoint[1] + 0.5,
    #     s="$4$",
    #     fontsize=16,
    #     ha="center",
    #     va="center",
    # )

    # label BC
    midpoint = ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)
    plt.text(
        x=midpoint[0],
        y=midpoint[1] + 0.5,
        s="$6$",
        fontsize=16,
        ha="left",
        va="center",
    )

    # Plot angle arc for A
    x, y = make_circle_arc(
        center=A,
        radius=0.8,
        start_angle=0,
        end_angle=60,
    )

    plt.plot(x, y, color="black", lw=1, ls="-")

    plt.text(
        x=A[0] + 1.1,
        y=A[1] + 0.5,
        s="$60^\\circ$",
        fontsize=16,
        ha="center",
        va="center",
    )

    x, y = make_circle_arc(
        center=B,
        radius=1,
        start_angle=180,
        end_angle=180 - 38.2,
    )

    plt.plot(x, y, color="black", lw=1, ls="-")

    plt.text(
        x=B[0] - 1.5,
        y=B[1] + 0.5,
        s="$38.2^\\circ$",
        fontsize=16,
        ha="center",
        va="center",
    )

    psi = 107.03
    phi = 34.77
    x, y = make_circle_arc(
        center=B,
        radius=1.5,
        start_angle=psi,
        end_angle=psi + phi,
    )
    plt.plot(x, y, color="black", lw=1, ls="-")

    plt.text(
        x=B[0] - 1.1,
        y=B[1] + 1.6,
        s=f"${phi}^\\circ$",
        fontsize=16,
        ha="center",
        va="center",
    )

    xi = 86.42
    rho = 180 - xi
    x, y = make_circle_arc(
        center=C,
        radius=0.7,
        start_angle=psi + rho,
        end_angle=psi + rho + xi,
    )

    plt.text(
        x=C[0] - 0.5,
        y=C[1] - 1,
        s=f"${xi}^\\circ$",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.plot(x, y, color="black", lw=1, ls="-")

    points = (A, B, C, D)
    plotmath.plot_polygon(
        *points,
        ax=None,
        show_vertices=True,
        alpha=0.05,
    )

    # Label vertices

    plt.text(
        x=A[0] - 0.2,
        y=A[1] - 0.2,
        s="$A$",
        fontsize=16,
        ha="right",
        va="top",
    )

    plt.text(
        x=B[0] + 0.2,
        y=B[1] - 0.2,
        s="$B$",
        fontsize=16,
        ha="left",
        va="top",
    )

    plt.text(
        x=C[0] + 0.2,
        y=C[1] + 0.2,
        s="$C$",
        fontsize=16,
        ha="center",
        va="bottom",
    )

    plt.text(
        x=D[0] - 0.2,
        y=D[1] + 0.2,
        s="$D$",
        fontsize=16,
        ha="right",
        va="bottom",
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
