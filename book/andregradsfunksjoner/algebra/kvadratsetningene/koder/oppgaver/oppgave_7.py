import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rc("text", usetex=True)

a = 1
b = 0.35

# plt.plot([0, a], [0, 0], 'teal')
# plt.plot([a, a], [0, a + b], "teal", linestyle="--")
# plt.plot([0, a + b], [a, a], 'teal', linestyle="--")
# plt.plot([0, 0], [0, a], 'teal')


# plt.plot([a, a + b], [0, 0], 'k')
# plt.plot([a + b, a + b], [0, a + b], "k")
# plt.plot([0, a + b], [a + b, a + b], 'k')
# plt.plot([0, 0], [0, a + b], 'k')


rect_1 = patches.Rectangle(
    xy=(0, 0),
    width=a - b,
    height=a - b,
    fill=True,
    edgecolor="black",
    facecolor="teal",
    alpha=0.2,
    lw=2,
)
rect_2 = patches.Rectangle(
    xy=(a - b, 0),
    width=b,
    height=a - b,
    fill=True,
    edgecolor="black",
    facecolor="gray",
    alpha=0.1,
    lw=2,
)
rect_3 = patches.Rectangle(
    xy=(0, a - b),
    width=a - b,
    height=b,
    fill=True,
    edgecolor="black",
    facecolor="gray",
    alpha=0.1,
    lw=2,
)

rect_4 = patches.Rectangle(
    xy=(a - b, a - b),
    width=b,
    height=b,
    fill=True,
    edgecolor="black",
    facecolor="gray",
    alpha=0.1,
    lw=2,
)

plt.gca().add_patch(rect_1)
plt.gca().add_patch(rect_2)
plt.gca().add_patch(rect_3)
plt.gca().add_patch(rect_4)

plt.text(
    x=-0.3,
    y=0.5 * a,
    s="$a$",
    fontsize=20,
    color="black",
    ha="center",
    va="center",
)

plt.annotate(
    "",
    xy=(-0.2, 0),
    xycoords="data",
    xytext=(-0.2, a),
    textcoords="data",
    arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="black"),
)


plt.annotate(
    "",
    xy=(-0.1, a - b),
    xycoords="data",
    xytext=(-0.1, a),
    textcoords="data",
    arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="black"),
)

plt.text(
    x=-0.05,
    y=a - 0.5 * b,
    s="$b$",
    fontsize=20,
    color="black",
    ha="center",
    va="center",
)


plt.text(
    x=0.5 * a,
    y=-0.1,
    s="$a$",
    fontsize=20,
    color="black",
    ha="center",
    va="center",
)

plt.annotate(
    "",
    xy=(0, -0.05),
    xycoords="data",
    xytext=(a, -0.05),
    textcoords="data",
    arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="black"),
)


plt.text(
    x=a - 0.5 * b,
    y=a + 0.1,
    s="$b$",
    fontsize=20,
    color="black",
    ha="center",
    va="center",
)

plt.annotate(
    "",
    xy=(a - b, a + 0.05),
    xycoords="data",
    xytext=(a, a + 0.05),
    textcoords="data",
    arrowprops=dict(arrowstyle="|-|,widthA=0.5,widthB=0.5", color="black"),
)


plt.axis("equal")
plt.axis("off")

plt.savefig("../../figurer/oppgaver/oppgave_7.svg")

plt.show()