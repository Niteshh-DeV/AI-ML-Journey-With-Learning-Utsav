import numpy as np

# Determinant of a matrix or 2D array
A = np.array([[1, 2], [3, 4]])

Det = np.linalg.det(A)
print("Determinant:", Det)

# linalag is a submodule of numpy which contains functions for linear algebra operations.
# The det function computes the determinant of an array.

# For 2 decimal places
Det_2dp = np.round(Det, 2)
print("Determinant (2 decimal places):", Det_2dp)
# The round function rounds the elements of an array to the specified number of decimals.

# For Higher Dimensions like (3D array)
B = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
Det_B = np.linalg.det(B)
print("Determinant of 3D array:\n", Det_B)
#This will compute the determinant for each 2x2 matrix in the 3D array.
# Note: Determinant is only defined for square matrices. For non-square matrices, it will raise an error.