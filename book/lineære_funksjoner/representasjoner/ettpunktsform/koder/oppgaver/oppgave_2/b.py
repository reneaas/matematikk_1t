import plotmath


def main(dirname, save):
    #
    # Define functions
    def g(x):
        return -2 * (x + 2) + 3

    # List of functions and their labels.
    functions = [g]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-6,
        xmax=6,
        ymin=-6,
        ymax=6,
        ticks=True,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    P = (-2, 3)
    ax.plot(*P, "ko", markersize=8)
    ax.text(
        x=P[0],
        y=P[1],
        s="$Q$",
        fontsize=20,
        color="black",
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
