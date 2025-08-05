import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -((x - 1) ** 2) + 3

    def g(x):
        return 1 * (x + 1) - 1

    # List of functions and their labels.
    functions = [f, g]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-6,
        xmax=6,
        ymin=-6,
        ymax=6,
        ticks=True,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(25)  # Set to desired font size

    ax.yaxis.label.set_size(25)  # Set y-axis label font size
    ax.xaxis.label.set_size(25)  # Set x-axis label font size

    ax.text(
        x=4,
        y=4,
        s="C",
        fontsize=25,
        bbox=dict(facecolor="white", edgecolor="black", boxstyle="round,pad=0.3"),
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
