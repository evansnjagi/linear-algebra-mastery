"""
    Linear Algebra Mastery
    ----------------------
    1. Vector and vector operation
"""
# Import
import numpy as np 

# 1.1 Define vector
u = np.array([1, 3])
v = np.array([2, -1])

print("=== Vectors ===")
print(f"u = {u}")
print(f"v = {v}")

# 1.2 Vector addition
addition = u + v

print("\n=== Vector addition ===\n")
print(f"u + v = {addition}")
print(f"v + u = {v + u}")
print(f"Commutative: {np.array_equal(u + v, v + u)}")

# 1.3 Scalar multiplication
print("\n=== Scalar multiplication ===\n")
print(f"2u = {2*u}")
print(f"-1u: = {-1 * u}")
print(f"0u = {0 * u}")
print(f"||u||: {np.linalg.norm(u):.4f}")
print(f"||v||: {np.linalg.norm(v):.4f}")
print(f"Magnitude preserved under -1: {np.isclose(np.linalg.norm(u), np.linalg.norm(-1 * u))}")

# 1.4 Linear combination
v1 = np.array([1, 2])
v2 = np.array([3, -1])
c1, c2 = 2, 3

linear_combination = c1 * v1 + c2 * v2

print("\n=== Linear combination ===\n")
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"2v1 = {2 * v1}")
print(f"3v2 = {3 * v2}")
print(f"2v1 + 3v2: {linear_combination}")

# 1.5 Span. Checking parallel vectors
v1 = np.array([1, 0])
v2 = np.array([0, 1])

v3 = np.array([2, 4])
v4 = np.array([1, 2])

matrix1 = np.column_stack([v1, v2])
matrix2 = np.column_stack([v3, v4])

rank1 = np.linalg.matrix_rank(matrix1)
rank2 = np.linalg.matrix_rank(matrix2)

print("\n=== Span ===\n")
print(f"v1 = {v1}, v2 = {v2}")
print(f"Rank of [v1, v2]: {rank1} and spans R^2: {rank1 == 2}")
print(f"Rank of [v3, v4]: {rank2} and spans R^2: {rank2 == 2}")
print(f"v3 and v4 are parallel: {rank2 == 1}")