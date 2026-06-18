import sympy as sp
n, z = sp.symbols('n z')
x_n = (1/sp.Integer(2))**n
X_z = sp.summation(x_n*z**(-n), (n, 0, sp.oo))
print("Z-transform of x[n] = (1/2)^n u[n] is:")
sp.pprint(X_z.simplify())