from global_stiffness import assemble_K_global, check_stiffness_properties
from fractions import Fraction
import numpy as np



# ---------- data ----------
K1 = np.array([
    [Fraction(41,60),  Fraction(-7,120), Fraction(-41,120), Fraction(-17,60)],
    [Fraction(-7,120), Fraction(41,60),  Fraction(-17,60),   Fraction(-41,120)],
    [Fraction(-41,120),Fraction(-17,60),  Fraction(41,60),   Fraction(-7,120)],
    [Fraction(-17,60),  Fraction(-41,120),Fraction(-7,120), Fraction(41,60)],
], dtype=object)

K2 = np.array([
    [Fraction(29,30),  Fraction(17,60),  Fraction(-29,60), Fraction(-23,30)],
    [Fraction(17,60),  Fraction(29,30),  Fraction(-23,30), Fraction(-29,60)],
    [Fraction(-29,60), Fraction(-23,30), Fraction(29,30),  Fraction(17,60)],
    [Fraction(-23,30), Fraction(-29,60), Fraction(17,60),  Fraction(29,30)],
], dtype=object)

K3 = np.array([
    [Fraction(1,2),  Fraction(-1,2), Fraction(0)],
    [Fraction(-1,2), Fraction(1),    Fraction(-1,2)],
    [Fraction(0),    Fraction(-1,2), Fraction(1,2)],
], dtype=object)

K4 = np.array([
    [Fraction(5,4), Fraction(-1), Fraction(-1,4)],
    [Fraction(-1),  Fraction(1),  Fraction(0)],
    [Fraction(-1,4),Fraction(0),  Fraction(1,4)],
], dtype=object)

K5 = np.array([
    [Fraction(29,32), Fraction(-9,16), Fraction(-11,32)],
    [Fraction(-9,16), Fraction(5,8),   Fraction(-1,16)],
    [Fraction(-11,32),Fraction(-1,16), Fraction(13,32)],
], dtype=object)

K6 = np.array([
    [Fraction(5,4),  Fraction(-5,4), Fraction(0)],
    [Fraction(-5,4), Fraction(29,20),Fraction(-1,5)],
    [Fraction(0),    Fraction(-1,5), Fraction(1,5)],
], dtype=object)

K_locals = [K1, K2, K3, K4, K5, K6]

C = np.array([
    [3, 4, 8, 7],
    [1, 2, 4, 3],
    [2, 4, 5, 0],
    [4, 5, 8, 0],
    [5, 6, 8, 0],
    [6, 9, 8, 0],
], dtype=int)

# ---------- main ----------
if __name__ == "__main__":
    for K in K_locals:
        check_stiffness_properties(K)

    K_global = assemble_K_global(K_locals, C)

    print("K_global (exact fractions):\n")
    for row in K_global:
        print([str(x) for x in row])
        
    check_stiffness_properties(K_global)