import numpy as np
import matplotlib.pyplot as plt
import plotmath

plt.rc("text", usetex=True)


def circle_arc(center, radius, start_angle, end_angle, n_points=128):
    angles = np.linspace(start_angle, end_angle, n_points)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y


def main(dirname, save):
    A = (0, 0)
    B = (4, 0)
    C = (3, 4)

    plt.fill([A[0], B[0], C[0]], [A[1], B[1], C[1]], "teal", alpha=0.1)
    plt.plot(
        [A[0], B[0], C[0], A[0]],
        [
            A[1],
            B[1],
            C[1],
            A[1],
        ],
        "k",
    )

    plt.plot(*A, "ko", markersize=8, alpha=0.7)
    plt.plot(*B, "ko", markersize=8, alpha=0.7)
    plt.plot(*C, "ko", markersize=8, alpha=0.7)

    A = np.array(A)
    B = np.array(B)
    C = np.array(C)

    AB = B - A
    AC = C - A

    angle1 = np.arccos(np.dot(AB, AC) / (np.linalg.norm(AB) * np.linalg.norm(AC)))

    BC = C - B
    BA = A - B

    angle2 = np.arccos(np.dot(BC, BA) / (np.linalg.norm(BC) * np.linalg.norm(BA)))

    angle3 = np.pi - angle1 - angle2

    x, y = circle_arc(center=A, radius=0.5, start_angle=0, end_angle=angle1)

    plt.plot(x, y, "k")

    x, y = circle_arc(center=B, radius=0.5, start_angle=np.pi - angle2, end_angle=np.pi)

    plt.plot(x, y, "k")

    x, y = circle_arc(center=C, radius=0.5, start_angle=0, end_angle=np.pi)

    plt.plot(x, y, "k")

    x, y = circle_arc(
        center=C, radius=0.5, start_angle=np.pi + angle1, end_angle=2 * np.pi - angle2
    )

    plt.plot(x, y, "k")

    plt.hlines(y=0, xmin=-1, xmax=5, color="k", linestyle="--")
    plt.hlines(y=4, xmin=-1, xmax=5, color="k", linestyle="--")

    slope = (C[1] - B[1]) / (C[0] - B[0])
    x = np.linspace(-1, 5, 100)
    y = slope * (x - B[0]) + B[1]
    plt.plot(x, y, "k--")

    slope = (C[1] - A[1]) / (C[0] - A[0])
    x = np.linspace(-1, 5, 100)
    y = slope * (x - A[0]) + A[1]
    plt.plot(x, y, "k--")

    plt.text(
        x=0.7,
        y=0.3,
        s="$a$",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.text(
        x=4 - 0.7,
        y=0.4,
        s="$b$",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.text(
        x=3 - 0.15,
        y=4 - 0.8,
        s="$c$",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.text(
        x=C[0] - 0.5,
        y=C[1] + 0.5,
        s=r"$x$",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.text(
        x=C[0] + 0.1,
        y=C[1] + 0.8,
        s=r"$y$",
        fontsize=16,
        ha="left",
        va="center",
    )

    plt.text(
        x=C[0] + 0.6,
        y=C[1] + 0.4,
        s=r"$z$",
        fontsize=16,
        ha="left",
        va="center",
    )

    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.xlim(-0.5, 4.5)
    plt.ylim(-1, 6.5)

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
