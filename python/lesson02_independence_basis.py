"""
    Linear Algebra Mastery
    ---------------------
    lesson 2: Independece and basis of a vector
"""
# Import 
import numpy as np 

# 2.1 Checking linear independence via rank
v1 = np.array([1, 2])
v2 = np.array([3, 5])

# 2.1.1 vectors as column of a matrix
matrix = np.column_stack([v1, v2])

# 2.1.2 Compute rank
rank = np.linalg.matrix_rank(matrix)

# 2.1.3 Print results
print("\n=== Linear Independence ===\n")
print("v1 = ", v1)
print("v2 = ", v2)
print("Matrix formed by v1, v2 = \n", matrix)
print(f"Rank = {rank}")
print(f"Linear Independence: {rank == 2}")

# 2.2 Checking dependent vectors
v3 = np.array([2, 4])
v4 = np.array([1, 2])

# 2.2.1 Stack vectors
matrix2 = np.column_stack([v3, v4])

# 2.2.2 Compute rank
rank2 = np.linalg.matrix_rank(matrix2)

# 2.2.3 Print results
print("\n=== Linear Dependence ===\n")
print("v3 = ", v3)
print("v4 = ", v4)
print("Stacked Matrix = \n", matrix2)
print("Second Rank = ", rank2)
print("Linear independent = ", rank2 == 2)
print("Linear dependent = ", rank2 < 2)

# 2.3 Standard basis
print("\n=== Standard basis ===\n")
e1 = np.array([1, 0])
e2 = np.array([0, 1])

# 2.3.1 Stack basis vectors
matrix_basis = np.column_stack([e1, e2])

# 2.3.2 Compute rank
rank_R2 = np.linalg.matrix_rank(matrix_basis)

# 2.3.3 Print result
print("Standard basis for R2")
print("e1 = ", e1)
print("e2 = ", e2)
print("Rank = ", rank_R2)
print(f"Forms a basis for R2 = \n", rank_R2 == 2)

# 2.3.4 Basis for R3
e3 = np.array([1, 0, 0])
e4 = np.array([0, 1, 0])
e5 = np.array([0, 0, 1])

# 2.3.5 Stack basis columns
matrix_R3 = np.column_stack([e3, e4, e5])

# 2.3.6 Compure rank
rank_R3 = np.linalg.matrix_rank(matrix_R3)

# 2.3.7 Print results
print("Standard basis for R3")
print("e3 = ", e3)
print("e4 = ", e4)
print("e5 = ", e5)
print("Stacked matrix = \n", matrix_R3)
print("Rank = ", rank_R3)
print(f"Forms a basis in R3 = {rank_R3 == 3}")

# 2.4 Machine learning connection
# 2.4.1 Feature matrix
X = np.array([[1, 2],[3, 5],[2, 4]])

# 2.4.2 Compute rank
rank_X = np.linalg.matrix_rank(X)

# 2.4.3 Print results
print("ML connection")
print("Feature matrix = \n", X)
print("Rank = ", rank_X)
print("Number of independent features: ", rank_X)
print("Total number of features: ", X.shape[0])
print(f"Redundant features: {X.shape[0] - rank_X}")