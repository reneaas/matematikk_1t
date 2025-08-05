import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -(x**2) + 1

    def g(x):
        return -x - 1

    # List of functions and their labels.
    functions = [f, g]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=["$x^2 + y = 1$", "$x + y = -1$"],
        xmin=-5,
        xmax=5,
        ymin=-5,
        ymax=5,
        ticks=True,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
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
