import plotmath
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return 1 * 2**x

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-6,
        xmax=6,
        ymin=-2.5,
        ymax=int(2**4) + 5,
        ticks=False,
    )

    xticks = [i for i in range(-5, 6)]
    if 0 in xticks:
        xticks.remove(0)

    yticks = [2**i for i in range(5)]

    xticklabels = [f"${i}$" for i in xticks]

    yticklabels = [f"${i}$" for i in yticks]

    ax.set_xticks(xticks)
    ax.set_yticks(yticks)

    ax.set_xticklabels(xticklabels, fontsize=16)
    ax.set_yticklabels(yticklabels, fontsize=16)

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
