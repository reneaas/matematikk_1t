import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -2 * (x - 4) * x

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-3,
        xmax=6,
        ymin=-6,
        ymax=10,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
        fontsize=20,
        figsize=None,
    )

    ax.plot(4, 0, "ko", ms=8)
    ax.plot(1, 6, "ko", ms=8)
    ax.text(x=4, y=0, s="$(4, 0)$", fontsize=20, ha="left", va="bottom")
    ax.text(x=1, y=6, s="$(1, 6)$", fontsize=20, ha="right", va="bottom")

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
