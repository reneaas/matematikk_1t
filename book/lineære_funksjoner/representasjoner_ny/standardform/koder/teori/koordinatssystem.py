import plotmath


def main(dirname, save):

    # List of functions and their labels.
    functions = []

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-2,
        xmax=6,
        ymin=-3,
        ymax=5,
        ticks=True,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=0.8,
        domain=False,
    )

    point = (3, 2)
    ax.plot(*point, "ko", markersize=8, alpha=0.7)

    x0, y0 = point
    ax.hlines(y0, 0, x0, color=plotmath.COLORS.get("red"), lw=2.5, linestyle="--")
    ax.vlines(x0, 0, y0, color=plotmath.COLORS.get("red"), lw=2.5, linestyle="--")

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
