import plotmath
import numpy as np
import matplotlib.pyplot as plt


def make_angle_arc(center, radius, start_angle, end_angle, num_points=1024):
    """
    Create points for an arc between two angles.

    Parameters:
        center (tuple): The center of the arc (x, y).
        radius (float): The radius of the arc.
        start_angle (float): The starting angle in radians.
        end_angle (float): The ending angle in radians.
        num_points (int): Number of points to generate for the arc.

    Returns:
        tuple: x and y coordinates of the arc points.
    """
    start_angle = np.deg2rad(start_angle)
    end_angle = np.deg2rad(end_angle)
    angles = np.linspace(start_angle, end_angle, num_points)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)

    return x, y


def main(dirname, save):
    # TODO: write code here

    L = 20

    fig, ax = plt.subplots(figsize=(10, 4))

    A = (0, 0)
    B = (L, 0)
    ax.plot(*zip(A, B), color="black", lw=2)

    angle = 50
    angle = np.deg2rad(angle)
    C = (B[0] + L * np.cos(angle), B[1] + L * np.sin(angle))
    ax.plot(*zip(B, C), color="black", lw=2)

    angle = 180 - 50
    angle = np.deg2rad(angle)
    D = (L * np.cos(angle), L * np.sin(angle))
    ax.plot(*zip(A, D), color="black", lw=2)

    ax.plot(*zip(C, D), color="black", lw=1.5, ls="--")

    angle = 50
    angle = np.deg2rad(angle)
    g = L * np.cos(angle)
    h = L * np.sin(angle)

    ax.plot([0, -g], [0, 0], color="black", lw=1.5, ls="--")
    ax.plot([L, L + g], [0, 0], color="black", lw=1.5, ls="--")

    angle = 50
    x, y = make_angle_arc(
        center=B,
        radius=0.25 * L,
        start_angle=0,
        end_angle=50,
    )

    ax.plot(x, y, color="black")

    x, y = make_angle_arc(
        center=A,
        radius=0.25 * L,
        start_angle=180 - 50,
        end_angle=180,
    )

    ax.plot(x, y, color="black")

    ax.text(
        x=0.5 * L,
        y=-2,
        s=r"$10$",
        fontsize=20,
        ha="center",
        va="center",
    )

    ax.text(
        x=-0.5 * g,
        y=0.5 * h,
        s=r"$10$",
        fontsize=20,
        ha="left",
        va="bottom",
    )

    ax.text(
        x=1.5 * L - 4,
        y=0.5 * h,
        s=r"$10$",
        fontsize=20,
        ha="right",
        va="bottom",
    )

    ax.text(
        x=L + 0.4 * g,
        y=0.15 * h,
        s=r"$x$",
        fontsize=20,
    )

    ax.text(
        x=-0.5 * g,
        y=0.15 * h,
        s=r"$x$",
        fontsize=20,
    )

    ax.plot([-g, -g], [0, h], color="black", lw=1.5, ls="--")
    ax.plot([L + g, L + g], [0, h], color="black", lw=1.5, ls="--")

    dx = dy = 2
    ax.plot([-g + dx, -g + dx], [0, dy], color="black", lw=1.5, ls="-")
    ax.plot([-g, -g + dx], [dy, dy], color="black", lw=1.5, ls="-")

    ax.text(
        x=-g - 1,
        y=0.5 * h,
        s=r"$h$",
        fontsize=20,
        ha="right",
        va="center",
    )

    ax.text(
        x=-0.5 * g,
        y=-1,
        s=r"$g$",
        fontsize=20,
        ha="center",
        va="top",
    )

    ax.plot([L + g - dx, L + g - dx], [0, dy], color="black", lw=1.5, ls="-")
    ax.plot([L + g, L + g - dx], [dy, dy], color="black", lw=1.5, ls="-")

    ax.text(
        x=L + g + 1,
        y=0.5 * h,
        s=r"$h$",
        fontsize=20,
        ha="left",
        va="center",
    )

    ax.text(
        x=L + 0.5 * g,
        y=-1,
        s=r"$g$",
        fontsize=20,
        ha="center",
        va="top",
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
