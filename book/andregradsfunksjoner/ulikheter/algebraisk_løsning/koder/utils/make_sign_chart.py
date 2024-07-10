import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

plt.rc("text", usetex=True)

def get_factors(polynomial: sp.Expr, x: sp.symbols) -> list[dict]:
    polynomial = sp.expand(polynomial) # expand first in case multiple factors of the same kind are present
    factor_list = sp.factor_list(polynomial)
    leading_coeff = factor_list[0]
    if not leading_coeff == 1:
        linear_factors = [{"expression": leading_coeff, "exponent": 1, "root": -np.inf}]
    else:
        linear_factors = []

    
    for (linear_factor, exponent) in factor_list[1]:            
        exponent = int(exponent)
        root = sp.solve(linear_factor, x)
        if root == []:
            linear_factors.append(
                {
                    "expression": linear_factor,
                    "exponent": exponent,
                    "root": -np.inf
                }
            )
        else:
            linear_factors.append(
                {
                    "expression": linear_factor,
                    "exponent": exponent,
                    "root": sp.solve(linear_factor, x)[0]    
                }
            )
    
    return linear_factors



def sort_factors(factors: list[dict]) -> list[dict]:
    factors = sorted(factors, key=lambda x: x.get("root"))
    return factors


def make_sign_chart(f: sp.Expr, x: sp.symbols, fn_name: str = None, fname: str = None, color: bool = True) -> None:

    if color:
        color_pos = "red"
        color_neg = "blue"
    else:
        color_pos = color_neg = "black"

    factors = get_factors(polynomial=f, x=x)         # Compute the linear factors of the polynomial
    factors = sort_factors(factors=factors)     # Sort linear factors in ascending order.

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
    roots = [factor.get("root") for factor in factors if factor.get("root") != -np.inf]
    plt.xticks(
        ticks=[i for i in range(len(roots))],
        labels=[f"${root}$" for root in roots],
        fontsize=16,
    )

    # Draw horisontal sign lines for each factor 
    dy = -1
    dx = 0.1
    for i, factor in enumerate(factors):
        expression = str(factor.get("expression"))
        exponent = factor.get("exponent")
        if "**" in str(expression):
            expression = expression.replace("**", "^")
        
        if exponent > 1:
            s = f"$({expression})^{exponent}$"
        else:
            s = f"${expression}$"


        plt.text(
            x=-1,
            y=(i+1)*dy,
            s=s,
            fontsize=16,
            ha="center",
            va="center",
        )
        if factor.get("root") == -np.inf:
            if sp.sympify(factor.get("expression")).evalf(subs={x: 0}) > 0:
                # plt.axhline(y=(i+1)*dy, xmin=0.05, xmax=1, color="blue", linestyle="-", lw=2)
                ax.plot([-0.7, len(roots)], [(i+1)*dy, (i+1)*dy], color=color_pos, linestyle="-", lw=2)
            else:
                # plt.axhline(y=(i+1)*dy, xmin=0.05, xmax=1, color="red", linestyle="--", lw=2)
                ax.plot([-0.7, len(roots)], [(i+1)*dy, (i+1)*dy], color=color_neg, linestyle="--", lw=2)
        
        elif factor.get("exponent") % 2 == 0:
            root = factor.get("root")
            root_idx = roots.index(float(root))
            ax.plot([-0.7, root_idx - dx], [(i+1)*dy, (i+1)*dy], color=color_pos, linestyle="-", lw=2)
            ax.plot([root_idx + dx, len(roots)], [(i+1)*dy, (i+1)*dy], color=color_pos, linestyle="-", lw=2)

            root_idx = roots.index(float(root))
            plt.text(
                x=root_idx,
                y=(i+1)*dy,
                s=f"$0$",
                fontsize=20,
                ha="center",
                va="center",
            )

        else:
            root = factor.get("root")
            root_idx = roots.index(float(root))
            ax.plot([-0.7, root_idx - dx], [(i+1)*dy, (i+1)*dy], color=color_neg, linestyle="--", lw=2)
            ax.plot([root_idx + dx, len(roots)], [(i+1)*dy, (i+1)*dy], color=color_pos, linestyle="-", lw=2)


            plt.text(
                x=root_idx,
                y=(i+1)*dy,
                s=f"$0$",
                fontsize=20,
                ha="center",
                va="center",
            )


    # Label the function
    plt.text(
        x=-1,
        y=(len(factors)+1)*dy,
        s=f"${fn_name}$" if fn_name else f"$f(x)$",
        fontsize=16,
        ha="center",
        va="center",
    )


    for i, root in enumerate(roots):

        plt.text(
            x=i,
            y=(len(factors)+1)*dy,
            s=f"${0}$",
            fontsize=20,
            ha="center",
            va="center",
        )
        
        x0 = root - dx
        y0 = sp.sympify(f).evalf(subs={x: x0})
        print(f" {x0 = } ; {y0 = }")

        if y0 > 0:
            plt.axhline(y=(len(factors)+1)*dy, xmin=i/(len(roots)+1) + 0.05, xmax=(i+1)/(len(roots) + 1)- 0.05, color=color_pos, linestyle="-", lw=2)
        else:
            plt.axhline(y=(len(factors)+1)*dy, xmin=i/(len(roots)+1) + 0.05, xmax=(i+1)/(len(roots) + 1)- 0.05, color=color_neg, linestyle="--", lw=2)

    x0 = roots[-1] + dx
    y0 = sp.sympify(f).evalf(subs={x: x0})
    if y0 > 0:
        plt.axhline(y=(len(factors)+1)*dy, xmin=(len(roots))/(len(roots)+1) + 0.05, xmax=1, color=color_pos, linestyle="-", lw=2)
    else:
        plt.axhline(y=(len(factors)+1)*dy, xmin=(len(roots))/(len(roots)+1) + 0.05, xmax=1, color=color_neg, linestyle="--", lw=2)



    # Draw vertical lines to separate regions
    offset_upper = 1 / (len(factors) + 2)
    offset_lower = (len(factors) + 1) / (len(factors) + 2)

    offset_dy = 0.2


    n_factors_without_roots = len([factor for factor in factors if factor.get("root") == -np.inf])

    print(f"{n_factors_without_roots = }")

    offset = 1
    for i, root in enumerate(roots):
        plt.plot([i, i], [-0.4, (i + n_factors_without_roots + offset) * dy + offset_dy], color="black", linestyle="--", lw=1)
        plt.plot([i, i], [(i + n_factors_without_roots + offset) * dy - offset_dy, (len(factors) + 1) * dy + offset_dy], color="black", linestyle="--", lw=1)


    # Remove tick labels on y-axis 
    plt.yticks([])

    # plt.ylim(-4, 4)
    plt.xlim(-1, len(roots))

    plt.tight_layout()

    if fname:
        plt.savefig(fname)
    
    plt.show()


if __name__ == "__main__":
    x = sp.symbols("x", real=True)
    # f = -(2*x**2 - 8*x - 10) 
    # f = -(x**2 - 4*x - 5) * (x**2 + 1)
    # f = x**2 + 4*x + 4
    f = -2 * (x**2 - 1)**4 * (x - 3) * (x - 1)
    make_sign_chart(f, x, color=True)