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
    ax.plot(x, y, color="black")


def main(dirname, save):
    # TODO: write code here

    angle = 45
    radius = 2
    S = (0, 0)
    A = (radius, 0)
    B = (radius * np.cos(angle * np.pi / 180), radius * np.sin(angle * np.pi / 180))
    C = (-radius * np.cos(angle * np.pi / 180), -radius * np.sin(angle * np.pi / 180))

    points = [S, A, B]
    plotmath.plot_polygon(
        *points,
        show_vertices=True,
    )

    points = [S, A, C]
    plotmath.plot_polygon(
        *points,
        show_vertices=True,
    )

    x, y = make_circle(center=S, radius=2)

    plt.plot(x, y, color="black")

    draw_circle_arc(
        center=C,
        radius=0.7,
        start_angle=45,
        end_angle=22.5,
    )

    angle = 22.5
    plt.text(
        x=C[0] + 0.8,
        y=C[1] + 0.5,
        s=f"${angle}^\\circ$",
        fontsize=20,
        ha="left",
        va="bottom",
    )

    plt.text(
        x=S[0] - 0.1,
        y=S[1] + 0.1,
        s=r"$S$",
        fontsize=20,
        ha="left",
        va="bottom",
    )

    plt.text(
        x=A[0] + 0.1,
        y=A[1],
        s=r"$A$",
        fontsize=20,
        ha="left",
        va="center",
    )

    plt.text(
        x=B[0] + 0.1,
        y=B[1] + 0.2,
        s=r"$B$",
        fontsize=20,
        ha="left",
        va="top",
    )

    plt.text(
        x=C[0] - 0.1,
        y=C[1] - 0.1,
        s=r"$C$",
        fontsize=20,
        ha="right",
        va="center",
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
