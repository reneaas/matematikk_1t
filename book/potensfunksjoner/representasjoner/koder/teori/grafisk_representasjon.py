import numpy as np 
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)

def lag_potens_fn(a, b):
    def f(x):
        return a * x**b
    return f


f1 = lag_potens_fn(a=1, b=3)
f2 = lag_potens_fn(a=1, b=0.5)
f3 = lag_potens_fn(a=1, b=-1)

fig, ax = plt.subplots()
x = np.linspace(0, 6, 1024)

alpha = 0.7
ax.plot(x, f1(x), color="teal", lw=2, alpha=alpha)
ax.plot(x, f2(x), color="purple", lw=2, alpha=alpha)
ax.plot(x, f3(x), color="blue", lw=2, alpha=alpha)

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
    x=1.3+dx,
    y=f1(1.3), 
    s="$b>1$",
    fontsize=18,
    color="white",
    bbox=dict(facecolor="teal", alpha=alpha, edgecolor="black", boxstyle="round,pad=0.3"),
)

plt.text(
    x=0.3+dx,
    y=3, 
    s="$b<0$",
    fontsize=18,
    color="white",
    bbox=dict(facecolor="blue", alpha=alpha, edgecolor="black", boxstyle="round,pad=0.3"),
)


plt.text(
    x=2.3+dx,
    y=1.2, 
    s="$0<b<1$",
    fontsize=18,
    color="white",
    bbox=dict(facecolor="purple", alpha=alpha, edgecolor="black", boxstyle="round,pad=0.3"),
)


plt.plot([1, 1], [0, f1(1)], "--", color="black", alpha=0.5)
plt.plot([0, 1], [f1(1), f1(1)], "--", color="black", alpha=0.5)


plt.xticks([1], [f"$1$"],fontsize=18, ha="center")
plt.yticks([f1(1)], [f"$a$"], fontsize=18, va="center")
plt.xlim(-0.5, 4)
plt.ylim(-0.5, 4)
plt.tight_layout()
plt.savefig("../../figurer/teori/grafisk_representasjon.svg")
plt.show()