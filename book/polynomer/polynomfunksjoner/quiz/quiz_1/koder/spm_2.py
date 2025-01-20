import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -((x + 1) ** 2) * (x - 1)

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-4,
        xmax=4,
        ymin=-2,
        ymax=2,
        ticks=False,
    )

    xticks = list(range(-3, 4))
    xticks.remove(0)

    xtick_labels = [f"${x}$" for x in xticks]

    ax.set_xticks(xticks)
    ax.set_xticklabels(xtick_labels, fontsize=16)

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
