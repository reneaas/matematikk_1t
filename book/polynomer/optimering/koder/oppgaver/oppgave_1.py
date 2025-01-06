import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -(x**2) + 16

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-5,
        xmax=5,
        ymin=-2,
        ymax=17,
        ticks=False,
        domain=[-4, 4],
    )

    color = "blue"
    x0 = 3

    A = [-x0, 0]
    C = [x0, f(x0)]
    B = [x0, 0]
    D = [-x0, f(-x0)]

    ax.fill(
        [A[0], B[0], C[0], D[0]],
        [A[1], B[1], C[1], D[1]],
        color=color,
        alpha=0.1,
    )

    ax.plot([A[0], B[0]], [A[1], B[1]], color=color, lw=1.5, alpha=0.7)
    ax.plot([B[0], C[0]], [B[1], C[1]], color=color, lw=1.5, alpha=0.7)
    ax.plot([C[0], D[0]], [C[1], D[1]], color=color, lw=1.5, alpha=0.7)
    ax.plot([D[0], A[0]], [D[1], A[1]], color=color, lw=1.5, alpha=0.7)

    ax.plot(*A, "ko", markersize=8, alpha=0.7)
    ax.plot(*B, "ko", markersize=8, alpha=0.7)
    ax.plot(*C, "ko", markersize=8, alpha=0.7)
    ax.plot(*D, "ko", markersize=8, alpha=0.7)

    dy = 0.2
    dx = 0.2

    ax.text(
        x=x0,
        y=f(x0) + dy,
        s="$(3, f(3))$",
        color="black",
        fontsize=16,
        ha="left",
        va="bottom",
    )

    ax.text(
        x=-x0,
        y=f(x0) + dy,
        s="$(-3, f(-3))$",
        color="black",
        fontsize=16,
        ha="right",
        va="bottom",
    )

    ticks = [i for i in range(-4, 5, 1)]
    ticks.remove(0)
    ax.set_xticks(ticks)
    ax.tick_params(axis="x", labelsize=16)
    ax.grid(False)

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
