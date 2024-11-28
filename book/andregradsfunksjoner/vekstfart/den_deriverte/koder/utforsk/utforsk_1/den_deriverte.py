import plotmath


def main(dirname, save):
    #
    # Define functions

    def f(x):
        return 0.5 * ((x + 2) ** 2 - 4)

    def make_secant_fn(f, a, b):
        slope = (f(b) - f(a)) / (b - a)

        def secant(x):
            return f(a) + slope * (x - a)

        return secant

    def make_tangent_fn(f, a, h=1e-5):
        slope = (f(a + h) - f(a - h)) / (2 * h)

        def tangent(x):
            return f(a) + slope * (x - a)

        return tangent

    # List of functions and their labels.
    x0 = -1
    secant = make_secant_fn(f=f, a=x0 - 1, b=x0 + 1)
    tangent = make_tangent_fn(f=f, a=x0)
    functions = [f, secant, tangent]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=["$f$", "sekant", "tangent"],
        xmin=-6,
        xmax=2,
        ymin=-4,
        ymax=3,
        ticks=True,
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
    main(dirname=dirname, save=False)
