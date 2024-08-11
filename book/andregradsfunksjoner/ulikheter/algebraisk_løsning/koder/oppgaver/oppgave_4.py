import sys
import os

import sympy as sp

relative_path = "../utils/"
absolute_path = os.path.join(os.getcwd(), relative_path)
sys.path.append(absolute_path)

from make_sign_chart import make_sign_chart

if __name__ == "__main__":
    x = sp.symbols("r")
    f = 1 - 4 * x**2
    fname = "../../figurer/oppgaver/oppgave_4_uten_faktorer.svg"
    make_sign_chart(f, x, fname=fname, include_factors=False, fn_name="D(r)")

    fname = "../../figurer/oppgaver/oppgave_4.svg"
    make_sign_chart(f, x, fname=fname, include_factors=True, fn_name="D(r)")
