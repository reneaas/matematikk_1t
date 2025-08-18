import matplotlib.pyplot as plt
import numpy as np
import plotmath

plt.rc("text", usetex=True)


def calculate_trajectory(H, y0, x0):
    g = 9.81
    a = np.array([0, -g])
    v0 = np.array([np.sqrt(2 * g * H), 0])
    r0 = np.array([x0, y0])

    t = np.linspace(0, np.sqrt(2 * y0 / g), 1024)
    r = np.zeros((len(t), 2))
    r[:, 0] = r0[0] + v0[0] * t
    r[:, 1] = r0[1] + v0[1] * t + 0.5 * a[1] * t**2

    return r


def plot_trajectory(H, y0, x0, hole_size):
    trajectory_lower = calculate_trajectory(
        H=H + hole_size,
        x0=x0,
        y0=y0,
    )
    trajectory_upper = calculate_trajectory(
        H=H,
        x0=x0,
        y0=y0 + hole_size,
    )
    plt.gca().fill_between(
        trajectory_lower[:, 0],
        trajectory_lower[:, 1],
        trajectory_upper[:, 1],
        color=plotmath.COLORS.get("blue"),
    )


def main(dirname, save, R, h, table_height, p, g=9.81):
    plt.figure(figsize=(5, 6))

    hole_size = 0.3
    plt.plot([0, R], [table_height, table_height], color="black")
    plt.plot(
        [R, R],
        [table_height + hole_size, table_height + h],
        color="black",
    )
    plt.plot([0, 0], [table_height, table_height + h], color="black")

    H = table_height + p * h

    # Trajectory for the first hole
    plot_trajectory(H=H, y0=table_height, x0=R, hole_size=hole_size)

    A = (0, table_height)
    B = (0, H + table_height)
    C = (R, H + table_height)
    D = (R, table_height)

    plt.fill(
        [A[0], B[0], C[0], D[0]],
        [A[1], B[1], C[1], D[1]],
        color=plotmath.COLORS.get("blue"),
    )

    dy = 0.05
    plt.annotate(
        "",
        xy=(-0.5, table_height),
        xycoords="data",
        xytext=(-0.5, table_height + H + dy),
        textcoords="data",
        arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="black"),
    )

    plt.text(
        x=-1,
        y=0.5 * (table_height + H + 0.1 * h),
        s="$x_2$",
        fontsize=28,
        ha="right",
        va="center",
    )
    plt.hlines(y=0, xmin=-2, xmax=R + 6, linestyle="-", color="black")

    S = R + np.sqrt(2 * g * H) * np.sqrt(2 * table_height / g)
    # plt.plot(S, 0, "ko")

    dx = 0.1
    plt.annotate(
        "",
        xy=(R - dx, -0.5),
        xycoords="data",
        xytext=(S + dx, -0.5),
        textcoords="data",
        arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="black"),
    )

    plt.text(
        x=0.5 * (R + S),
        y=-1,
        s="$S_2$",
        fontsize=28,
        ha="center",
        va="top",
    )

    # Table
    A = (0, 0)
    B = (0, table_height)
    C = (R, table_height)
    D = (R, 0)

    plt.fill(
        [A[0], B[0], C[0], D[0]],
        [A[1], B[1], C[1], D[1]],
        color="brown",
        alpha=0.5,
    )

    plt.xlim(-2, R + 6.5)

    plt.axis("off")

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname,
            fname=fname,
            transparent=True,
        )  # Lagrer figuren i `dirname`-directory

    if not save:

        plotmath.show()

    plt.show()


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

    main(
        dirname=dirname,
        save=True,
        R=2,
        h=10,
        table_height=1,
        p=0.2,
    )
