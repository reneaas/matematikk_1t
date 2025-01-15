import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -(x + 1) * (x - 1) * (x - 2)

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=["$p'$"],
        xmin=-4,
        xmax=4,
        ymin=-6,
        ymax=6,
        ticks=False,
    )

    ax.plot(-1, 0, "ko", markersize=8, alpha=0.7)
    ax.plot(1, 0, "ko", markersize=8, alpha=0.7)
    ax.plot(2, 0, "ko", markersize=8, alpha=0.7)

    dx = dy = 0.1
    ax.text(
        x=-1 - dx,
        y=0 - dy,
        s="$(-1, 0)$",
        fontsize=16,
        va="top",
        ha="right",
    )

    ax.text(
        x=1 - dx,
        y=0 + dy,
        s="$(1, 0)$",
        fontsize=16,
        va="bottom",
        ha="right",
    )

    ax.text(
        x=2 + dx,
        y=0 + dy,
        s="$(2, 0)$",
        fontsize=16,
        va="bottom",
        ha="left",
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
