import sys
import os

import sympy as sp

relative_path = "../utils/"
absolute_path = os.path.join(os.getcwd(), relative_path)
sys.path.append(absolute_path)

from make_sign_chart import make_sign_chart

if __name__ == "__main__":
    x = sp.symbols("x", real=True)
    f = x**2 - x - 6
    fname = "../../figurer/eksempler/eksempel_2.svg"
    make_sign_chart(f=f, x=x, fname=fname)
    

