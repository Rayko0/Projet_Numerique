import sympy as sp

# Symboles
x, a = sp.symbols('x a', real=True)
k, K = sp.symbols('k K', real=True, positive=True)
R, A, B, T = sp.symbols('R A B T', complex=True)

# Fonctions d'onde dans chaque région
psi_I = sp.exp(sp.I * k * x) + R * sp.exp(-sp.I * k * x)
psi_II = A * sp.exp(sp.I * K * x) + B * sp.exp(-sp.I * K * x)
psi_III = T * sp.exp(sp.I * k * x)

# Conditions de raccordement à x = 0
cond1 = sp.Eq(psi_I.subs(x, 0), psi_II.subs(x, 0))  # continuité
cond2 = sp.Eq(sp.diff(psi_I, x).subs(x, 0), sp.diff(psi_II, x).subs(x, 0))  # dérivée

# Conditions de raccordement à x = a
cond3 = sp.Eq(psi_II.subs(x, a), psi_III.subs(x, a))  # continuité
cond4 = sp.Eq(sp.diff(psi_II, x).subs(x, a), sp.diff(psi_III, x).subs(x, a))  # dérivée

# Résolution
sol = sp.solve([cond1, cond2, cond3, cond4], (R, A, B, T), simplify=True)

# Transmission symbolique
T_expr = sp.simplify(sol[T])
P_T = sp.simplify(sp.Abs(T_expr)**2)

# Affichage
sp.pprint(P_T)
