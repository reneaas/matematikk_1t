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
        xstep=2,
        ystep=2,
    )

    xticks = [i for i in range(-3, 7, 1)]
    yticks = [i for i in range(-2, 7, 1)]

    xticks.remove(0)
    yticks.remove(0)

    xtick_labels = []
    for xtick in xticks:
        if xtick % 2 == 0:
            xtick_labels.append(f"${xtick}$")
        else:
            xtick_labels.append("")

    ytick_labels = []
    for ytick in yticks:
        if ytick % 2 == 0:
            ytick_labels.append(f"${ytick}$")
        else:
            ytick_labels.append("")

    # Set ticks and labels
    ax.set_xticks(xticks)
    ax.set_xticklabels(xtick_labels, fontsize=16)
    ax.set_yticks(yticks)
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
