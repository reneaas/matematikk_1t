import plotmath
import matplotlib.pyplot as plt
import numpy as np


def make_circle_arc(center, radius, start_angle, end_angle, num_points=1024):
    angles = np.linspace(start_angle, end_angle, num_points)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y


def main(dirname, save):
    fontsize = 22
    # List of functions and their labels.
    A = (-1.5, 0)
    B = (1.5, 0)
    C = (0, 4)

    plotmath.plot_polygon(A, B, C, show_vertices=True, alpha=0.05)

    dx = dy = 0.1
    plt.text(
        x=A[0] - dx,
        y=A[1] - dy,
        s="$A$",
        fontsize=fontsize,
        ha="right",
        va="center",
    )

    plt.text(
        x=B[0] + dx,
        y=B[1] - dy,
        s="$B$",
        fontsize=fontsize,
        ha="left",
        va="center",
    )

    plt.text(
        x=C[0],
        y=C[1] + dy,
        s="$C$",
        fontsize=fontsize,
        ha="center",
        va="bottom",
    )

    AB = np.array(B) - np.array(A)
    AC = np.array(C) - np.array(A)
    BC = np.array(C) - np.array(B)

    angle_A = np.arccos(np.dot(AB, AC) / (np.linalg.norm(AB) * np.linalg.norm(AC)))
    angle_B = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))
    angle_C = np.arccos(np.dot(AB, -BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))

    x, y = make_circle_arc(
        center=A,
        radius=0.6,
        start_angle=0,
        end_angle=angle_A,
    )

    plt.plot(x, y, color="black")

    x, y = make_circle_arc(
        center=B,
        radius=0.6,
        start_angle=angle_B,
        end_angle=np.pi,
    )

    plt.plot(x, y, color="black")

    plt.text(
        x=A[0] + 0.5 * (np.cos(angle_A) + 1),
        y=A[1] + 0.5 * np.sin(angle_A),
        s="$v$",
        fontsize=26,
        ha="center",
        va="center",
    )

    plt.text(
        x=B[0] - 0.5 * (np.cos(angle_A) + 1),
        y=B[1] + 0.5 * np.sin(angle_A),
        s="$v$",
        fontsize=26,
        ha="center",
        va="center",
    )

    # plt.text(
    #     x=0.5 * (A[0] + B[0]),
    #     y=0.5 * (A[1] + B[1]) - dy,
    #     s="$\\mathrm{katet}_1$",
    #     fontsize=fontsize,
    #     ha="center",
    #     va="top",
    # )

    # plt.text(
    #     x=0.5 * (A[0] + C[0]) - dx,
    #     y=0.5 * (A[1] + C[1]),
    #     s="$\\mathrm{katet}_2$",
    #     fontsize=fontsize,
    #     ha="right",
    #     va="center",
    # )

    # plt.text(
    #     x=0.5 * (B[0] + C[0]),
    #     y=0.5 * (B[1] + C[1]) + dy,
    #     s="Hypotenus",
    #     fontsize=fontsize,
    #     ha="left",
    #     va="bottom",
    # )

    # dx = dy = 0.2
    # plt.plot([0, dx], [dy, dy], "k")
    # plt.plot([dx, dx], [0, dy], "k")

    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.title("Likebeint", loc="right", fontsize=fontsize)

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
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
