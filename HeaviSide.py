import sympy as sp
import  numpy as np
from sympy import Heaviside, nan
x=sp.symbols('x ', whole =True)

i,j,k=sp.symbols('i j k',integer = True, positive= True)
z=2
sp.plot(sp.Heaviside(-1)*x**2,title="heavySide", show=True)
