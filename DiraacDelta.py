import sympy as sp
from sympy import DiracDelta, diff, pi

x=sp.symbols('x ', whole =True)

i,j,k=sp.symbols('i j k',integer = True, positive= True)
z=2
sp.plot(sp.DiracDelta(0)*x**2,title="heavySide", show=True)
