import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

plt.rc("text", usetex=True)

def make_sign_chart(f: sp.Expr, x: sp.symbols, fn_name: str = None, fname: str = None) -> None:
    # Extract the roots of the polynomial
    roots = sp.solve(f, x)
    roots = [float(root) for root in roots]
    roots = [int(root) if int(root) == root else root for root in roots]

    # Sort roots in ascending order just in case
    roots = sorted(roots)
    

    # Extract the linear factors of the polynomial
    factors = str(f.factor())
    factors = factors.split("*")
    new_factors = []
    for factor in factors:
        if factor[0] == "-" and factor[1] == "(":
            tmp = ["-1", factor[1:]]
            new_factors = new_factors + tmp
        else:
            new_factors.append(factor)
    
    factors = new_factors
        

    # Sort linear factors in ascending order. 
    sorted_factors = [0]*len(factors)
    if sp.solve(factors[0]) == []:
        sorted_factors[0] = factors[0]
        for factor in factors[1:]:
            root = sp.solve(factor, x)[0]
            root_idx = roots.index(float(root))
            sorted_factors[root_idx + 1] = factor
    else:
        for factor in factors:
            root = sp.solve(factor, x)[0]
            root_idx = roots.index(float(root))
            sorted_factors[root_idx] = factor

    factors = sorted_factors


    print(f"Creating sign chart for f(x) = {f} = {f.factor()}")

    # Create figure 
    fig, ax = plt.subplots()

    # Create x-axis and remove y-axis
    ax.spines["left"].set_color("none") # Remove the left y-axis
    ax.spines["right"].set_color("none") # Remove the right y-axis
    ax.spines["bottom"].set_position("zero") # Move the bottom x-axis to y=0
    ax.spines["top"].set_color("none") # Remove the top x-axis

    # Attach arrow to the right end of the x-axis
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)

    # Label the x-axis
    ax.set_xlabel(r"$x$", fontsize=16, loc="right")

    # Set tick marks to roots of the polynomial
    plt.xticks(
        ticks=[i for i in range(len(roots))],
        labels=[f"${root}$" for root in roots],
        fontsize=16
    )

    # Draw horisontal sign lines for each factor 
    dy = -1
    dx = 0.1
    for i, factor in enumerate(factors):
        plt.text(
            x=-1,
            y=(i+1)*dy,
            s=f"${factor}$",
            fontsize=16,
            ha="center",
            va="center",
        )
        if sp.solve(factor, x) == []:
            if sp.sympify(factor).evalf(subs={x: 0}) > 0:
                plt.axhline(y=(i+1)*dy, xmin=0.05, xmax=1, color="blue", linestyle="-", lw=2)
            else:
                plt.axhline(y=(i+1)*dy, xmin=0.05, xmax=1, color="red", linestyle="--", lw=2)
        
        elif sp.solve(factor, x) != []:
            root = sp.solve(factor, x)[0]
            root_idx = roots.index(float(root))
            plt.text(
                x=root_idx,
                y=(i+1)*dy,
                s=f"$0$",
                fontsize=20,
                ha="center",
                va="center",
            )
            ax.plot([-0.7, root_idx - dx], [(i+1)*dy, (i+1)*dy], color="red", linestyle="--", lw=2)
            ax.plot([root_idx + dx, len(roots)], [(i+1)*dy, (i+1)*dy], color="blue", linestyle="-", lw=2)


    # Label the function
    plt.text(
        x=-1,
        y=(len(factors)+1)*dy,
        s=f"${fn_name}$" if fn_name else f"$f(x)$",
        fontsize=16,
        ha="center",
        va="center",
    )
    
    # Draw sign lines for the complete function
    if sp.sympify(f).evalf(subs={x: float(roots[0]) - dx}) > 0:
        for root in roots:
            plt.text(
                x=roots.index(root),
                y=(len(factors)+1)*dy,
                s=f"${0}$",
                fontsize=20,
                ha="center",
                va="center",
            )

        for i, root in enumerate(roots):
            if i % 2 == 0:
                plt.axhline(y=(len(factors)+1)*dy, xmin=i/(len(roots)+1) + 0.05, xmax=(i+1)/(len(roots) + 1)- 0.05, color="blue", linestyle="-", lw=2)
            else:
                plt.axhline(y=(len(factors)+1)*dy, xmin=i/(len(roots)+1) + 0.05, xmax=(i+1)/(len(roots) + 1)- 0.05, color="red", linestyle="--", lw=2)

        if (len(roots) + 1) % 2 != 0:
            plt.axhline(y=(len(factors)+1)*dy, xmin=(len(roots))/(len(roots)+1) + 0.05, xmax=1, color="blue", linestyle="-", lw=2)
        else:
            plt.axhline(y=(len(factors)+1)*dy, xmin=(len(roots))/(len(roots)+1) + 0.05, xmax=1, color="red", linestyle="--", lw=2)

    else:
        for root in roots:
            plt.text(
                x=roots.index(root),
                y=(len(factors)+1)*dy,
                s=f"${0}$",
                fontsize=20,
                ha="center",
                va="center",
            )

        for i, root in enumerate(roots):
            if i % 2 == 0:
                plt.axhline(y=(len(factors)+1)*dy, xmin=i/(len(roots)+1) + 0.05, xmax=(i+1)/(len(roots) + 1)- 0.05, color="red", linestyle="--", lw=2)
            else:
                plt.axhline(y=(len(factors)+1)*dy, xmin=i/(len(roots)+1) + 0.05, xmax=(i+1)/(len(roots) + 1)- 0.05, color="blue", linestyle="-", lw=2)

        if (len(roots) + 1) % 2 == 0:
            plt.axhline(y=(len(factors)+1)*dy, xmin=(len(roots))/(len(roots)+1) + 0.05, xmax=1, color="blue", linestyle="-", lw=2)
        else:
            plt.axhline(y=(len(factors)+1)*dy, xmin=(len(roots))/(len(roots)+1) + 0.05, xmax=1 , color="red", linestyle="--", lw=2)

    # Draw vertical lines to separate regions
    offset_upper = 1 / (len(factors) + 2)
    offset_lower = (len(factors) + 1) / (len(factors) + 2)

    print(len(factors) + 2)

    offset = 0
    offset_dy = 0.2

    if sp.solve(factors[0]) == []:
        # factors.remove(factors[0])
        offset = 1

        for i, factor in enumerate(factors[1:]):
            plt.plot([i, i], [-0.4, (i + 1 + offset) * dy + offset_dy], color="black", linestyle="--", lw=1)
            plt.plot([i, i], [(i + 1 + offset) * dy - offset_dy, (len(factors) + 1) * dy + offset_dy], color="black", linestyle="--", lw=1)
    
    else:
        for i, factor in enumerate(factors):
            plt.plot([i, i], [-0.4, (i + 1 + offset) * dy + offset_dy], color="black", linestyle="--", lw=1)
            plt.plot([i, i], [(i + 1 + offset) * dy - offset_dy, (len(factors) + 1) * dy + offset_dy], color="black", linestyle="--", lw=1)


        # plt.axvline(x=i, ymin=(len(factors) - 1 - i)/(len(factors)), ymax=0.85, color="black", linestyle="--", lw=1)
        # plt.axvline(x=i, ymin=0.1, ymax=(len(factors) - i - offset_lower)/(len(factors) + 1), color="black", linestyle="--", lw=1)
        # plt.axvline(x=i, ymin=1/(len(roots)) * i, ymax=0.85, color="black", linestyle="--", lw=1)
        # plt.axvline(x=i, ymin=0.1, ymax=0.85, color="black", linestyle="--", lw=1)

    # Remove tick labels on y-axis 
    plt.yticks([])

    # plt.ylim(-4, 4)
    plt.xlim(-1, len(roots))

    plt.tight_layout()

    if fname:
        plt.savefig(fname)
    
    plt.show()


if __name__ == "__main__":
    x = sp.symbols("x")
    f = -1*(2*x**2 - 8*x - 10) * (x - 6)
    make_sign_chart(f)

