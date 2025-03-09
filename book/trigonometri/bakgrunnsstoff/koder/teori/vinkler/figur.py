import matplotlib.pyplot as plt
import numpy as np
import plotmath

plt.rc("text", usetex=True)


def circle_arc(center, radius, start_angle, end_angle, n_points=128):
    angles = np.linspace(start_angle, end_angle, n_points)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y


def main(dirname, save):
    plt.hlines(y=0, xmin=-2, xmax=2, color="k", lw=2)
    plt.hlines(y=1, xmin=-2, xmax=2, color="k", lw=2)

    x = np.linspace(-2, 2, 1024)
    plt.plot(x, x + 1, "k")

    x, y = circle_arc(center=(0, 1), radius=0.5, start_angle=0, end_angle=np.pi / 4)
    plt.plot(x, y, "r")

    x, y = circle_arc(
        center=(0, 1), radius=0.5, start_angle=np.pi, end_angle=np.pi + np.pi / 4
    )
    plt.plot(x, y, "r")

    x, y = circle_arc(center=(-1, 0), radius=0.5, start_angle=0, end_angle=np.pi / 4)
    plt.plot(x, y, "r")

    x, y = circle_arc(
        center=(-1, 0), radius=0.5, start_angle=np.pi, end_angle=np.pi + np.pi / 4
    )

    plt.plot(x, y, "r")

    x, y = circle_arc(
        center=(-1, 0), radius=0.3, start_angle=np.pi / 4, end_angle=np.pi
    )
    plt.plot(x, y, "b")

    x, y = circle_arc(
        center=(-1, 0), radius=0.3, start_angle=np.pi + np.pi / 4, end_angle=2 * np.pi
    )
    plt.plot(x, y, "b")

    x, y = circle_arc(center=(0, 1), radius=0.3, start_angle=np.pi / 4, end_angle=np.pi)
    plt.plot(x, y, "b")

    x, y = circle_arc(
        center=(0, 1), radius=0.3, start_angle=np.pi + np.pi / 4, end_angle=2 * np.pi
    )
    plt.plot(x, y, "b")

    plt.text(
        x=-0.8,
        y=-0.4,
        s="$a$",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.text(
        x=-1.2,
        y=0.4,
        s="$a$",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.text(
        x=0.7,
        y=1.2,
        s="$b$",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.text(
        x=-0.65,
        y=0.7,
        s="$b$",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.axis("equal")
    plt.axis("off")

    plt.xlim(-2, 2)
    plt.ylim(-0.5, 2)

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
