import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return (x - 1) * (x + 2) + 4

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-4,
        xmax=4,
        ymin=-2,
        ymax=6,
        ticks=False,
    )

    ax.plot(1, 4, "ko", markersize=10, alpha=0.7)
    ax.plot(-2, 4, "ko", markersize=10, alpha=0.7)

    ax.hlines(y=4, xmin=-10, xmax=10, lw=2, alpha=0.7, color="blue", label="$y = y_0$")
    ax.vlines(x=1, ymin=0, ymax=4, linestyle="--", color="black", alpha=0.5)
    ax.vlines(x=-2, ymin=0, ymax=4, linestyle="--", color="black", alpha=0.5)

    xticks = [-2, 1]
    xlabels = ["$x_1$", "$x_2$"]

    ax.set_xticks(xticks, xlabels, fontsize=16)

    ax.legend(fontsize=16)
    ax.grid(False)

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
