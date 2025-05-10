import plotmath
import numpy as np
import matplotlib.pyplot as plt


def make_circle(x, y, r):
    theta = np.linspace(0, 2 * np.pi, 1024)
    x_circle = x + r * np.cos(theta)
    y_circle = y + r * np.sin(theta)
    return x_circle, y_circle


def make_circle_arc(center, r, start_angle, end_angle):
    x, y = center
    theta = np.linspace(start_angle, end_angle, 1024)
    x_circle = x + r * np.cos(theta)
    y_circle = y + r * np.sin(theta)
    return x_circle, y_circle


def main(dirname, save):
    # TODO: write code here

    r = 1
    x, y = make_circle(x=0, y=0, r=r)

    plt.plot(x, y, color="black", lw=1.5)

    S = (0, 0)
    B = (r, 0)
    C = (0, r)

    angle = -120
    angle_rad = np.deg2rad(angle)
    A = (r * np.cos(angle_rad), r * np.sin(angle_rad))

    # plotmath.plot_polygon(
    #     A,
    #     B,
    #     C,
    #     alpha=0,
    # )

    ax = plt.gca()
    color = plotmath.COLORS.get("blue")
    ax.plot(*zip(A, B), lw=2.5, color=color)
    ax.plot(*zip(B, C), lw=2.5, color=color)
    ax.plot(*zip(C, A), lw=2.5, color=color)

    dx = dy = 0.1

    ax.plot([S[0], S[0] + dx], [S[1] + dy, S[1] + dy], color="black", lw=2)
    ax.plot([S[0] + dx, S[0] + dx], [S[1], S[1] + dy], color="black", lw=2)

    ax.plot(*zip(S, B), color="black", ls="--")
    ax.plot(*zip(S, C), color="black", ls="--")
    ax.plot(*zip(S, A), color="black", ls="--")

    x, y = make_circle_arc(B, 0.3, np.deg2rad(180), np.deg2rad(180 + 30))
    ax.plot(x, y, color="black", lw=1.5)

    ax.text(
        x=B[0] - 0.40,
        y=B[1] - 0.15,
        s=r"$30^\circ$",
        fontsize=20,
        ha="center",
    )

    # label lengths
    ax.text(
        x=0.5 * (S[0] + B[0]),
        y=0.5 * (S[1] + B[1]),
        s=r"$r$",
        fontsize=20,
        ha="center",
        va="bottom",
    )

    ax.text(
        x=0.5 * (S[0] + A[0]) + 0.15,
        y=0.5 * (S[1] + A[1]) + 0.1,
        s=r"$r$",
        fontsize=20,
        ha="left",
        va="center",
    )

    ax.text(
        x=0.5 * (S[0] + C[0]) + 0.05,
        y=0.5 * (S[1] + C[1]),
        s=r"$r$",
        fontsize=20,
        ha="left",
        va="center",
    )

    # Label vertices
    ax.text(
        x=S[0] - 0.08,
        y=S[1],
        s=r"$S$",
        fontsize=20,
        ha="center",
        va="center",
    )

    ax.text(
        x=B[0] + 0.08,
        y=B[1],
        s=r"$B$",
        fontsize=20,
        ha="center",
        va="center",
    )

    ax.text(
        x=A[0] - 0.03,
        y=A[1] - 0.08,
        s=r"$A$",
        fontsize=20,
        ha="center",
        va="center",
    )

    ax.text(
        x=C[0],
        y=C[1] + 0.08,
        s=r"$C$",
        fontsize=20,
        ha="center",
        va="center",
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
