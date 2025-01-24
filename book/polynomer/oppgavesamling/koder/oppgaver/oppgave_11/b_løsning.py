import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -(1 / 3 * x**3 + x**2 - 3 * x - 4)

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=["$g$"],
        xmin=-6,
        xmax=6,
        ymin=-8,
        ymax=8,
        ticks=False,
    )

    ax.plot(1, f(1), "ko", markersize=8, alpha=0.7)
    dy = dx = 0.5
    ax.text(
        x=1,
        y=f(1) + dy,
        s="$(1, g(1))$",
        fontsize=16,
        ha="center",
        va="bottom",
    )

    ax.plot(-3, f(-3), "ko", markersize=8, alpha=0.7)
    dy = dx = 0.5
    ax.text(
        x=-3,
        y=f(-3) - dy,
        s="$(-3, g(-3))$",
        fontsize=16,
        ha="center",
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
