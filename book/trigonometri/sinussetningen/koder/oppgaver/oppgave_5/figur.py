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

    a = 1
    b = a / np.sqrt(2)
    d = np.sqrt(a**2 + b**2 - 2 * a * b * np.cos(np.radians(105)))
    A = (0, 0)
    D = (a / np.sqrt(2) * np.cos(np.pi / 4), a / np.sqrt(2) * np.sin(np.pi / 4))
    B = (d, 0)
    A = np.array(A)
    B = np.array(B)
    D = np.array(D)

    C = (d, 0.5 * a)
    C = np.array(C)

    angle = np.radians(20)
    A_rot = np.dot(rotation_matrix(angle), A)
    B_rot = np.dot(rotation_matrix(angle), B)
    C_rot = np.dot(rotation_matrix(angle), C)
    D_rot = np.dot(rotation_matrix(angle), D)

    # Draw angle ADB
    x, y = make_circle_arc(center=D, radius=0.1, start_angle=-30, end_angle=-30 - 105)

    # rotate angle arc
    x = x - D[0]
    y = y - D[1]

    x, y = np.dot(rotation_matrix(np.radians(20)), np.array([x, y]))
    x = x + D_rot[0]
    y = y + D_rot[1]

    plt.plot(x, y, color="black", lw=1)
    dx = dy = 0.15
    plt.text(
        x=D_rot[0] + 0.1,
        y=D_rot[1] - dy,
        s="$105^\\circ$",
        fontsize=16,
        ha="center",
        va="center",
    )

    # Draw angle BDC
    x, y = make_circle_arc(center=D, radius=0.15, start_angle=0, end_angle=-30)
    x = x - D[0]
    y = y - D[1]

    x, y = np.dot(rotation_matrix(np.radians(20)), np.array([x, y]))
    x = x + D_rot[0]
    y = y + D_rot[1]

    plt.plot(x, y, color="black", lw=1)
    plt.text(
        x=D_rot[0] + 0.2,
        y=D_rot[1] + 0.02,
        s="$30^\\circ$",
        fontsize=16,
        ha="center",
        va="center",
    )

    # Make right angle in C
    dx = dy = 0.1
    x = np.linspace(C[0], C[0] - dx, 100)
    y = np.ones_like(x) * C[1] - dy

    # rotate right angle
    x = x - C[0]
    y = y - C[1]

    x, y = np.dot(rotation_matrix(np.radians(20)), np.array([x, y]))
    x = x + C_rot[0]
    y = y + C_rot[1]

    plt.plot(x, y, color="black", lw=1)

    # Complete right angle in C
    x = np.ones_like(y) * C[0] - dx
    y = np.linspace(C[1], C[1] - dy, 100)

    # rotate right angle
    x = x - C[0]
    y = y - C[1]

    x, y = np.dot(rotation_matrix(np.radians(20)), np.array([x, y]))
    x = x + C_rot[0]
    y = y + C_rot[1]

    plt.plot(x, y, color="black", lw=1)

    # Draw angle ABD
    x, y = make_circle_arc(center=B, radius=0.15, start_angle=180, end_angle=180 - 30)

    # rotate angle arc
    x = x - B[0]
    y = y - B[1]

    x, y = np.dot(rotation_matrix(np.radians(20)), np.array([x, y]))
    x = x + B_rot[0]
    y = y + B_rot[1]

    plt.plot(x, y, color="black", lw=1)
    dx = dy = 0.15
    plt.text(
        x=B_rot[0] - 0.2,
        y=B_rot[1] - 0.02,
        s="$30^\\circ$",
        fontsize=16,
        ha="center",
        va="center",
    )

    x_midpoint = 0.5 * (B_rot + D_rot)
    plt.text(
        x=x_midpoint[0],
        y=x_midpoint[1] + 0.05,
        s="$a$",
        fontsize=16,
        ha="center",
        va="center",
    )

    # label vertices
    dx = dy = 0.05
    plt.text(
        x=A_rot[0] - dx,
        y=A_rot[1] - dy,
        s="$A$",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.text(
        x=B_rot[0] + dx,
        y=B_rot[1] - dy,
        s="$B$",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.text(
        x=C_rot[0] + dx,
        y=C_rot[1] + dy,
        s="$C$",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.text(
        x=D_rot[0] - dx,
        y=D_rot[1] + dy,
        s="$D$",
        fontsize=16,
        ha="center",
        va="center",
    )

    A = tuple(A_rot)
    B = tuple(B_rot)
    C = tuple(C_rot)
    D = tuple(D_rot)

    points = (A, B, D)
    plotmath.plot_polygon(
        *points,
        ax=None,
        show_vertices=False,
        alpha=0.03,
    )

    points = (B, C, D)
    plotmath.plot_polygon(
        *points,
        ax=None,
        show_vertices=False,
        alpha=0.03,
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
