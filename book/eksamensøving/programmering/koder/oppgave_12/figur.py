import matplotlib.pyplot as plt
import plotmath

plt.rc("text", usetex=True)


def main(dirname, save):

    L = 2
    x = 1.4
    A = (0, 1)
    B = (x, 0)
    D = (L, 0)
    C = (L, -1)

    plt.plot(*A, "ko", markersize=8, alpha=0.7)
    plt.text(
        x=A[0] - 0.01,
        y=A[-1] + 0.1,
        s="$A$",
        fontsize=16,
        ha="right",
        va="center",
    )
    plt.plot([A[0], B[0]], [A[1], B[1]], color="red")

    plt.text(
        x=0.5 * (A[0] + B[0]),
        y=0.5 * (A[-1] + B[-1]),
        s="Lysstråle",
        fontsize=16,
        ha="left",
        va="bottom",
        color="red",
    )

    plt.plot(*B, "ko", markersize=8, alpha=0.7)
    plt.text(
        x=B[0] + 0.05,
        y=B[-1],
        s="$M$",
        fontsize=16,
        ha="left",
        va="bottom",
    )

    plt.plot([B[0], C[0]], [B[1], C[1]], color="red")
    plt.plot(*C, "ko", markersize=8, alpha=0.7)
    plt.text(
        x=C[0] + 0.05,
        y=C[-1] - 0.1,
        s="$C$",
        fontsize=16,
        ha="left",
        va="center",
    )

    plt.vlines(x=0, ymin=0, ymax=A[-1], linestyle="--", color="black")

    plt.text(
        x=-0.35,
        y=0.5 * A[-1],
        s="$1000 \\, \\mathrm{m}$",
        fontsize=16,
        ha="right",
        va="center",
    )

    plt.annotate(
        "",
        xy=(A[0] - 0.3, 0),
        xycoords="data",
        xytext=(A[0] - 0.3, A[-1]),
        textcoords="data",
        arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="black"),
    )

    plt.vlines(x=C[0], ymin=0, ymax=C[-1], linestyle="--", color="black")

    plt.text(
        x=C[0] + 0.40,
        y=0.5 * C[-1],
        s="$1000 \\, \\mathrm{m}$",
        fontsize=16,
        ha="left",
        va="center",
    )

    plt.annotate(
        "",
        xy=(C[0] + 0.3, 0),
        xycoords="data",
        xytext=(C[0] + 0.3, C[-1]),
        textcoords="data",
        arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="black"),
    )

    plt.hlines(y=0, xmin=-20, xmax=20)

    plt.text(
        x=0.5 * B[0],
        y=-0.1,
        s="$x$",
        fontsize=16,
        ha="center",
        va="top",
    )

    plt.annotate(
        "",
        xy=(0 - 0.02, -0.1),
        xycoords="data",
        xytext=(x + 0.02, -0.1),
        textcoords="data",
        arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="black"),
    )

    plt.annotate(
        "",
        xy=(0 - 0.02, -1.2),
        xycoords="data",
        xytext=(L + 0.02, -1.2),
        textcoords="data",
        arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="black"),
    )

    plt.text(
        x=0.5 * L,
        y=-1,
        s="$10 \\, 000 \\, \\mathrm{m}$",
        fontsize=16,
        ha="center",
        va="top",
    )

    dx = 0.15
    dy = 0.15

    plt.plot([0, dx], [dy, dy], linestyle="-", color="black", lw=0.8)
    plt.plot([dx, dx], [dy, 0], linestyle="-", color="black", lw=0.8)

    plt.plot([L, L - dx], [-dy, -dy], linestyle="-", color="black", lw=0.8)
    plt.plot([L - dx, L - dx], [-dy, 0], linestyle="-", color="black", lw=0.8)

    # S = (0, 0)
    # plt.plot(*S, "ro", markersize=8, alpha=0.7)
    # plt.text(
    #     x=S[0] - 0.05,
    #     y=S[-1] - 0.3,
    #     s="$S$",
    #     fontsize=16,
    #     ha="right",
    #     va="center",
    #     color="red",
    # )

    plt.text(
        x=-0.8,
        y=1,
        s="Luft",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.text(
        x=-0.8,
        y=-1,
        s="Vann",
        fontsize=16,
        ha="center",
        va="center",
    )

    plt.ylim(-1.5, 1.5)

    plt.axis("off")
    plt.axis("equal")
    plt.xlim(-1, 3)

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
