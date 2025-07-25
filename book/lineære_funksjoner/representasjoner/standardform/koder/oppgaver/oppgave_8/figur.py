import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -2 * x + 3

    def g(x):
        return 2 * x - 1

    def h(x):
        return 2 * x + 1

    # List of functions and their labels.
    import numpy as np

    np.random.seed(42)

    functions = [f, g, h]

    functions = np.random.permutation(functions).tolist()

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=["A", "B", "C"],
        xmin=-4,
        xmax=4,
        ymin=-6,
        ymax=6,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=False,
        lw=2.5,
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
