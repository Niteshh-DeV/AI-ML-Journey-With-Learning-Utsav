import numpy as np

# Matrix Multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = np.dot(A, B)  # or C = A @ B    
print("Matrix Multiplication Result:\n", C)
# The @ is also used for matrix multiplication

D = A @ B
print("Matrix Multiplication Result using @:\n", D)

# np.matmul can also be used for matrix multiplication
E = np.matmul(A, B) # same as np.dot for 2-D arrays
print("Matrix Multiplication Result using np.matmul:\n", E)
# For higher dimensions, np.matmul behaves differently than np.dot.
# For example, for 3-D arrays, np.matmul performs matrix multiplication on the last two dimensions.
