import plotmath
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    x0 = -3
    y0 = 1
    a = -2

    def g(x):
        return a * (x - x0) ** 2 + y0

    # List of functions and their labels.
    functions = [g]

    fig, ax = plotmath.plot(
        functions=functions,
        # fn_labels=[
        #     (
        #         f"$g(x) = {a}(x - {x0})^2 + {y0}$"
        #         if x0 > 0
        #         else f"$g(x) = {a}(x + {-x0})^2 + {y0}$"
        #     )
        # ],
        fn_labels=True,
        xmin=-6,
        xmax=3,
        ymin=-4,
        ymax=4,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    ax.vlines(x=x0, ymin=-20, ymax=20, color="red", lw=1.5, ls="--")

    fontsize = 28
    ax.text(
        x=x0 - 0.5,
        y=2 * y0,
        s=f"$x = {x0}$",
        fontsize=fontsize,
        va="center",
        ha="right",
        color="red",
    )

    ax.plot(x0, y0, "ko", markersize=10, alpha=0.7)
    ax.text(
        x0 + 0.15,
        y0 + 0.15,
        f"$({x0}, {y0})$",
        fontsize=fontsize,
        va="bottom",
        ha="left",
    )

    # Set font sizes for legend and axes labels
    ax.legend(fontsize=fontsize)
    ax.yaxis.label.set_size(fontsize)  # Set y-axis label font size
    ax.xaxis.label.set_size(fontsize)  # Set x-axis label font size

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
