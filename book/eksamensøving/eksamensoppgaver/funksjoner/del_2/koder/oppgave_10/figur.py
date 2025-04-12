import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return 8 / (x**2 + 20)

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-1,
        xmax=15,
        ymin=-0.1,
        ymax=0.5,
        ticks=True,
        xstep=1,
        ystep=0.1,
        grid=False,
        lw=2.5,
        alpha=0.8,
        domain=(0, 15),
    )

    A = (0, 0)
    B = (5, 0)
    C = (5, f(5))
    D = (0, f(5))

    plotmath.plot_polygon(
        A,
        B,
        C,
        D,
        alpha=0.2,
        color="teal",
        show_vertices=True,
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
