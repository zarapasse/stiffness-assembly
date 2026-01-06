# Exact Global Stiffness Matrix Assembly (Direct Stiffness Method)

A minimal, exact-arithmetic implementation of **global stiffness matrix assembly**
using the **Direct Stiffness Method** 

This repository focuses **only on assembly**:
- given local element stiffness matrices
- and a connectivity (LM) matrix

it assembles the global stiffness matrix **exactly**, using rational arithmetic
(`fractions.Fraction`) instead of floating point.

The goal is clarity, correctness, and traceability — not performance.

---

## ✨ Features

- ✔️ Direct stiffness (scatter–add) assembly
- ✔️ Exact arithmetic using `Fraction` (no numerical roundoff)
- ✔️ Supports **mixed element sizes** (e.g. 4×4 and 3×3)
- ✔️ Bathe-style LM / connectivity matrix
- ✔️ Property checks:
  - symmetry
  - row and column equilibrium checks
- ✔️ Minimal dependencies (Python + NumPy only)

---

## 📁 Repository Structure

    ├── assembly.py        # Core assembly and diagnostic functions
    ├── example.py         # Worked example with exact fractions
    └── README.md

---

## 🔧 Assembly Philosophy

The assembly follows the classical rule:

\[
K_{IJ} \;{+}{=}\; k^{(e)}_{ab}
\quad\text{where}\quad
I = C_{e,a},\; J = C_{e,b}
\]

- `C` is the **connectivity (LM) matrix**
- `0` entries indicate constrained / inactive DOFs
- Local stiffness matrices may have different sizes
- Assembly is purely index bookkeeping — no geometry or physics here

---

## ▶️ Example Usage

Run the example script:

```bash
python example.py
```

This will:
	1.	Assemble the global stiffness matrix exactly
	2.	Print it as rational numbers
	3.	Check key structural properties

---

## 🧪 Diagnostics Included

The following checks are provided:
	•	Symmetry
Confirms correct assembly and energy consistency
	•	Row/column equilibrium checks
Useful for scalar systems and debugging,

Additional helper functions allow inspection of which elements
contribute to specific global rows or columns.