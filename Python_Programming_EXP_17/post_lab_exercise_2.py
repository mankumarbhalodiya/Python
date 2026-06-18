import sympy as sp
n, z, w = sp.symbols('n z w')
x_n = sp.cos(w * n)
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
print("Z-transform of x[n] = cos(w*n)u[n] is:")
sp.pprint(X_z.simplify())
