import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return 2 * (x - 2)

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-4,
        xmax=7,
        ymin=-3,
        ymax=7,
        ticks=False,
        xstep=1,
        ystep=1,
        alpha=0.8,
    )

    xticks = [i for i in range(-4, 7)]
    xticks.remove(0)

    yticks = [i for i in range(-2, 7)]
    yticks.remove(0)

    ax.set_xticks(xticks)
    ax.set_yticks(yticks)

    xtick_labels = [f"${i}$" if i % 2 == 0 else "" for i in xticks]
    ytick_labels = [f"${i}$" if i % 2 == 0 else "" for i in yticks]

    ax.set_xticklabels(xtick_labels, fontsize=16)
    ax.set_yticklabels(ytick_labels, fontsize=16)

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
