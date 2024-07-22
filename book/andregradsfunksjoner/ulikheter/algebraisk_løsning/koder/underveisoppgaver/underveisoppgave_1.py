import sys
import os

import sympy as sp

relative_path = "../utils/"
absolute_path = os.path.join(os.getcwd(), relative_path)
sys.path.append(absolute_path)

from make_sign_chart import make_sign_chart

if __name__ == "__main__":
    x = sp.symbols("x")
    f = x**2 - 4*x - 5
    fname = "../../figurer/underveisoppgaver/underveisoppgave_1.svg"
    make_sign_chart(f, x, fn_name="f(x)", fname=fname)
    

