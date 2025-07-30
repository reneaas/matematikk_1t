import matplotlib.pyplot as plt
import plotmath

plt.rc("text", usetex=True)


def main(dirname, save):
    #
    # Define functions
    def f(x, a=1, b=-1):
        return a * x + b

    # List of functions and their labels.
    a = 1
    b = -2
    functions = [lambda x: f(x, a=a, b=b)]
    fn_labels = [f"$f$" for fn in functions]

    # Create the math figure
    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=fn_labels,  # NOTE: Set `None` hvis du ikke vil ha labels.
        xmin=-8,
        xmax=8,
        ymin=-8,
        ymax=8,
        ticks=False,
    )

    ax.plot(-b / a, 0, "ko", markersize=10, alpha=0.7)

    ax.hlines(
        y=0, xmin=-b / a, xmax=100, color=plotmath.COLORS.get("red"), alpha=0.6, lw=8
    )

    # ax.text(
    #     s=r"$ax + b > 0$ eller $ax + b \geq 0$",
    #     x=0,
    #     y=4,
    #     fontsize=16,
    #     bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=2),
    #     horizontalalignment="center",
    #     verticalalignment="center",
    # )

    x_coord = 4.5
    ax.annotate(
        text="Løsningsmengde",
        xy=(-b / a + 0.5, 0),
        xytext=(x_coord, -3),
        fontsize=16,
        arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.annotate(
        text="Løsningsmengde",
        xy=(x_coord, 0),
        xytext=(x_coord, -3),
        fontsize=16,
        arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.annotate(
        text="Løsningsmengde",
        xy=(-b / a + 5, 0),
        xytext=(x_coord, -3),
        fontsize=16,
        arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.annotate(
        text=r"Nullpunkt er inkludert for $f(x) \geq 0$",
        xy=(-b / a, 0),
        xytext=(-6, 4),
        fontsize=16,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=-0.3",
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

        plt.show()


if __name__ == "__main__":

    import sys
    import pathlib

    def find_repo_root(current_path):
        current_path = pathlib.Path(
            current_path
        ).resolve()  # Convert to an absolute Path object
        while (
            current_path != current_path.parent
        ):  # Stop when you reach the filesystem root
            if (current_path / ".git").is_dir():  # Check if the .git directory exists
                return str(current_path)
            current_path = current_path.parent  # Move one level up
        raise FileNotFoundError("No .git directory found in any parent directories.")

    # Get the directory where the script is located
    current_dir = str(pathlib.Path(__file__).resolve().parent)

    # Find the root of the GitHub repository (where .git is located)
    repo_root = find_repo_root(current_dir)

    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break

    dirname = "/".join(parts)

    # NOTE: Set `save=True` to save figure. `save=False` to display figure.
    main(dirname=dirname, save=True)
