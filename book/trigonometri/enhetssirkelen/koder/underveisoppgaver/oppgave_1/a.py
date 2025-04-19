import plotmath
import numpy as np
import matplotlib.pyplot as plt


def make_circle(radius=1):
    t = np.linspace(0, 2 * np.pi, 1024)
    x = radius * np.cos(t)
    y = radius * np.sin(t)
    return x, y


def make_circle_arc(stop, radius=0.3, start=0):
    t = np.linspace(start, stop, 1024)
    x = radius * np.cos(t)
    y = radius * np.sin(t)
    return x, y


def draw_angle_arc_with_tangent_arrow(
    ax, center, start_angle, end_angle, radius, arrow_length=0.1
):
    """
    Draws an angle arc with an arrow tangent to the end of the arc.

    Args:
        ax: Matplotlib Axes object to draw on.
        center: Tuple (x, y) representing the center of the arc.
        start_angle: Starting angle of the arc in degrees.
        end_angle: Ending angle of the arc in degrees.
        radius: Radius of the arc.
        arrow_length: Length of the arrow as a fraction of the radius.
    """

    # Convert angles to radians
    start_rad = np.radians(start_angle)
    end_rad = np.radians(end_angle)

    # Generate points for the arc
    theta = np.linspace(start_rad, end_rad, 100)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)

    # Plot the arc
    ax.plot(x, y, "k-")

    # Calculate the arrow's starting point (end of the arc)
    arrow_start_x = center[0] + radius * np.cos(end_rad)
    arrow_start_y = center[1] + radius * np.sin(end_rad)

    # Calculate the tangent vector
    tangent_x = -np.sin(end_rad)  # Derivative of x = r * cos(theta)
    tangent_y = np.cos(end_rad)  # Derivative of y = r * sin(theta)

    # Normalize the tangent vector
    tangent_magnitude = np.sqrt(tangent_x**2 + tangent_y**2)
    tangent_x /= tangent_magnitude
    tangent_y /= tangent_magnitude

    # Calculate the arrow's endpoint
    arrow_end_x = arrow_start_x + arrow_length * radius * tangent_x
    arrow_end_y = arrow_start_y + arrow_length * radius * tangent_y

    # Plot the arrow
    ax.arrow(
        arrow_start_x,
        arrow_start_y,
        arrow_end_x - arrow_start_x,
        arrow_end_y - arrow_start_y,
        head_width=radius * arrow_length / 2,
        head_length=radius * arrow_length,
        fc="k",
        ec="k",
        length_includes_head=True,
    )


def main(dirname, save):

    fontsize = 20

    fig, ax = plotmath.plot(
        functions=[],
        fn_labels=False,
        ticks=False,
        grid=False,
        xmin=-1.35,
        xmax=1.35,
        ymin=-1.3,
        ymax=1.3,
    )
    x, y = make_circle(radius=1)

    plt.plot(x, y, color=plotmath.COLORS.get("blue"), lw=2.5)

    angle = np.radians(37)
    x0 = np.cos(angle)
    y0 = np.sin(angle)

    plt.plot([0, x0], [0, y0], color="black", lw=2, alpha=0.7)

    ax.set_xlabel("$x$", fontsize=fontsize, loc="right")
    ax.set_ylabel("$y$", fontsize=fontsize, loc="top")

    x, y = make_circle_arc(radius=0.2, stop=angle)
    plt.plot(x, y, color="black", lw=1, alpha=0.7)

    # plt.text(
    #     x=0.5 * x0,
    #     y=0.5 * y0,
    #     s="$1$",
    #     fontsize=fontsize,
    #     ha="right",
    #     va="bottom",
    # )

    r = 0.4
    dx = dy = 0.05
    plt.text(
        x=r * 0.5 * (np.cos(angle) + 1),
        y=r * 0.5 * (np.sin(angle) + 0) - dy,
        s=f"${np.degrees(angle) :.0f} ^\\circ$",
        fontsize=fontsize,
        ha="center",
        va="center",
    )

    dx = dy = 0.1
    ax.plot(x0, y0, "ko", ms=8, alpha=0.7)

    plt.text(
        x=x0 + dx,
        y=y0,
        s=f"$P({x0 :.2f}, {y0 :.2f})$",
        fontsize=fontsize,
        ha="left",
        va="bottom",
    )

    ax.set_aspect("equal")

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
