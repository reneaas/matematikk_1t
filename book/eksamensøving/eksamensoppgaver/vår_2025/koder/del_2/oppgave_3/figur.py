import plotmath
import numpy as np
import matplotlib.pyplot as plt


def make_circle(center, radius, num_points=1024):
    angles = np.linspace(0, 2 * np.pi, num_points)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y


def draw_circle_arc(center, radius, start_angle, end_angle, num_points=100):
    ax = plt.gca()
    start_angle = np.radians(start_angle)
    end_angle = np.radians(end_angle)
    angles = np.linspace(start_angle, end_angle, num_points)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    ax.plot(x, y, color="black", lw=1)


def main(dirname, save):
    # TODO: write code here

    x, y = make_circle(center=(0, 0), radius=1)
    plt.plot(x, y, color="black")

    n = 12
    angles = [360 / n * i for i in range(n)]
    angles = [np.radians(angle) for angle in angles]

    points = [(np.cos(angle), np.sin(angle)) for angle in angles]

    origin = [0, 0]
    for point in points:
        plt.plot(*zip(origin, point), color="black", lw=1)

    plotmath.plot_polygon(
        *points,
        alpha=0.15,
    )

    draw_circle_arc(
        center=(0, 0),
        radius=0.3,
        start_angle=0,
        end_angle=30,
    )

    plt.text(
        x=0.45,
        y=0.1,
        s="$30^\\circ$",
        fontsize=18,
        ha="center",
        va="center",
    )

    # x, y = zip(*points)

    # plt.plot(x + x[:1], y + y[:1], color="black", lw=2)

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
