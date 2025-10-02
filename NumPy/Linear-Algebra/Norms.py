import numpy as np

# Norms
# The norm of a vector is a measure of its length or magnitude.
# The most common norm is the Euclidean norm (L2 norm), which is the square root of the sum of the squares of the vector's components.
# Other norms include the L1 norm (sum of absolute values) and the infinity norm (maximum absolute value).

# 1D array (vector)
v = np.array([3, 4])
print("Vector v:", v)

norm_v = np.linalg.norm(v)  # Default is L2 norm
print("L2 Norm of vector v:", norm_v)
norm_v1 = np.linalg.norm(v, 1)  # L1 norm
print("L1 Norm of vector v:", norm_v1)
norm_v_inf = np.linalg.norm(v, np.inf)  # Infinity norm
print("Infinity Norm of vector v:", norm_v_inf)

# 2D array (matrix)
A = np.array([[1, 2], [3, 4]])
print("Matrix A:\n", A)

norm_A = np.linalg.norm(A)  # Frobenius norm (default for matrices)
print("Frobenius Norm of matrix A:", norm_A)
# Frobenius norm is the square root of the sum of the absolute squares of its elements.
norm_A1 = np.linalg.norm(A, 1)  # Max column sum
print("Max Column Sum Norm of matrix A:", norm_A1)
# This is the maximum absolute column sum of the matrix. Also known as the L1 norm for matrices.

norm_A_inf = np.linalg.norm(A, np.inf)  # Max row sum
print("Max Row Sum Norm of matrix A:", norm_A_inf)
# This is the maximum absolute row sum of the matrix. Also known as the L-infinity norm for matrices.
# For higher dimensions, like 3D arrays, the function computes the norm for each 2D slice along the last two axes.