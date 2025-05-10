import plotmath
import numpy as np
import matplotlib.pyplot as plt


def make_circle(x, y, r):
    theta = np.linspace(0, 2 * np.pi, 1024)
    x_circle = x + r * np.cos(theta)
    y_circle = y + r * np.sin(theta)
    return x_circle, y_circle


def make_circle_arc(center, r, start_angle, end_angle):
    x, y = center
    theta = np.linspace(start_angle, end_angle, 1024)
    x_circle = x + r * np.cos(theta)
    y_circle = y + r * np.sin(theta)
    return x_circle, y_circle


def main(dirname, save):
    # TODO: write code here

    r = 1
    x, y = make_circle(x=0, y=0, r=r)

    plt.plot(x, y, color="black", lw=1.5)

    S = (0, 0)
    B = (r, 0)
    A = (-r, 0)
    angle = 45
    angle_rad = np.deg2rad(angle)
    C = (r * np.cos(angle_rad), r * np.sin(angle_rad))

    plotmath.plot_polygon(
        S,
        B,
        C,
        alpha=0.2,
    )

    plotmath.plot_polygon(
        A,
        B,
        C,
    )

    ax = plt.gca()

    ax.text(
        x=0,
        y=0 - 0.05,
        s=r"$S$",
        fontsize=20,
        ha="center",
        va="top",
    )

    ax.text(
        x=r + 0.05,
        y=0,
        s=r"$B$",
        fontsize=20,
        ha="left",
        va="center",
    )

    ax.text(
        x=-r - 0.05,
        y=0,
        s=r"$A$",
        fontsize=20,
        ha="right",
        va="center",
    )

    ax.text(
        x=r * np.cos(angle_rad) + 0.05,
        y=r * np.sin(angle_rad) + 0.05,
        s=r"$C$",
        fontsize=20,
        ha="center",
        va="center",
    )

    x, y = make_circle_arc(
        center=S,
        r=0.2 * r,
        start_angle=0,
        end_angle=angle_rad,
    )

    ax.plot(x, y, color="black", lw=1)

    ax.text(
        x=0.2,
        y=0.05,
        s=r"$45^\circ$",
        fontsize=20,
        ha="left",
        va="bottom",
    )

    plt.axis("off")
    plt.axis("equal")

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
