def main(dirname, save):

    # Define functions
    def f(x):
        return 2 * x - 3

    # List of functions and their labels.
    functions = []
    fn_labels = None

    # Create the math figure
    fig, ax = make_figure(
        functions=functions,
        fn_labels=fn_labels,  # Set `None` hvis du ikke vil ha labels.
        xmin=-6,
        xmax=6,
        ymin=-6,
        ymax=6,
        ticks=True,
    )

    A = (1, 2)
    B = (-2, 3)
    C = (3, -1)
    D = (-5, -3)
    E = (4, 4)
    F = (2, -4)

    punkter = {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F}

    for punktnavn in punkter:
        x, y = punkter.get(punktnavn)
        ax.plot(x, y, "ko", markersize=8, alpha=0.7)

        ax.text(
            s=f"${punktnavn}$",
            x=x + 0.2,
            y=y - 0.2,
            fontsize=16,
            ha="left",
            va="bottom",
        )

    # ax.text(
    #     s=r"$A$",
    #     x=A[0] + 0.2,
    #     y=A[1] + 0.2,
    #     fontsize=16,
    #     ha="left",
    #     va="bottom",
    # )

    # ax.text(
    #     s=r"$B$",
    #     x=B[0] - 0.2,
    #     y=B[1] + 0.2,
    #     fontsize=16,
    #     ha="right",
    #     va="bottom",
    # )

    # ax.text(
    #     s=r"$C$",
    #     x=C[0] + 0.2,
    #     y=C[1] - 0.2,
    #     fontsize=16,
    #     ha="left",
    #     va="top",
    # )

    # ax.text(
    #     s=r"$C$",
    #     x=C[0] + 0.2,
    #     y=C[1] - 0.2,
    #     fontsize=16,
    #     ha="left",
    #     va="top",
    # )

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        savefig(dirname=dirname, fname=fname)  # Lagrer figuren i `dirname`-directory

    if not save:
        import matplotlib.pyplot as plt

        plt.show()


if __name__ == "__main__":

    import sys
    import os

    def find_repo_root(current_path):
        while current_path != os.path.dirname(
            current_path
        ):  # Stop when you reach the filesystem root
            if os.path.isdir(os.path.join(current_path, ".git")):
                return current_path
            current_path = os.path.dirname(current_path)
        raise FileNotFoundError("No .git directory found in any parent directories.")

    # Get the directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Find the root of the GitHub repository (where .git is located)
    repo_root = find_repo_root(current_dir)

    # Add the GitHub repository root to sys.path
    sys.path.append(repo_root)

    # Now you can import modules from the GitHub repo root
    from python_templates.plot_utils import make_figure, savefig

    # NOTE: Set `save=True` to save figure. `save=False` to display figure.
    dirname = "../../figurer/underveisoppgaver/"
    main(dirname=dirname, save=True)
