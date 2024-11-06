import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rc("text", usetex=True)

a = 1
b = 0.3

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
    width=a,
    height=a,
    fill=True,
    edgecolor="teal",
    facecolor="teal",
    alpha=0.2,
    lw=2,
)
rect_2 = patches.Rectangle(
    xy=(a, 0),
    width=b,
    height=a,
    fill=True,
    edgecolor="black",
    facecolor="blue",
    alpha=0.2,
    lw=2,
)
rect_3 = patches.Rectangle(
    xy=(0, a),
    width=a,
    height=b,
    fill=True,
    edgecolor="black",
    facecolor="blue",
    alpha=0.2,
    lw=2,
)
rect_4 = patches.Rectangle(
    xy=(a, a),
    width=b,
    height=b,
    fill=True,
    edgecolor="red",
    facecolor="red",
    alpha=0.2,
    lw=2,
)
plt.gca().add_patch(rect_1)
plt.gca().add_patch(rect_2)
plt.gca().add_patch(rect_3)
plt.gca().add_patch(rect_4)

plt.text(
    x=0.5 * a,
    y=-0.1,
    s="$a$",
    fontsize=20,
    color="teal",
)

plt.text(
    x=-0.1,
    y=0.5 * a,
    s="$a$",
    fontsize=20,
    color="teal",
)


plt.text(
    x=a + 0.5 * b,
    y=-0.1,
    s="$b$",
    fontsize=20,
    color="blue",
)

plt.text(
    x=-0.1,
    y=a + 0.5 * b,
    s="$b$",
    fontsize=20,
    color="blue",
)


plt.axis("equal")
plt.axis("off")

plt.savefig("../../figurer/oppgaver/oppgave_4.svg")
