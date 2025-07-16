import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return (x - 1) ** 2 * (x + 3)

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-5,
        xmax=4,
        ymin=-6,
        ymax=12,
        ticks=False,
    )

    ax.plot([-3, 1], [0, 0], "ko", markersize=8, alpha=0.7)

    dx = 0.1
    dy = 0.2
    ax.text(
        x=1,
        y=0 - dy,
        s="$(1, 0)$",
        fontsize=16,
        va="top",
        ha="right",
    )

    ax.text(
        x=-3 - dx,
        y=0 + dy,
        s="$(-3, 0)$",
        fontsize=16,
        va="bottom",
        ha="right",
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
