import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return 2 * x + 8

    def g(x):
        return x**3 - x**2 - 4 * x + 8

    # List of functions and their labels.
    functions = [f, g]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-1,
        xmax=5,
        ymin=-2,
        ymax=24,
        ticks=False,
    )

    ax.vlines(
        x=1,
        ymin=-1,
        ymax=100,
        color="gray",
        linestyle="-",
        lw=2,
        alpha=1,
    )

    ax.text(
        x=1,
        y=-3,
        s="$x = 1$",
        fontsize=20,
        ha="center",
        va="bottom",
    )

    P = (1, f(1))
    Q = (1, g(1))

    ax.plot(*P, "ko", markersize=8, alpha=0.7)
    ax.plot(*Q, "ko", markersize=8, alpha=0.7)

    dx = dy = 0.5
    ax.text(
        x=P[0] + 0.1 * dx,
        y=P[1] + dy,
        s="$P$",
        fontsize=20,
        ha="left",
        va="bottom",
    )

    ax.text(
        x=Q[0] + 0.1 * dx,
        y=Q[1],
        s="$Q$",
        fontsize=20,
        ha="left",
        va="bottom",
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
