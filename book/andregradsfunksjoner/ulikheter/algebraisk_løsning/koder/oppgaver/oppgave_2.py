import sys
import os

import sympy as sp

relative_path = "../utils/"
absolute_path = os.path.join(os.getcwd(), relative_path)
sys.path.append(absolute_path)

from make_sign_chart import make_sign_chart

if __name__ == "__main__":
    x = sp.symbols("x")
    f = -x**2 + 3*x + 4
    fname = "../../figurer/oppgaver/oppgave_2.svg"
    make_sign_chart(f, x, fn_name="f(x)", fname=fname)

    fname = "../../figurer/oppgaver/oppgave_2_uten_faktorer.svg"
    make_sign_chart(f, x, fn_name="f(x)", fname=fname, include_factors=False)
    

