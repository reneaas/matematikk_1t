import sympy
import numpy as np


a = np.random.randint(-5, 6)
b = np.random.randint(-5, 6)
c = np.random.randint(-5, 6)

a = sympy.sympify(a)
b = sympy.sympify(b)
c = sympy.sympify(c)

x = sympy.symbols("x")

p = (x - a) * (x - b) * (x - c)
print("Faktorisert form:")
print(f"{p = } \n")


p = p.expand()
print("Utvidet form:")
print(f"{p = } \n")


d = np.random.randint(-5, 6)
d = sympy.sympify(d)
q = x - d
print("Polynomdivisjon:")

k, r = sympy.div(p, q)
if r == 0:
    print(f"({p}) : ({q}) = {k}")
else:
    print(f"({p}) : ({q}) = {k} + {r} / ({q})")
