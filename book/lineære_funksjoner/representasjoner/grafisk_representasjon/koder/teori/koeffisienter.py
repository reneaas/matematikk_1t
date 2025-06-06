import plotmath


def main(dirname, save):

    # Define functions
    def f(x):
        return 2 * x - 1

    # List of functions and their labels.
    functions = [f]
    fn_labels = None

    # Create the math figure
    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=fn_labels,  # Set `None` hvis du ikke vil ha labels.
        xmin=-3,
        xmax=6,
        ymin=-4,
        ymax=10,
        ticks=False,
        grid=False,
    )

    import matplotlib.pyplot as plt

    x0 = 2
    dx = 2
    xticks = [x0, x0 + dx]
    yticks = [f(x0), f(x0 + dx)]
    ax.plot(x0, f(x0), "ko", markersize=8, alpha=0.7)
    ax.plot(x0 + dx, f(x0 + dx), "ko", markersize=8, alpha=0.7)
    ax.plot(0, f(0), "ko", markersize=8, alpha=0.7)

    xticks_labels = [r"$x$", r"$x + 1$"]
    yticks_labels = [r"$f(x)$", r"$f(x + 1)$"]

    plt.xticks(xticks, labels=xticks_labels, fontsize=16)
    plt.yticks(yticks, labels=yticks_labels, fontsize=16)

    ax.hlines(f(x0), x0, x0 + dx, color="black", linestyle="--", lw=1)
    ax.vlines(x0 + dx, f(x0), f(x0 + dx), color="black", linestyle="--", lw=1)

    # Annotate dx = 1
    ax.annotate(
        "",
        xy=(x0, f(x0) - 0.5),
        xycoords="data",
        xytext=(x0 + dx, f(x0) - 0.5),
        textcoords="data",
        arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="blue"),
    )

    ax.text(
        s="$1$",
        x=x0 + dx / 2,
        y=f(x0) - 1,
        fontsize=16,
        color="blue",
        horizontalalignment="center",
        verticalalignment="center",
    )

    # Annotate dy = f(x + 1) - f(x) = a
    ax.annotate(
        "",
        xy=(x0 + dx + 0.3, f(x0)),
        xycoords="data",
        xytext=(x0 + dx + 0.3, f(x0 + dx)),
        textcoords="data",
        arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="blue"),
    )

    ax.text(
        s="$a$",
        x=x0 + dx + 0.5,
        y=f(x0 + dx / 2),
        fontsize=16,
        color="blue",
        horizontalalignment="center",
        verticalalignment="center",
    )

    # Annotate the y-intercept
    plt.annotate(
        text="$y = f(0)= b$",
        xy=(0, f(0)),
        xytext=(-1.5, 1.5),
        fontsize=16,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=+0.4",
        ),
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
