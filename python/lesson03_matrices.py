"""
    Linear Algebra Mastary
    ---------------------
    Lesson 3: Matrices
"""
# Import 
import numpy as np

# Define a matrix
A =  np.array([[1, 2], [3, 4]])

B = np.array([[2, 1, 4], [3, 0, 5]])

# print
print("=== Matrices ===")
print(f"A = \n{A}")
print(f"Shape of A: {A.shape}")
print(f"B = \n{B}")
print(f"Shape of B: {B.shape}")
print(f"Entry b[1][2]: {B[1][2]}")

# Matrix vector multiplication
x = np.array([2, 1])

# Method one, Using numpy operator
Ax = A @ x

# Method two, Column combination manual
first_col = A[:,0]
second_col = A[:,1]

Ax_manual = first_col * x[0] + second_col * x[1]

print("\n=== Matrix-vector multiplication ===\n")
print(f"A = \n{A}")
print(f"x = {x}")
print(f"Ax (NumPy): {Ax}")
print(f"Ax (Manual): {Ax_manual}")
print(f"Both methods match {np.array_equal(Ax, Ax_manual)}")

# Matrix multiplication

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[2, 0],
              [1, 3]])

# Method one (NumPy)
AB = A @ B

# Method two (Manual)
col1_B = B[:,0]
col2_B = B[:,1]

AB_col1 = A @ col1_B
AB_col2 = A @ col2_B

AB_manual = np.column_stack([AB_col1, AB_col2])

print("\n=== Matrix Multiplication ===")
print(f"A =\n{A}")
print(f"B =\n{B}")
print(f"AB (NumPy) =\n{AB}")
print(f"AB (manual) =\n{AB_manual}")
print(f"Both methods match: {np.array_equal(AB, AB_manual)}")

# Verify AB ≠ BA
BA = B @ A
print(f"\nAB =\n{AB}")
print(f"BA =\n{BA}")
print(f"AB == BA: {np.array_equal(AB, BA)}")


# Machine learning connection - prediction of Ax
# Feature matrix X with 3 data points and two features
X = np.array([[1, 2], [3, 4], [5, 6]])

# Weight vector
w = np.array([0.5,  1.5])

# Predictions
predictions = X @ w

print("\n=== Machine learning connection ===\n")
print(f"Feature matrix: \n{X}")
print(f"Weight vector = {w}")
print(f"Predictions = {predictions}")
print("\nBreak it down: ")
for i, row in enumerate(X):
    pred = np.dot(row, w)
    print(f"Data point {i + 1} = {row} . {w} = {pred}")

# Transpose
A = np.array([[2, 1, 4], [3, 0,  5]])

A_T = A.T
print("\n=== Transpose ===\n")
print(f"A = \n{A}")
print(f"Shape of A = {A.shape}")
print(f"A transpose = \n{A_T}")
print(f"Shape of A transpose = {A_T.shape}")

# Key properties (AB)^T = (B^T)(A^T)
B = np.array([[1, 2], [3, 4], [5, 6]])

AB = A @ B

print(f"(AB)^T = \n{AB.T}")
print(f"B^T A^T = \n{B.T @ A.T}")
print(f"(AB)^T = B^T A^T = {np.array_equal(AB.T, B.T @ A.T)}")

# Symmetry example
S = np.array([[1, 2, 3], [2, 5, 4], [3, 4, 6]])
print("\n===Symmetrix matrix ===")
print(f"S = \n{S}")
print(f"S^T = \n{S.T}")
print(f"S is symmetric = {np.array_equal(S, S.T)}")