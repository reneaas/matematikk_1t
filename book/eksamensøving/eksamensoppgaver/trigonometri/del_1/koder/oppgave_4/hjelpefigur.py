import plotmath
import numpy as np
import matplotlib.pyplot as plt


def make_angle_arc(center, radius, start_angle, end_angle):
    start_angle = np.deg2rad(start_angle)
    end_angle = np.deg2rad(end_angle)
    theta = np.linspace(start_angle, end_angle, 100)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    return x, y


def main(dirname, save):
    # TODO: write code here
    fig, ax = plt.subplots(figsize=(3, 4))

    A = (0, 0)
    B = (6, 0)
    C = (0, 8)

    plotmath.plot_polygon(
        A,
        B,
        C,
        alpha=0.05,
    )

    angle = np.arccos(8 / 10)
    angle = np.rad2deg(angle)
    start = 90 + 180
    end = start + angle

    x0, y0 = make_angle_arc(C, radius=1.2, start_angle=start, end_angle=end)
    ax.plot(x0, y0, color="black", lw=1.5)

    ax.text(
        x=C[0] + 0.5,
        y=C[1] - 1.5,
        s=r"$u$",
        fontsize=20,
        ha="center",
        va="center",
    )

    angle = np.arccos(6 / 10)
    angle = np.rad2deg(angle)
    start = 180
    end = start - angle
    x0, y0 = make_angle_arc(B, radius=1.2, start_angle=start, end_angle=end)
    ax.plot(x0, y0, color="black", lw=1.5)

    ax.text(
        x=B[0] - 1.5,
        y=B[1] + 0.8,
        s=r"$v$",
        fontsize=20,
        ha="center",
        va="center",
    )

    dx = dy = 0.8
    ax.plot([0, dx], [dy, dy], color="black", lw=1.5)
    ax.plot([dx, dx], [0, dy], color="black", lw=1.5)

    ax.text(
        x=0.5 * (A[0] + C[0]) - 0.2,
        y=0.5 * (A[1] + C[1]),
        s="$b$",
        fontsize=20,
        ha="right",
        va="center",
    )

    ax.text(
        x=0.5 * (B[0] + C[0]) + 0.2,
        y=0.5 * (B[1] + C[1]),
        s="$a$",
        fontsize=20,
        ha="left",
        va="bottom",
    )

    ax.text(
        x=0.5 * (A[0] + B[0]),
        y=0.5 * (A[1] + B[1]) - 0.2,
        s="$c$",
        fontsize=20,
        ha="center",
        va="top",
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
