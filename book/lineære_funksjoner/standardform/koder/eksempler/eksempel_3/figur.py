import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -x + 2

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-5,
        xmax=5,
        ymin=-2,
        ymax=5,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    ax.plot(0, f(0), "ko", markersize=10, alpha=0.8)
    ax.text(
        x=0 + 0.2,
        y=f(0),
        s=f"$(0, {f(0)})$",
        fontsize=20,
        ha="left",
        va="bottom",
    )

    x0 = -2
    y0 = f(x0)
    ax.hlines(
        y=y0, xmin=x0, xmax=x0 + 1, lw=2.5, ls="--", color=plotmath.COLORS.get("red")
    )
    ax.text(
        x=0.5 * (x0 + x0 + 1),
        y=y0 + 0.5,
        s="$1$",
        fontsize=20,
        ha="center",
        va="bottom",
    )

    ax.vlines(
        x=x0 + 1,
        ymin=min(f(x0), f(x0 + 1)),
        ymax=max(f(x0), f(x0 + 1)),
        lw=2.5,
        ls="--",
        color=plotmath.COLORS.get("red"),
    )

    ax.text(
        x=x0 + 1 + 0.2,
        y=0.5 * (f(x0) + f(x0 + 1)),
        s="$-1$",
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
