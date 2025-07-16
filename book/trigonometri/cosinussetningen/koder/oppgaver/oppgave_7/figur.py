import plotmath
import numpy as np
import matplotlib.pyplot as plt


def make_circle_arc(center, radius, start_angle, stop_angle):
    start_angle = np.radians(start_angle)
    stop_angle = np.radians(stop_angle)
    angles = np.linspace(start_angle, stop_angle, 1024)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    plt.plot(x, y, color="black", lw=1.5)


def main(dirname, save):
    # TODO: write code here

    s = 1
    A = (0, 0)
    B = (s, 0)

    angle = 72
    C = (B[0] + s * np.cos(np.radians(angle)), B[1] + s * np.sin(np.radians(angle)))
    angle += 72

    D = (C[0] + s * np.cos(np.radians(angle)), C[1] + s * np.sin(np.radians(angle)))
    angle += 72

    E = (D[0] + s * np.cos(np.radians(angle)), D[1] + s * np.sin(np.radians(angle)))

    plotmath.plot_polygon(
        A,
        B,
        C,
        D,
        E,
        show_vertices=False,
        alpha=0.1,
        color=plotmath.COLORS.get("rare"),
    )

    plt.plot(*zip(A, C), ls="--", color="black")

    plt.plot(*zip(C, E), ls="--", color="black")

    # Label vertices
    plt.text(
        x=A[0] - 0.1,
        y=A[1] - 0.1,
        s=r"$A$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.text(
        x=B[0] + 0.1,
        y=B[1] - 0.1,
        s=r"$B$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.text(
        x=C[0] + 0.1,
        y=C[1],
        s=r"$C$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.text(
        x=D[0],
        y=D[1] + 0.1,
        s=r"$D$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.text(
        x=E[0] - 0.1,
        y=E[1],
        s=r"$E$",
        fontsize=20,
        ha="center",
        va="center",
    )

    make_circle_arc(
        center=B,
        radius=0.15,
        start_angle=180,
        stop_angle=180 - 108,
    )

    plt.text(
        x=B[0] - 0.15,
        y=B[1] + 0.2,
        s=r"$108^\circ$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.text(
        x=0.5 * s,
        y=-0.1,
        s=r"$\ell$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.axis("equal")
    plt.axis("off")

    # NOTE: Automatically saves with correct file format and filename.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname,
            fname=fname,
            transparent=True,
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
