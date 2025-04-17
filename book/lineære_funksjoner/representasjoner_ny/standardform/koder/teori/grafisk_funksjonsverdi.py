import plotmath


def main(dirname, save):

    # Define functions
    def f(x):
        return x - 1

    # List of functions and their labels.
    functions = [f]

    # Create the math figure
    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,  # Set `None` hvis du ikke vil ha labels.
        xmin=-2,
        xmax=6,
        ymin=-4,
        ymax=6,
        ticks=False,
        grid=False,
    )

    import matplotlib.pyplot as plt

    x0 = 4
    xticks = [x0]
    yticks = [f(x0)]
    ax.plot(x0, f(x0), "ko", markersize=8, alpha=0.7)

    xticks_labels = [r"$c$"]
    yticks_labels = [r"$f(c)$"]

    plt.xticks(xticks, labels=xticks_labels, fontsize=16)
    plt.yticks(yticks, labels=yticks_labels, fontsize=16)

    plt.annotate(
        text="$(c, f(c))$",
        xy=(x0, f(x0)),
        xytext=(2.2, 5),
        fontsize=16,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=-0.4",
        ),
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.hlines(f(x0), 0, x0, color="black", linestyle="--", lw=1)
    ax.vlines(x0, 0, f(x0), color="black", linestyle="--", lw=1)

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname, fname=fname
        )  # Lagrer figuren i `dirname`-directory

    if not save:
        import matplotlib.pyplot as plt

        plt.show()


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
