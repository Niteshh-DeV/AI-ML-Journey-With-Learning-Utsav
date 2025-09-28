import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Array properties
print("Array:\n", arr)  # Display the array

print("Shape:", arr.shape)  # (rows, columns)

print("Dimensions:", arr.ndim)  # Number of dimensions

print("Size:", arr.size)    # Total number of elements

print("Data type:", arr.dtype)   # Data type of elements

print("Item size (bytes):", arr.itemsize) # Size of each element in bytes

print("Total bytes:", arr.nbytes)   # Total bytes consumed by the array