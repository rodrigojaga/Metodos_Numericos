import sympy as sp
from sympy import *
import math

X, y, z = sp.symbols('X y z')

#Cambiar a como sea necesario
expr = -X**2 + 18*X + 2.5

deriv = sp.diff(expr, X)
print(deriv)

