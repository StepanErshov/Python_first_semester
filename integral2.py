from sympy import *
import math
x = symbols('x')
f = integrate(1//(x**3 * (sqrt(log(E, x)))), (x, 0, 2))
print(f)