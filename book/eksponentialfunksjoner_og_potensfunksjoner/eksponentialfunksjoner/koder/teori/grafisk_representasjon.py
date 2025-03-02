import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)


def lag_eksponential_fn(a, b):
    def f(x):
        return a * b**x

    return f


f1 = lag_eksponential_fn(a=1, b=3)
f2 = lag_eksponential_fn(a=1, b=0.5)

fig, ax = plt.subplots()
x = np.linspace(-6, 6, 1024)

alpha = 0.7
ax.plot(x, f1(x), color="teal", lw=2, alpha=alpha)
ax.plot(x, f2(x), color="purple", lw=2, alpha=alpha)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

plt.xlabel("$x$", fontsize=18, loc="right")
plt.ylabel("$y$", fontsize=18, loc="top", rotation="horizontal")


dx = 0.3
plt.text(
    x=1 + dx,
    y=f1(1) - 0.2,
    s="$b>1$",
    fontsize=18,
    color="white",
    bbox=dict(
        facecolor="teal", alpha=alpha, edgecolor="black", boxstyle="round,pad=0.3"
    ),
)

plt.text(
    x=1.5 + dx,
    y=0.8,
    s="$0<b<1$",
    fontsize=18,
    color="white",
    bbox=dict(
        facecolor="purple", alpha=alpha, edgecolor="black", boxstyle="round,pad=0.3"
    ),
)


plt.annotate(
    text="$y = a$",
    xy=(0, 1),
    xytext=(-1, 3),
    fontsize=16,
    arrowprops=dict(
        arrowstyle="->", lw=2, color="black", alpha=0.7, connectionstyle="arc3,rad=-0.2"
    ),
    horizontalalignment="center",
    verticalalignment="center",
)


plt.xlim(-2, 3)
plt.ylim(-1, 4)
plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig("../../figurer/teori/grafisk_representasjon.svg")
plt.show()
