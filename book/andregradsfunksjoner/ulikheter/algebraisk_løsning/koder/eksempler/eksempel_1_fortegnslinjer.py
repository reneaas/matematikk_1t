import sys
import os

import sympy as sp

relative_path = "../utils/"
absolute_path = os.path.join(os.getcwd(), relative_path)
sys.path.append(absolute_path)

from make_sign_chart import make_sign_chart

if __name__ == "__main__":
    x = sp.symbols("x", real=True)
    f = x**2 - 4*x
    g = x - 4
    fname_f = "../../figurer/eksempler/eksempel_1_fortegnslinje_f.svg"
    fname_g = "../../figurer/eksempler/eksempel_1_fortegnslinje_g.svg"
    make_sign_chart(f=f, x=x, fname=fname_f, include_factors=False, fn_name="f(x)")
    make_sign_chart(f=g, x=x, fname=fname_g, include_factors=False, fn_name="g(x)")
    

