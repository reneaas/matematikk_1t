import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

plt.rc("text", usetex=True)

def make_sign_chart_theory(color: bool = True, degree: int = 2, include_factors: bool = True) -> None:
    if color:
        color_pos = "red"
        color_neg = "blue"
    else:
        color_pos = "black"
        color_neg = "black"

    roots = [f"$x_{i}$" for i in range(1, degree + 1)]
    factors = ["$a$"] + [f"$x - x_{i}$" for i in range(1, degree + 1)]

    # Create figure
    fig, ax = plt.subplots()

    # Create x-axis and remove y-axis
    ax.spines["left"].set_color("none")  # Remove the left y-axis
    ax.spines["right"].set_color("none")  # Remove the right y-axis
    ax.spines["bottom"].set_position("zero")  # Move the bottom x-axis to y=0
    ax.spines["top"].set_color("none")  # Remove the top x-axis

    # Attach arrow to the right end of the x-axis
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)

    # Label the x-axis
    ax.set_xlabel(r"$x$", fontsize=16, loc="right")

    # Set tick marks to roots of the polynomial
    plt.xticks(
        ticks=[i for i in range(len(roots))],
        labels=roots,
        fontsize=16,
    )


    # Draw sign lines for each factor if include_factors is True
    dy = -1
    dx = 0.1
    for i, factor in enumerate(factors):
