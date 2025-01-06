import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return (x + 1) ** 2 - 4

    def make_tangent_fn(f, a, h=1e-5):
        slope = 0.5 * (f(a + h) - f(a - h)) / h

        def tangent(x):
            return f(a) + slope * (x - a)

        return tangent

    # List of functions and their labels.
    tangent = make_tangent_fn(f=f, a=1)
    functions = [f, tangent]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=["$f$", "tangent"],
        xmin=-6,
        xmax=6,
        ymin=-6,
        ymax=6,
        ticks=True,
    )

    ax.plot(1, f(1), "ko", markersize=8, alpha=0.7)

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
