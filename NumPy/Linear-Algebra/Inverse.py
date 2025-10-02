import numpy as np

# Inverse of a matrix or 2D array
A = np.array([[1, 2], [3, 4]])

Inverse_A = np.linalg.inv(A)
print("Inverse of A:\n", Inverse_A)

#For Higher Dimensions like (3D array)
B = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
Inverse_B = np.linalg.inv(B)
print("Inverse of 3D array B:\n", Inverse_B)
#This will compute the inverse for each 2x2 matrix in the 3D array
# Note: Inverse is only defined for square matrices. For non-square matrices, it will raise an error.
# Also, not all square matrices are invertible. If a matrix is singular (determinant is zero), it does not have an inverse and will raise an error.