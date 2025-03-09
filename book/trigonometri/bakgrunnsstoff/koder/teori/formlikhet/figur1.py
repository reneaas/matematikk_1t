import plotmath
import matplotlib.pyplot as plt
import numpy as np


def make_circle_arc(center, radius, start_angle, end_angle, num_points=1024):
    angles = np.linspace(start_angle, end_angle, num_points)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y


def main(dirname, save):
    fontsize = 20
    # List of functions and their labels.
    A = (0, 0)
    B = (3, 0)
    C = (5, 2)

    plotmath.plot_polygon(A, B, C, show_vertices=True)

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
        x=C[0] + dx,
        y=C[1] + dy,
        s="$C$",
        fontsize=fontsize,
        ha="left",
        va="center",
    )

    AB = np.array(B) - np.array(A)
    BC = np.array(C) - np.array(B)
    AC = np.array(C) - np.array(A)
    angle_A = np.arccos(np.dot(AB, AC) / (np.linalg.norm(AB) * np.linalg.norm(AC)))
    angle_B = np.arccos(np.dot(BC, -AB) / (np.linalg.norm(BC) * np.linalg.norm(AB)))
    angle_C = np.arccos(np.dot(AC, -BC) / (np.linalg.norm(AC) * np.linalg.norm(BC)))

    radius = 1
    x, y = make_circle_arc(
        center=A,
        radius=1,
        start_angle=0,
        end_angle=angle_A,
    )

    plt.plot(x, y, color="blue")

    radius = 0.4
    x, y = make_circle_arc(
        center=B,
        radius=radius,
        start_angle=np.pi - angle_B,
        end_angle=np.pi,
    )

    plt.plot(x, y, color="red")

    # Angle C
    start_angle = (np.pi - angle_B) + np.pi
    angle = np.pi - angle_C
    x, y = make_circle_arc(
        center=C,
        radius=1,
        start_angle=start_angle,
        end_angle=start_angle - angle,
    )

    plt.plot(x, y, color="darkorange")

    plt.axis("equal")
    plt.axis("off")

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
