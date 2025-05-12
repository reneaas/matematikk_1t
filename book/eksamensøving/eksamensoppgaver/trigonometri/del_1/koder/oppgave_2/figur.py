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
    fig, ax = plt.subplots(figsize=(2, 2))

    A = (0, 0)
    B = (2, 0)
    angle = 60
    angle = np.deg2rad(angle)
    C = (2 * np.cos(angle), 2 * np.sin(angle))

    plotmath.plot_polygon(
        A,
        B,
        C,
        alpha=0.05,
    )

    ax.text(
        x=0.5 * (A[0] + C[0]) - 0.08,
        y=0.5 * (A[1] + C[1]),
        s="$2$",
        fontsize=20,
        ha="right",
        va="center",
    )

    ax.text(
        x=0.5 * (B[0] + C[0]) + 0.08,
        y=0.5 * (B[1] + C[1]),
        s="$2$",
        fontsize=20,
        ha="left",
        va="center",
    )

    ax.text(
        x=0.5 * (A[0] + B[0]),
        y=0.5 * (A[1] + B[1]) - 0.05,
        s="$2$",
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
    main(dirname=dirname, save=False)
