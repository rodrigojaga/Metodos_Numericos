import sympy as sp
from sympy import *
import math

X, y, z = sp.symbols('X y z')

#Cambiar a como sea necesario
expr = math.e**sp.sqrt(X) * sp.sin(2*X) + sp.cos(X**3)

deriv1Expre = sp.diff(expr, X)
print(deriv1Expre)
deriv2Expre = sp.diff(deriv1Expre, X)
print(deriv2Expre)

