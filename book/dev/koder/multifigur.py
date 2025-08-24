import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return (x + 1) ** 2 - 3

    def g(x):
        return (x - 2) ** 2 + 1

    def h(x):
        return -(x**2) + 4

    def r(x):
        return (x + 3) ** 2 - 4

    # List of functions and their labels.
    functions = [f, g, h]

    letters = ["A", "B", "C", "D"]
    fig, axes = plotmath.multiplot(
        functions=[],
        fn_labels=False,
        xmin=-6,
        xmax=6,
        ymin=-6,
        ymax=6,
        xstep=1,
        ystep=1,
        ticks=True,
        alpha=None,
        grid=True,
        rows=1,
        cols=3,
        figsize=(10, 3),
        lw=2.5,
    )

    fig.savefig("test.svg", format="svg", bbox_inches="tight", transparent=True)

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
    main(dirname=dirname, save=False)
