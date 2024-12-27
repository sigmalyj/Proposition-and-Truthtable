from sympy.logic.boolalg import Or, And, Not
from sympy.abc import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
from sympy.logic.boolalg import to_cnf, to_dnf

def show_cnf_dnf(formula):
    dnf = to_dnf(formula, True)
    cnf = to_cnf(formula, True)

    print("主析取范式（DNF）:", dnf)
    print("主合取范式（CNF）:", cnf)
