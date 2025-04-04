import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -2 * (x + 3) * (x - 4)

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-4,
        xmax=7,
        ymin=-8,
        ymax=26,
        ticks=True,
        xstep=1,
        ystep=4,
        grid=False,
    )

    dx = dy = 1
    ax.plot(-3, 0, "ko", markersize=8, alpha=0.7)
    ax.text(
        x=-3,
        y=0 + dy,
        s="$(-3, 0)$",
        fontsize=16,
        ha="right",
        va="bottom",
    )

    ax.plot(4, 0, "ko", markersize=8, alpha=0.7)
    ax.text(
        x=4,
        y=0 + dy,
        s="$(4, 0)$",
        fontsize=16,
        ha="left",
        va="bottom",
    )

    ax.plot(0, 24, "ko", markersize=8, alpha=0.7)
    dx = 0.2
    ax.text(
        x=0 + dx,
        y=24 - dy,
        s="$(0, 24)$",
        fontsize=16,
        ha="left",
        va="top",
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
