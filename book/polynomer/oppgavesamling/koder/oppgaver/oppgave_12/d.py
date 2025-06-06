import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x, a=4):
        return a * (x - 1) ** 2 * (x + 2)

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=["$p'$"],
        xmin=-4,
        xmax=4,
        ymin=-4,
        ymax=18,
        ticks=True,
        ystep=2,
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
