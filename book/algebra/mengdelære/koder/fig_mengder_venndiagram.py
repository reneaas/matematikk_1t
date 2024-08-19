import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plt.rc("text", usetex=True)
plt.rcParams.update(
    {"text.usetex": True, "text.latex.preamble": r"\usepackage{amsfonts}"}
)


def circle(x, y, r):
    angles = np.linspace(0, 2 * np.pi, 1024)
    x = x + r * np.cos(angles)
    y = y + r * np.sin(angles)
    return x, y


def donut(x, y, r, R):
    angles = np.linspace(0, 2 * np.pi, 1024)
    angles = angles[2:]
    x = x + r * np.cos(angles)
    y = y + r * np.sin(angles)
    x = np.append(x, (x[0],))
    y = np.append(y, (y[0],))
    x = np.append(x, R * np.cos(angles[::-1]))
    y = np.append(y, R * np.sin(angles[::-1]))
    return x, y


radius_N = 1
radius_Z = 2
radius_Q = 3
radius_R = 4

plt.figure(figsize=(7, 7))

# plt.fill(*circle(0, 0, radius_N), color="blue", alpha=0.3) # N
# plt.fill(*donut(0, 0, radius_N, radius_Z), color="red", alpha=0.3) # Z
# plt.fill(*donut(0, 0, radius_Z, radius_Q), color="teal", alpha=0.3) # Q
# plt.fill(*donut(0, 0, radius_Q, radius_R), color="purple", alpha=0.3) # R
plt.fill(*circle(0, 0, radius_R), color="purple", alpha=0.3)  # R
plt.fill(*circle(0, 0, radius_Q), color="white", alpha=1)  # Q
plt.fill(*circle(0, 0, radius_Q), color="teal", alpha=0.3)  # Q
plt.fill(*circle(0, 0, radius_Z), color="white", alpha=1)  # Z
plt.fill(*circle(0, 0, radius_Z), color="red", alpha=0.3)  # Z
plt.fill(*circle(0, 0, radius_N), color="white", alpha=1)  # N
plt.fill(*circle(0, 0, radius_N), color="blue", alpha=0.3)  # N
plt.axis("equal")

plt.axis("off")
plt.tight_layout()

plt.text(
    x=0,
    y=0,
    s=r"$\mathbb{N}$",
    fontsize=22,
    ha="center",
    va="bottom",
)
angles = [-3 * np.pi / 4, -np.pi / 2, -np.pi / 4]

naturlige_tall = [r"$1$", r"$2$", r"$3$"]
for angle, naturlig_tall in zip(angles, naturlige_tall):
    plt.text(
        x=0.5 * radius_N * np.cos(angle),
        y=0.5 * radius_N * np.sin(angle),
        s=naturlig_tall,
        fontsize=22,
        ha="center",
        va="center",
    )


plt.text(
    x=0,
    y=0.5 * (radius_N + radius_Z),
    s=r"$\mathbb{Z}$",
    fontsize=22,
    ha="center",
    va="center",
)

heltall = [r"$-2$", r"$-1$", r"$0$"]
for angle, heltall in zip(angles, heltall):
    plt.text(
        x=0.5 * (radius_N + radius_Z) * np.cos(angle),
        y=0.5 * (radius_N + radius_Z) * np.sin(angle),
        s=heltall,
        fontsize=22,
        ha="center",
        va="center",
    )


plt.text(
    x=0,
    y=0.5 * (radius_Z + radius_Q),
    s=r"$\mathbb{Q}$",
    fontsize=22,
    ha="center",
    va="center",
)

brøker = [r"$\frac{1}{2}$", r"$\frac{5}{2}$", r"$\frac{100}{3}$"]

for angle, brøk in zip(angles, brøker):
    plt.text(
        x=0.5 * (radius_Z + radius_Q) * np.cos(angle),
        y=0.5 * (radius_Z + radius_Q) * np.sin(angle),
        s=brøk,
        fontsize=22,
        ha="center",
        va="center",
    )


plt.text(
    x=0,
    y=0.5 * (radius_Q + radius_R),
    s=r"$\mathbb{R}$",
    fontsize=22,
    ha="center",
    va="center",
)

reelle_tall = [r"$\pi$", r"$\sqrt{2}$", r"$\frac{1 + \sqrt{5}}{2}$"]
for angle, reelt_tall in zip(angles, reelle_tall):
    plt.text(
        x=0.5 * (radius_Q + radius_R) * np.cos(angle),
        y=0.5 * (radius_Q + radius_R) * np.sin(angle),
        s=reelt_tall,
        fontsize=22,
        ha="center",
        va="center",
    )


try:
    plt.savefig("book/algebra/mengdelære/figurer/mengder_venndiagram.svg")
    plt.close()

except:
    plt.savefig("../figurer/mengder_venndiagram.svg")
    plt.show()
