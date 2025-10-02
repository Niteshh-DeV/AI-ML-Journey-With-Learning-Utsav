import numpy as np

# Eigenvalues and Eigenvectors

A = np.array([[4, -2], [1, 1]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Matrix A:\n", A)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
# Each column in 'eigenvectors' corresponds to an eigenvalue in 'eigenvalues'.

# .eig function returns two arrays - one for eigenvalues and another for eigenvectors.

# For higher dimensions, like 3D arrays, the function computes eigenvalues and eigenvectors for each 2D slice along the last two axes.
B = np.array([[[4, -2], [1, 1]], [[3, 0], [0, 3]]])
eigenvalues_B, eigenvectors_B = np.linalg.eig(B)
print("3D Array B:\n", B)
print("Eigenvalues of B:\n", eigenvalues_B)
print("Eigenvectors of B:\n", eigenvectors_B)