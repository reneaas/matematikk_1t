import plotmath
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    x1 = -2
    x2 = 4
    a = -0.5

    def h(x):
        return a * (x - x1) * (x - x2)

    # List of functions and their labels.
    functions = [h]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-6,
        xmax=6,
        ymin=-6,
        ymax=6,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    ax.plot(x1, 0, "ko", markersize=10, alpha=0.7)
    ax.plot(x2, 0, "ko", markersize=10, alpha=0.7)

    # Set font sizes for legend and axes labels
    fontsize = 28
    ax.legend(fontsize=fontsize)
    ax.yaxis.label.set_size(fontsize)  # Set y-axis label font size
    ax.xaxis.label.set_size(fontsize)  # Set x-axis label font size

    ax.text(
        x=x1 - 0.2,
        y=0 + 0.2,
        s=f"$({x1}, 0)$",
        fontsize=fontsize,
        va="bottom",
        ha="right",
    )

    ax.text(
        x=x2 + 0.2,
        y=0 + 0.2,
        s=f"$({x2}, 0)$",
        fontsize=fontsize,
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
