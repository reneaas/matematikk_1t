import matplotlib.pyplot as plt

# Define figure
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis("off")  # Hide the axes for a cleaner look

# Node text
nodes = [
    (r"$ax^2 + bx + c$", (0, 1)),  # Position (x, y)
    (r"$a(x - x_0)^2 + y_0$", (1, 0)),
    (r"$a(x - x_1)(x - x_2)$", (0, -1)),
]

# Draw boxes with text
for text, pos in nodes:
    ax.text(
        pos[0],
        pos[1],
        text,
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightblue"),
    )

# Arrow and label positions
connections = [
    ((0, 1), (1, 0), "Fullstendig kvadraters metode"),  # (start, end, label)
    ((1, 0), (0, -1), "Konjugatsetningen"),
    ((0, -1), (0, 1), "Utvid"),
]

# Draw arrows with annotations
for start, end, label in connections:
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops=dict(arrowstyle="->", color="black", lw=1.5),
    )
    # Position label at midpoint of each arrow
    label_pos = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
    ax.text(
        label_pos[0], label_pos[1], label, fontsize=10, color="darkgreen", ha="center"
    )

# Show plot
plt.title("Cyclical Diagram of Quadratic Transformations", fontsize=14)
plt.show()
