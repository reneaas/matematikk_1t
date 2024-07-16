import sys
import os

import sympy as sp

relative_path = "../utils/"
absolute_path = os.path.join(os.getcwd(), relative_path)
sys.path.append(absolute_path)

from make_sign_chart import make_sign_chart

if __name__ == "__main__":
    x = sp.symbols("x")
    f = -(x - 2) * (x + 2)
    fname = "../../figurer/oppgaver/oppgave_3_uten_faktorer.svg"
    make_sign_chart(f, x, fn_name="g(x)", fname=fname, include_factors=False)

    fname = "../../figurer/oppgaver/oppgave_3.svg"
    make_sign_chart(f, x, fn_name="g(x)", fname=fname, include_factors=True)
    

