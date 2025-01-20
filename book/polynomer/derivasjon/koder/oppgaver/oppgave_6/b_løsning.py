import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return 1 / 3 * x**3 - 4 * x + 2

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=["$g$"],
        xmin=-6,
        xmax=6,
        ymin=-6,
        ymax=10,
        ticks=False,
    )

    ax.plot(2, f(2), "ko", markersize=8, alpha=0.7)
    ax.plot(-2, f(-2), "ko", markersize=8, alpha=0.7)

    xticks = list(range(-6, 7))
    xticks.remove(0)
    ax.set_xticks(xticks)
    ax.set_xticklabels([f"${x}$" for x in xticks], fontsize=16)

    dy = 0.5
    ax.text(
        x=2,
        y=f(2) - dy,
        s="$(2, g(2))$",
        fontsize=16,
        va="top",
        ha="center",
    )

    ax.text(
        x=-2,
        y=f(-2) + dy,
        s="$(-2, g(-2))$",
        fontsize=16,
        va="bottom",
        ha="center",
    )

    ax.grid(False)

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
