import numpy as np

# Reshaping arrays

a = np.array([[1,2,3], [4,5,6]])
print(a.shape)  # (2, 3)

b = a.reshape((3, 2)) # reshape to 3 rows and 2 columns
print(b)
print(b.shape)  # (3, 2)

# Raveling arrays
# Raveling means converting a multi-dimensional array into a one-dimensional array.

c = a.ravel() 
print(c)  # [1 2 3 4 5 6]
print(c.shape)  # (6,) # one-dimensional array


# Flattening arrays
# Flattening is similar to raveling, but it always returns a copy of the original array. 
# ie modifying the flattened array does not affect the original array.

d = b.flatten()
print(d)  # [1 2 3 4 5 6]
print(d.shape)  # (6,)


# Transposing arrays
e = a.T  # transpose of a
print(e)
print(e.shape)  # (3, 2)