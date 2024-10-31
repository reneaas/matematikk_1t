import plotmath
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return (x - 3) ** 2 - 2

    def g(x):
        return ((x + 3) ** 2) - 2

    # List of functions and their labels.
    functions = [f, g]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-6,
        xmax=6,
        ymin=-6,
        ymax=6,
        ticks=False,
    )

    plt.text(
        x=3,
        y=-5,
        s="$a > 0$",
        fontsize=18,
        ha="center",
        color="black",
        bbox=dict(
            facecolor="white",
            alpha=0.5,
            edgecolor="black",
            boxstyle="round,pad=0.3",
        ),
    )

    plt.text(
        x=3,
        y=3,
        s="$b < 0$ \n høyre for $y$-aksen",
        fontsize=18,
        ha="center",
        color="black",
        bbox=dict(
            facecolor="teal",
            alpha=0.5,
            edgecolor="black",
            boxstyle="round,pad=0.3",
        ),
    )

    plt.text(
        x=-3,
        y=3,
        s="$b > 0$ \n venstre for $y$-aksen",
        fontsize=18,
        ha="center",
        color="black",
        bbox=dict(
            facecolor="#C875C4",
            alpha=0.5,
            edgecolor="black",
            boxstyle="round,pad=0.3",
        ),
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
