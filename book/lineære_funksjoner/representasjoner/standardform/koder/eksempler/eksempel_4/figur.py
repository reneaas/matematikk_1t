import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return 3 * x - 5

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-2,
        xmax=6,
        ymin=-8,
        ymax=6,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    ax.plot(0, -5, "ko", markersize=10, alpha=0.8)
    ax.text(
        x=0 - 0.2,
        y=-5,
        s="$(0, -5)$",
        fontsize=20,
        ha="right",
        va="center",
    )

    ax.plot(2, f(2), "ko", markersize=10, alpha=0.8)
    ax.text(
        x=2 + 0.2,
        y=f(2),
        s=f"$(2, {f(2)})$",
        fontsize=20,
        ha="left",
        va="center",
    )

    fontsize = 20
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(fontsize)  # Set to desired font size

    ax.yaxis.label.set_size(fontsize)  # Set y-axis label font size
    ax.xaxis.label.set_size(fontsize)  # Set x-axis label font size

    ax.legend(fontsize=fontsize)

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
