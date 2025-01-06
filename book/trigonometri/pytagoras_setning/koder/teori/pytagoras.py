import matplotlib.pyplot as plt
import plotmath

plt.rc("text", usetex=True)


def main(dirname, save):

    A = (0, 0)
    B = (2, 0)
    C = (0, 2)

    plt.plot(*A, "ko", markersize=8, alpha=0.7)
    plt.plot(*B, "ko", markersize=8, alpha=0.7)
    plt.plot(*C, "ko", markersize=8, alpha=0.7)

    plt.text(
        x=A[0] - 0.05,
        y=A[-1],
        s="$A$",
        fontsize=18,
        ha="right",
        va="top",
    )

    plt.text(
        x=B[0] + 0.05,
        y=B[-1],
        s="$B$",
        fontsize=18,
        ha="left",
        va="top",
    )

    plt.text(
        x=C[0] - 0.05,
        y=C[-1],
        s="$C$",
        fontsize=18,
        ha="right",
        va="bottom",
    )

    plt.plot(*[[x, y] for x, y in zip(A, B)], color="blue", lw=2)
    plt.plot(*[[x, y] for x, y in zip(B, C)], color="red", lw=2)
    plt.plot(*[[x, y] for x, y in zip(C, A)], color="teal", lw=2)

    dx = 0.2
    dy = 0.25

    plt.plot([0, dx], [dy, dy], color="black", lw=1)
    plt.plot([dx, dx], [dy, 0], color="black", lw=1)

    plt.text(
        x=0.5 * B[0],
        y=-0.1,
        s="$a$",
        fontsize=22,
        ha="center",
        va="top",
        color="blue",
    )

    plt.text(
        x=0.5 * (B[0] + C[0]),
        y=0.5 * (B[-1] + C[-1]) + 0.2,
        s="$c$",
        fontsize=22,
        ha="left",
        va="top",
        color="red",
    )

    plt.text(
        x=-0.1,
        y=0.5 * C[-1],
        s="$b$",
        fontsize=22,
        ha="right",
        va="center",
        color="teal",
    )

    plt.axis("off")
    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname,
            fname=fname,
        )

    if not save:

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
    main(dirname=dirname, save=True)
