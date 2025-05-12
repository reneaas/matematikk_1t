import plotmath
import numpy as np
import matplotlib.pyplot as plt


def make_circle(center, radius):
    theta = np.linspace(0, 2 * np.pi, 1024)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)

    return x, y


def make_angle_arc(center, radius, start_angle, end_angle):
    start_angle = np.deg2rad(start_angle)
    end_angle = np.deg2rad(end_angle)
    theta = np.linspace(start_angle, end_angle, 1024)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)

    return x, y


def main(dirname, save):
    # TODO: write code here

    x, y = make_circle((0, 0), 1)
    fig, ax = plotmath.plot(
        functions=[],
        fn_labels=False,
        xmin=-2,
        xmax=2,
        ymin=-2,
        ymax=2,
        ticks=True,
        grid=False,
    )

    ax.plot(x, y, color=plotmath.COLORS.get("blue"), lw=2.5)

    angle = 50
    angle_rad = np.deg2rad(angle)
    x0 = np.cos(angle_rad)
    y0 = np.sin(angle_rad)

    ax.plot([0, x0], [0, y0], color="black", lw=1.5)

    ax.plot(x0, y0, "ko", markersize=8, alpha=0.7)

    x, y = make_angle_arc(
        center=(0, 0),
        radius=0.2,
        start_angle=0,
        end_angle=angle,
    )

    ax.plot(x, y, color="black", lw=1.5)

    ax.text(
        x=0.3,
        y=0.1,
        s=r"$50^\circ$",
        fontsize=20,
        ha="center",
        va="center",
    )

    ax.text(
        x=x0 + 0.05,
        y=y0,
        s=r"$\left(0.64, 0.77\right)$",
        fontsize=20,
        ha="left",
        va="bottom",
    )

    ax.axis("equal")

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
