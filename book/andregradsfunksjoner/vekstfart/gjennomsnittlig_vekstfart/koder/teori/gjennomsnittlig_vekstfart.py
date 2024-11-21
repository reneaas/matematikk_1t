import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return (x - 1) ** 2

    def make_sekant_fn(f, a, b):
        slope = (f(b) - f(a)) / (b - a)

        def S(x):
            return slope * (x - a) + f(a)

        return S

    a = -0.5
    b = 3
    S = make_sekant_fn(f=f, a=a, b=b)
    # List of functions and their labels.
    functions = [f, S]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=["$f$", "Sekant"],
        xmin=-3,
        xmax=5,
        ymin=-2,
        ymax=6,
        ticks=False,
    )

    ax.plot(a, f(a), "ko", markersize=8, alpha=0.7)
    ax.plot(b, f(b), "ko", markersize=8, alpha=0.7)

    ax.text(
        s="$(a, f(a))$",
        x=a - 0.2,
        y=f(a),
        fontsize=16,
        ha="right",
        va="bottom",
    )

    ax.text(
        s="$(b, f(b))$",
        x=b + 0.2,
        y=f(b),
        fontsize=16,
        ha="left",
        va="top",
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
