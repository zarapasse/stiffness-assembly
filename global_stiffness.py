import numpy as np
from fractions import Fraction

def assemble_K_global(K_locals, C, n_eq=None):
    """
    Assemble global stiffness matrix from element stiffness matrices and connectivity matrix.
    """
    C = np.asarray(C, dtype=int)

    if n_eq is None:
        n_eq = int(C.max())

    K_global = np.full((n_eq, n_eq), Fraction(0), dtype=object)

    for e, k_e in enumerate(K_locals):
        lm = C[e]
        active = lm != 0
        lm_active = lm[active] - 1

        m = lm_active.size
        if k_e.shape != (m, m):
            raise ValueError(
                f"Element {e}: expected {(m,m)}, got {k_e.shape}"
            )

        for a in range(m):
            I = lm_active[a]
            for b in range(m):
                J = lm_active[b]
                K_global[I, J] += k_e[a, b]

    return K_global

def is_symmetric(K):
    n = K.shape[0]
    for i in range(n):
        for j in range(i + 1, n):
            if K[i, j] != K[j, i]:
                return False, (i, j, K[i, j], K[j, i])
    return True, None

def rows_sum_to_zero(K):
    n = K.shape[0]
    bad_rows = []

    for i in range(n):
        row_sum = sum(K[i, j] for j in range(n))
        if row_sum != 0:
            bad_rows.append((i, row_sum))

    return len(bad_rows) == 0, bad_rows

def columns_sum_to_zero(K):
    n = K.shape[0]
    bad_cols = []

    for j in range(n):
        col_sum = sum(K[i, j] for i in range(n))
        if col_sum != 0:
            bad_cols.append((j, col_sum))

    return len(bad_cols) == 0, bad_cols

def check_stiffness_properties(K):
    sym_ok, sym_info = is_symmetric(K)
    row_ok, bad_rows = rows_sum_to_zero(K)
    col_ok, bad_cols = columns_sum_to_zero(K)

    print("\n--- Stiffness matrix checks ---")

    print(f"Symmetric: {sym_ok}")
    if not sym_ok:
        i, j, kij, kji = sym_info
        print(f"  Mismatch at ({i},{j}): K_ij={kij}, K_ji={kji}")

    print(f"Rows sum to zero: {row_ok}")
    if not row_ok:
        for i, s in bad_rows:
            print(f"  Row {i} sum = {s}")

    print(f"Columns sum to zero: {col_ok}")
    if not col_ok:
        for j, s in bad_cols:
            print(f"  Column {j} sum = {s}")
