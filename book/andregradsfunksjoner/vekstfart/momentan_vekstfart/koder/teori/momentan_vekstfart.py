import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return x**2

    def make_tangent_fn(f, a, h=1e-5):
        slope = (f(a + h) - f(a)) / h

        def T(x):
            return slope * (x - a) + f(a)

        return T

    a = 1
    T = make_tangent_fn(f=f, a=a)
    # List of functions and their labels.
    functions = [f, T]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=["$f$", "Tangent"],
        xmin=-3,
        xmax=3,
        ymin=-2,
        ymax=6,
        ticks=False,
    )

    ax.plot(a, f(a), "ko", markersize=8, alpha=0.7)
    ax.text(
        s="$(a, f(a))$",
        x=a + 0.2,
        y=f(a),
        ha="left",
        va="center",
        fontsize=16,
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