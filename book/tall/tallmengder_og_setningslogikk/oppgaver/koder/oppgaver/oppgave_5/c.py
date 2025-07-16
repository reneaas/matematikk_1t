import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import plotmath

# Enable LaTeX rendering
mpl.rcParams["text.usetex"] = True
mpl.rcParams["font.size"] = 18


def prime_factors(n):
    for i in range(2, n + 1):
        if n % i == 0:
            if i == n:
                return [n]
            return [i] + prime_factors(n // i)


def build_tree(n):
    factors = prime_factors(n)
    if len(factors) == 1:
        return (n, [])
    left = factors[0]
    right = n // left
    return (n, [build_tree(left), build_tree(right)])


def get_tree_depth(node):
    if not node[1]:
        return 1
    return 1 + max(get_tree_depth(child) for child in node[1])


def plot_tree(
    node, x=0, y=0, ax=None, level=0, max_depth=None, branch_length=1.8, angle_deg=30
):
    if ax is None:
        # fig_height = (max_depth or 5) * branch_length * 1.2
        # fig, ax = plt.subplots(figsize=(4, fig_height))
        fig, ax = plt.subplots()
        ax.axis("off")
        ax.set_aspect("equal")

    angle_rad = np.radians(angle_deg)
    dx = branch_length * np.sin(angle_rad)
    dy = -branch_length * np.cos(angle_rad)

    value, children = node
    ax.text(
        x,
        y,
        f"${value}$",
        ha="center",
        va="center",
        bbox=dict(
            boxstyle="circle,pad=0.3",
            facecolor="#e0f7fa",
            # edgecolor="#00796b",
            edgecolor=plotmath.COLORS.get("blue"),
            linewidth=1.5,
        ),
    )

    if children:
        offsets = [-dx, dx]
        for child, offset_x in zip(children, offsets):
            child_x = x + offset_x
            child_y = y + dy
            ax.plot([x, child_x], [y, child_y], color="#455a64", linewidth=1.2)
            plot_tree(
                child,
                x=child_x,
                y=child_y,
                ax=ax,
                level=level + 1,
                max_depth=max_depth,
                branch_length=branch_length,
                angle_deg=angle_deg,
            )

    if ax is not None and level == 0:
        total_depth = max_depth or 6
        ax.set_xlim(-dx * total_depth, dx * total_depth)


def main(dirname, save):
    # Example usage
    n = 102
    tree = build_tree(n)
    depth = get_tree_depth(tree)
    plot_tree(tree, max_depth=depth, angle_deg=30)

    fig = plt.gcf()
    fig.set_size_inches(3, 3)  # Set figure size to 6x6 inches
    plt.tight_layout()

    # NOTE: Automatically saves with correct file format and filename.
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
