import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return x**3 + 7 * x**2 + 4 * x - 12

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-10,
        xmax=4,
        ymin=-24,
        ymax=24,
        ticks=False,
    )

    ax.hlines(
        y=0,
        xmin=-25,
        xmax=-6,
        color="red",
        lw=5,
        alpha=0.6,
    )

    ax.hlines(
        y=0,
        xmin=-2,
        xmax=1,
        color="red",
        lw=5,
        alpha=0.6,
    )

    ax.annotate(
        text="$x \\in \\langle \\gets , -6 \\rangle \\cup \\langle -2, 1 \\rangle$",
        xy=(-1, 0),
        xytext=(-6, -17),
        arrowprops=dict(arrowstyle="->", lw=1.5),
        fontsize=20,
    )

    ax.annotate(
        text="$x \\in \\langle \\gets , -6 \\rangle \\cup \\langle -2, 1 \\rangle$",
        xy=(-7, 0),
        xytext=(-6, -17),
        arrowprops=dict(arrowstyle="->", lw=1.5),
        fontsize=20,
    )

    ax.annotate(
        text="$f(x) < 0$",
        xy=(0.5, f(0.5)),
        xytext=(2, -15),
        arrowprops=dict(arrowstyle="->", lw=1.5),
        fontsize=20,
    )

    ax.annotate(
        text="$f(x) < 0$",
        xy=(-6.5, f(-6.5)),
        xytext=(-10, -12),
        arrowprops=dict(arrowstyle="->", lw=1.5),
        fontsize=20,
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
