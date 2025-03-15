import plotmath
import numpy as np
import matplotlib.pyplot as plt


def draw_circle_arc(center, radius, start_angle, end_angle, num_points=100):
    ax = plt.gca()
    angles = np.linspace(start_angle, end_angle, num_points)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    ax.plot(x, y, color="black")


def draw_right_angle(A, dx=0.1, dy=0.1):
    ax = plt.gca()
    x, y = A
    ax.plot([x, x + dx], [dy, dy], color="black")
    ax.plot([dx, dx], [y, y + dy], color="black")

    return ax


def main(dirname, save):
    # TODO: write code here

    angle_B = 180 - 120
    A = (0, 0)
    B = (10, 0)
    C = (
        10 + 15 * np.cos(angle_B * np.pi / 180),
        15 * np.sin(angle_B * np.pi / 180),
    )
    D = (0, 10)
    points = [A, B, C, D]
    ax = plotmath.plot_polygon(
        *points,
        show_vertices=True,
    )

    # Draw right angle
    draw_right_angle(A, dx=1.5, dy=1.5)

    # Draw angles
    draw_circle_arc(B, radius=1.5, start_angle=np.pi, end_angle=angle_B * np.pi / 180)

    plt.text(
        x=A[0] - 0.5,
        y=A[1] - 0.5,
        s=r"$A$",
        fontsize=20,
        ha="right",
        va="top",
    )

    plt.text(
        x=B[0] + 0.5,
        y=B[1] - 0.5,
        s=r"$B$",
        fontsize=20,
        ha="left",
        va="top",
    )

    plt.text(
        x=C[0] + 0.5,
        y=C[1] + 0.5,
        s=r"$C$",
        fontsize=20,
        ha="left",
        va="bottom",
    )

    plt.text(
        x=D[0] - 0.5,
        y=D[1] + 0.5,
        s=r"$D$",
        fontsize=20,
        ha="right",
        va="bottom",
    )

    AB = np.linalg.norm(np.array(B) - np.array(A))
    BC = np.linalg.norm(np.array(C) - np.array(B))
    CD = np.linalg.norm(np.array(D) - np.array(C))
    DA = np.linalg.norm(np.array(A) - np.array(D))

    plt.text(
        x=0.5 * (A[0] + B[0]),
        y=0.5 * (A[1] + B[1]) - 0.2,
        s=f"${AB:.0f}$ m",
        fontsize=20,
        ha="center",
        va="top",
    )

    plt.text(
        x=0.5 * (B[0] + C[0]) + 0.4,
        y=0.5 * (B[1] + C[1]),
        s=f"${BC:.0f}$ m",
        fontsize=20,
        ha="left",
        va="center",
    )

    # plt.text(
    #     x=0.5 * (C[0] + D[0]),
    #     y=0.5 * (C[1] + D[1]) + 0.2,
    #     s=f"${CD:.0f}$ m",
    #     fontsize=20,
    #     ha="center",
    #     va="bottom",
    # )

    plt.text(
        x=0.5 * (D[0] + A[0]) - 0.4,
        y=0.5 * (D[1] + A[1]),
        s=f"${DA:.0f}$ m",
        fontsize=20,
        ha="right",
        va="center",
    )

    plt.text(
        x=B[0] - 0.1,
        y=B[1] + 1.5,
        s=r"$120^\circ$",
        fontsize=20,
        ha="right",
        va="bottom",
    )

    plt.axis("off")
    plt.axis("equal")

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
