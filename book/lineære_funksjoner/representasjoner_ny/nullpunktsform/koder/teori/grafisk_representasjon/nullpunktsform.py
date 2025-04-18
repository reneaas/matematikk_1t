import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -2 * (x - 3)

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-2,
        xmax=6,
        ymin=-6,
        ymax=7,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        domain=False,
    )

    x0 = 3
    y0 = f(x0)

    ax.plot(
        x0,
        y0,
        "ro",
        markersize=8,
        alpha=0.8,
    )

    ax.annotate(
        text="Nullpunkt \n Skjæring med $x$-aksen",
        xy=(x0, f(x0)),
        xytext=(1, -4),
        fontsize=16,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="red",
            alpha=0.7,
            connectionstyle="arc3,rad=-0.4",
        ),
        horizontalalignment="left",
        verticalalignment="center",
        color="red",
    )

    x0 = 1
    y0 = f(x0)
    x1 = 2
    y1 = f(x1)

    ax.hlines(y=y0, xmin=x0, xmax=x1, color="black", linestyle="--", lw=1)
    ax.vlines(x=x1, ymin=y1, ymax=y0, color="blue", linestyle="--", lw=1)

    ax.text(
        x=0.5 * (x0 + x1),
        y=y0 + 0.3,
        s="$1$",
        fontsize=20,
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.text(
        x=x1 + 0.2,
        y=0.5 * (y0 + y1),
        s="$a$",
        fontsize=20,
        horizontalalignment="center",
        verticalalignment="center",
        color="blue",
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
