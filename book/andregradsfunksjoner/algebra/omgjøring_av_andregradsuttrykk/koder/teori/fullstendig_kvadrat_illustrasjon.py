import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rc("text", usetex=True)

a = 2
b = 1


# Kvadrat: (a + b)^2

rect_a = patches.Rectangle(
    xy=(0, 0), width=a, height=a, fill=True, color="teal", alpha=0.2
)

plt.text(
    x=0.5 * (a + b),
    y=-0.3,
    s=r"$a + b$",
    fontsize=22,
    ha="center",
    va="center",
)

plt.text(
    x=-0.3,
    y=0.5 * (a + b),
    s=r"$a + b$",
    fontsize=22,
    ha="center",
    va="center",
    rotation=90,
)

plt.text(
    x=0.5 * a,
    y=0.5 * a,
    s=r"$a^2$",
    fontsize=22,
    ha="center",
    va="center",
)


plt.gca().add_patch(rect_a)

rect_b = patches.Rectangle(
    xy=(a, a), width=b, height=b, fill=True, color="red", alpha=0.2
)
plt.gca().add_patch(rect_b)

plt.text(
    x=a + 0.5 * b,
    y=a + 0.5 * b,
    s=r"$b^2$",
    fontsize=22,
    ha="center",
    va="center",
)

rect_ab = patches.Rectangle(
    xy=(a, 0), width=b, height=a, fill=True, color="blue", alpha=0.2
)
plt.gca().add_patch(rect_ab)

plt.text(
    x=a + 0.5 * b,
    y=0.5 * a,
    s=r"$ab$",
    fontsize=22,
    ha="center",
    va="center",
)

rect_ab2 = patches.Rectangle(
    xy=(0, a), width=a, height=b, fill=True, color="blue", alpha=0.2
)
plt.gca().add_patch(rect_ab2)

plt.text(
    x=0.5 * a,
    y=a + 0.5 * b,
    s=r"$ab$",
    fontsize=22,
    ha="center",
    va="center",
)

plt.text(
    x=a + b + 0.5,
    y=0.5 * (a + b),
    s=r"$=$",
    fontsize=30,
    ha="center",
    va="center",
)

plt.text(
    x=a + b + 1.3,
    y=0.5 * (a + b),
    s=r"$(a+b)^2$",
    fontsize=22,
    ha="center",
    va="center",
)


plt.axis("off")
plt.axis("equal")
plt.xlim(-1, a + b + 1.8)
plt.ylim(-1, a + b + 0.5)
plt.tight_layout()
plt.savefig("../../figurer/teori/fullstendig_kvadrat.svg")
