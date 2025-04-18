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

    s = 2
    A = np.array((0, 0))
    unit_vector = np.array((1, 0))
    B = A + s * unit_vector
    angle = 180 - 128.57
    C = B + s * np.array((np.cos(np.radians(angle)), np.sin(np.radians(angle))))
    angle += 180 - 128.57
    D = C + s * np.array((np.cos(np.radians(angle)), np.sin(np.radians(angle))))
    angle += 180 - 128.57
    E = D + s * np.array((np.cos(np.radians(angle)), np.sin(np.radians(angle))))
    angle += 180 - 128.57
    F = E + s * np.array((np.cos(np.radians(angle)), np.sin(np.radians(angle))))
    angle += 180 - 128.57
    G = F + s * np.array((np.cos(np.radians(angle)), np.sin(np.radians(angle))))

    A = tuple(A)
    B = tuple(B)
    C = tuple(C)
    D = tuple(D)
    E = tuple(E)
    F = tuple(F)
    G = tuple(G)

    plotmath.plot_polygon(
        A,
        B,
        C,
        D,
        E,
        F,
        G,
        show_vertices=False,
        alpha=0.03,
    )

    # Label vertices
    plt.text(
        x=A[0] - 0.1,
        y=A[1] - 0.2,
        s=r"$A$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.text(
        x=B[0] + 0.1,
        y=B[1] - 0.2,
        s=r"$B$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.text(
        x=C[0] + 0.2,
        y=C[1],
        s=r"$C$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.text(
        x=D[0] + 0.2,
        y=D[1] + 0.1,
        s=r"$D$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.text(
        x=E[0],
        y=E[1] + 0.2,
        s=r"$E$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.text(
        x=F[0] - 0.2,
        y=F[1] + 0.1,
        s=r"$F$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.text(
        x=G[0] - 0.2,
        y=G[1],
        s=r"$G$",
        fontsize=20,
        ha="center",
        va="center",
    )

    make_circle_arc(
        center=B,
        radius=0.3,
        start_angle=180,
        stop_angle=180 - 128.57,
    )

    plt.text(
        x=B[0] - 0.2,
        y=B[1] + 0.45,
        s=r"$128.57^\circ$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.plot(*zip(A, C), ls="--", color="black", alpha=0.7)
    plt.plot(*zip(A, F), ls="--", color="black", alpha=0.7)
    plt.plot(*zip(F, C), ls="--", color="black", alpha=0.7)
    plt.plot(*zip(C, E), ls="--", color="black", alpha=0.7)

    plt.text(
        x=0.5 * s,
        y=-0.2,
        s="$2$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()

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
