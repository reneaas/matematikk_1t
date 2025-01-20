import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -(x**4 / 4 - 2 / 3 * x**3 - x**2 / 2 + 2 * x - 3)

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=["$p$"],
        xmin=-4,
        xmax=4,
        ymin=-2,
        ymax=6,
        ticks=True,
    )

    # ticks = list(range(-5, 6))
    # ticks.remove(0)
    # ax.set_xticks(ticks)
    # ax.set_xticklabels([f"${t}$" for t in ticks], fontsize=16)

    # ax.grid(False)

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
