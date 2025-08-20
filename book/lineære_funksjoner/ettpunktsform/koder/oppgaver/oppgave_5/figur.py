import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -(x + 1) + 2

    def g(x):
        return -(x - 2) + 1

    # List of functions and their labels.
    functions = [f, g]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-4,
        xmax=4,
        ymin=-2,
        ymax=6,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )
    P = (-1, 2)
    Q = (0, 1)

    R = (2, g(2))

    ax.plot(*P, "ko", markersize=8)
    ax.text(
        x=P[0],
        y=P[1],
        s="$(-1, 2)$",
        fontsize=20,
        color="black",
        ha="left",
        va="bottom",
    )

    ax.plot(*Q, "ko", markersize=8)
    ax.text(
        x=Q[0] + 0.2,
        y=Q[1],
        s="$(0, 1)$",
        fontsize=20,
        color="black",
        ha="left",
        va="bottom",
    )

    ax.plot(*R, "ko", markersize=8)
    ax.text(
        x=R[0] + 0.2,
        y=R[1],
        s=f"$(2, {g(2)})$",
        fontsize=20,
        color="black",
        ha="left",
        va="bottom",
    )

    A = (1, 0)
    B = (3, 0)
    C = (0, 3)
    D = (0, 1)

    plotmath.plot_polygon(
        A,
        B,
        C,
        D,
        ax=ax,
        alpha=0.3,
        edges=False,
    )

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
