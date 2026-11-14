# Powe Iteration Eigen Value Solver From Scratch
![Python](https://shields.io)
![Dependencies](https://shields.io)
![Topic](https://shields.io)

A zero-dependency, pure-Python implementation of the **Power Iteration Algorithm** engineered from first principles to compute the dominant eigenvalue (\(\lambda_1\)) of any square \(n \times n\) matrix—without relying on `numpy`, `scipy`, or external linear algebra libraries.

---

## Overview & Motivation

While \(2 \times 2\) and \(3 \times 3\) matrices can be solved on paper using the characteristic polynomial \(\det(A - \lambda I) = 0\), the **Abel–Ruffini theorem** proves that no general closed-form algebraic formula exists for polynomial equations of degree \(5\) or higher. 

To solve real-world systems in scientific computing, physics simulations, and machine learning (such as Google's PageRank and Principal Component Analysis), CPUs rely on **iterative numerical algorithms**. This repository translates the core eigenvalue equation \(Av = \lambda v\) into a self-stopping, crash-proof Python solver using only native lists and loops.

---

## Key Engineering Features

- **100% Pure Python Core:** Built entirely with native Python data structures (`script1.py`) with zero third-party packages.
- **Dynamic \(n \times n\) Matrix Support:** Clean row-by-row terminal parsing capable of solving matrices of arbitrary dimensions.
- **In-Loop Vector Normalization:** Scales the eigenvector by its maximum component on every iteration to prevent floating-point overflow (`inf`) on large matrices.
- **SciPy-Grade Relative Tolerance:** Automatically detects convergence when the relative change between consecutive estimates drops below `1e-8`:
  \[\frac{\vert{}\lambda_k - \lambda_{k-1}\vert{}}{\vert{}\lambda_k\vert{}} \le 10^{-8}\]
- **Edge-Case & Fault Protection:**
  - **Non-Converging Matrices:** Enforces an iteration cap to safely catch matrices with tied eigenvalues (e.g., \(\begin{bmatrix} 0 & 3 \\ 2 & 0 \end{bmatrix}\)) or pure rotation matrices without hanging in an infinite loop.
  - **Zero-Matrix Guard:** Handles all-zero matrices gracefully without triggering a `ZeroDivisionError`.

---

## Accuracy Benchmark (\(5 \times 5\) Dense Matrix)

Tested against a dense \(5 \times 5\) matrix that cannot be solved via closed-form polynomial formulas by hand:

\[A = \begin{bmatrix} 12 & 14 & 43 & 12 & 54 \\ 56 & 76 & 34 & 23 & 78 \\ 27 & 47 & 0 & 23 & 57 \\ 12 & 43 & 67 & 87 & 34 \\ 21 & 78 & 68 & 24 & 93 \end{bmatrix}\]

| Implementation | Dominant Eigenvalue (\(\lambda_1\)) | Absolute Error vs. NumPy |
| :--- | :--- | :--- |
| **NumPy (`np.linalg.eig`)** | `231.4141425067547` | Reference Value |
| **This Solver (`script1.py`)** | `231.4141421245695` | **`3.82 × 10⁻⁷`** |

---

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com
cd Power-Iteration-Eigenvalue-Solver
```
*(Note: Update the repository slug in the URL above if you chose a different repository name on GitHub.)*

### 2. Run the Solver
```bash
python script1.py
```

### 3. Sample Terminal Execution
```text
Enter the order of matrix nxn: 2
Enter 1 row: 1 4
Enter 2 row: 2 6
7.274917216804464
```

---

## How the Algorithm Works

1. **Initialization:** Starts with an initial guess vector $v_0 = [1, 1, \dots, 1]^T$.
2. **Matrix-Vector Product:** Computes $v_{k+1} = A v_k$ via nested row-column dot products.
3. **Eigenvalue Extraction:** Captures the dominant scaling factor from the largest component prior to normalization.
4. **Vector Normalization:** Divides all entries in $v_{k+1}$ by its maximum component so values remain bounded.
5. **Convergence Check:** Repeats until the relative error satisfies $\le 10^{-8}$ or triggers a safe exit if the matrix fails to converge.

---

## Known Mathematical Limitations

- **Dominant Eigenvalue Only:** Power Iteration isolates the eigenvalue with the largest absolute magnitude ($|\lambda_1|$). Computing the full spectrum of eigenvalues requires deflation or QR decomposition.
- **Unique Dominant Eigenvalue Requirement:** Matrices with complex conjugate eigenvalues (such as rotation matrices) or multiple eigenvalues sharing the exact same largest magnitude will oscillate indefinitely and trigger the solver's non-convergence guard.

---

## Author

**Dibyajit Chakraborty** — [GitHub Profile](https://github.com/Dibyajit-31)
