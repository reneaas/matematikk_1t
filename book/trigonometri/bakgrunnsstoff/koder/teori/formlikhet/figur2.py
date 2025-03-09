import plotmath
import matplotlib.pyplot as plt
import numpy as np


def rotation_matrix(theta):
    return [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]


def scale_matrix(s):
    return [[s, 0], [0, s]]


def reflection_matrix():
    return [[1, 0], [0, -1]]


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

    A0 = np.array(A)
    B0 = np.array(B)
    C0 = np.array(C)

    # Transformations
    S = scale_matrix(0.5)
    R = rotation_matrix(np.pi / 2)
    F = reflection_matrix()

    # Net transformation
    T = np.einsum("il,lk,kj->ij", R, F, S)
    # T = np.zeros((2, 2))
    # T[0, 0] = 1
    # T[1, 1] = 1
    # print(T)

    # New points after transformation
    A = np.einsum("ij,j->i", T, A0)
    B = np.einsum("ij,j->i", T, B0)
    C = np.einsum("ij,j->i", T, C0)

    A = tuple(A)
    B = tuple(B)
    C = tuple(C)

    plotmath.plot_polygon(A, B, C, show_vertices=True, alpha=0.05)

    dx = dy = 0.1
    plt.text(
        x=A[0] - dx,
        y=A[1] - dx,
        s="$D$",
        fontsize=fontsize,
        ha="center",
        va="top",
    )

    plt.text(
        x=B[0] - dx,
        y=B[1],
        s="$E$",
        fontsize=fontsize,
        ha="right",
        va="center",
    )

    plt.text(
        x=C[0] + dx,
        y=C[1] + dy,
        s="$F$",
        fontsize=fontsize,
        ha="left",
        va="bottom",
    )

    # Draw angles.

    AB = np.array(B) - np.array(A)
    BC = np.array(C) - np.array(B)
    AC = np.array(C) - np.array(A)
    angle_A = np.arccos(np.dot(AB, AC) / (np.linalg.norm(AB) * np.linalg.norm(AC)))
    angle_B = np.arccos(np.dot(BC, -AB) / (np.linalg.norm(BC) * np.linalg.norm(AB)))
    angle_C = np.arccos(np.dot(AC, -BC) / (np.linalg.norm(AC) * np.linalg.norm(BC)))

    radius = 1
    x, y = make_circle_arc(
        center=A0,
        radius=1,
        start_angle=0,
        end_angle=angle_A,
    )

    # Angle A
    r = np.stack((x, y), axis=1)
    r = np.einsum("ij,...j->...i", T, r)

    x = r[:, 0]
    y = r[:, 1]

    plt.plot(x, y, color="blue")

    # Angle B
    radius = 0.4
    x, y = make_circle_arc(
        center=B0,
        radius=radius,
        start_angle=np.pi - angle_B,
        end_angle=np.pi,
    )

    r = np.stack((x, y), axis=1)
    r = np.einsum("ij,...j->...i", T, r)

    x = r[:, 0]
    y = r[:, 1]

    plt.plot(x, y, color="red")

    # Angle C
    start_angle = (np.pi - angle_B) + np.pi
    angle = np.pi - angle_C
    x, y = make_circle_arc(
        center=C0,
        radius=1,
        start_angle=start_angle,
        end_angle=start_angle - angle,
    )

    r = np.stack((x, y), axis=1)
    r = np.einsum("ij,...j->...i", T, r)

    x = r[:, 0]
    y = r[:, 1]

    plt.plot(x, y, color="darkorange")

    print(np.degrees(angle_A), np.degrees(angle_B), np.degrees(angle_C))

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
