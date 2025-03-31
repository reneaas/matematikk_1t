import plotmath
import numpy as np
import matplotlib.pyplot as plt


def make_circle_arc(center, radius, start_angle, end_angle, n=100):
    import numpy as np

    angles = np.linspace(start_angle, end_angle, n)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y


def main(dirname, save):
    # TODO: write code here

    fig, ax = plt.subplots()

    xmin = -1.5
    xmax = 1.5
    ymin = -1.5
    ymax = 1.5
    ax.vlines(x=0, ymin=ymin, ymax=ymax, color="black")
    ax.hlines(y=0, xmin=xmin, xmax=xmax, color="black")

    A = (xmin, 0)
    B = (xmin, ymin)
    C = (xmax, ymin)
    D = (xmax, 0)

    x, y = zip(*[A, B, C, D])

    ax.fill(x, y, color="lightblue", alpha=0.5)
    ax.text(
        x=0 + 0.1,
        y=1,
        s="$m$",
        fontsize=20,
        ha="left",
        va="center",
    )

    angle_air = 150
    x = (xmax**2 + ymax**2) ** 0.5 * np.cos(np.radians(angle_air))
    y = (xmax**2 + ymax**2) ** 0.5 * np.sin(np.radians(angle_air))

    ax.plot([0, x], [0, y], color="red")

    ax.text(
        x=x / 2,
        y=y / 2,
        s=r"Lysstråle",
        fontsize=16,
        ha="left",
        va="bottom",
        color="red",
    )

    angle_water = np.arcsin(np.sin(np.radians(angle_air - 90)) / 1.33)
    print(np.degrees(angle_water))

    x = 20 * np.cos(-np.pi / 2 + angle_water)
    y = 20 * np.sin(-np.pi / 2 + angle_water)

    ax.plot([0, x], [0, y], color="red")

    start_angle = np.pi / 2
    end_angle = np.radians(angle_air)
    radius = 0.3
    x, y = make_circle_arc(
        center=(0, 0),
        radius=radius,
        start_angle=start_angle,
        end_angle=end_angle,
    )

    ax.plot(x, y, color="black")

    x_label = 1.5 * radius * 0.5 * (np.cos(start_angle) + np.cos(end_angle))
    y_label = 1.5 * radius * 0.5 * (np.sin(start_angle) + np.sin(end_angle))

    ax.text(
        x=x_label,
        y=y_label,
        s=r"$u$",
        fontsize=20,
        ha="center",
        va="center",
    )

    start_angle = -np.pi / 2
    end_angle = -np.pi / 2 + angle_water
    radius = 0.3
    x, y = make_circle_arc(
        center=(0, 0),
        radius=radius,
        start_angle=start_angle,
        end_angle=end_angle,
    )

    x_label = 1.5 * radius * 0.5 * (np.cos(start_angle) + np.cos(end_angle))
    y_label = 1.5 * radius * 0.5 * (np.sin(start_angle) + np.sin(end_angle))

    ax.text(
        x=x_label,
        y=y_label,
        s=r"$v$",
        fontsize=20,
        ha="center",
        va="center",
    )

    ax.plot(x, y, color="black")

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, xmax)

    ax.axis("off")
    ax.set_aspect("equal")
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
