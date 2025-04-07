import plotmath
import numpy as np
import matplotlib.pyplot as plt


def make_circle_arc(radius, center, start_angle, end_angle):
    start_angle = np.radians(start_angle)
    end_angle = np.radians(end_angle)
    theta = np.linspace(start_angle, end_angle, 1024)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)

    plt.plot(x, y, color="k", ls="-")


def main(dirname, save):
    # TODO: write code here

    a = 1
    A = (0, 0)
    B = (a, 0)
    angle = np.radians(180 - 60)
    D = (a * np.cos(angle), a * np.sin(angle))
    angle = np.radians(180 - 30 - 75)
    C = (a + np.sqrt(2) * a * np.cos(angle), np.sqrt(2) * a * np.sin(angle))

    plotmath.plot_polygon(
        A,
        B,
        C,
        D,
        show_vertices=False,
        alpha=0.05,
    )

    make_circle_arc(
        center=A,
        radius=0.15,
        start_angle=0,
        end_angle=120,
    )

    plt.text(
        x=0.18,
        y=0.18,
        s="$120^\\circ$",
        fontsize=20,
        ha="center",
        va="center",
    )

    make_circle_arc(
        center=B,
        radius=0.2,
        start_angle=180 - 30,
        end_angle=180 - 30 - 75,
    )

    plt.text(
        x=B[0] - 0.1,
        y=B[1] + 0.25,
        s="$75^\\circ$",
        fontsize=20,
        ha="center",
        va="center",
    )

    make_circle_arc(
        center=D,
        radius=0.3,
        start_angle=180 - 30 + 180,
        end_angle=180 - 30 + 180 - 30,
    )

    plt.text(
        x=D[0] + 0.3,
        y=D[1] - 0.3,
        s="$30^\\circ$",
        fontsize=20,
        ha="center",
        va="center",
    )

    # Label AB
    dy = 0.05
    plt.text(
        x=(A[0] + B[0]) / 2,
        y=(A[1] + B[1]) / 2 - dy,
        s="$a$",
        fontsize=20,
        ha="center",
        va="top",
    )

    # Label BC
    dx = dy = 0.05
    plt.text(
        x=(B[0] + C[0]) / 2 + dx,
        y=(B[1] + C[1]) / 2,
        s="$\\sqrt{2} \\cdot a$",
        fontsize=20,
        ha="left",
        va="top",
    )

    # Draw diagonal BD
    plt.plot([B[0], D[0]], [B[1], D[1]], "k--")

    # Label vertices

    plt.text(
        x=A[0],
        y=A[1] - 0.05,
        s="$A$",
        fontsize=20,
        ha="right",
        va="top",
    )

    plt.text(
        x=B[0],
        y=B[1] - 0.05,
        s="$B$",
        fontsize=20,
        ha="left",
        va="top",
    )

    plt.text(
        x=C[0] + 0.05,
        y=C[1],
        s="$C$",
        fontsize=20,
        ha="left",
        va="bottom",
    )

    plt.text(
        x=D[0] - 0.05,
        y=D[1],
        s="$D$",
        fontsize=20,
        ha="right",
        va="bottom",
    )

    plt.axis("off")
    plt.axis("equal")

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
