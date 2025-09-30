import numpy as np  

# Splitting arrays
# Splitting arrays is the process of dividing an array into multiple sub-arrays.

# 1-D array splitting
a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)  # (6,)

b = np.array_split(a, 3)  # split a into 3 sub-arrays
print(b)  # [array([1, 2]), array([3, 4]), array([5, 6])]

# 2-D array splitting
c = np.array([[1, 2, 3], [4, 5, 6]])
print(c.shape)  # (2, 3)

hsplit = np.hsplit(c, 3)  # split c into 3 sub-arrays horizontally (column-wise)
print(hsplit)  # [array([[1], [4]]), array([[2], [5]]), array([[3], [6]])]

vsplit = np.vsplit(c, 2)  # split c into 2 sub-arrays vertically (row-wise)
print(vsplit)  # [array([[1, 2, 3]]), array([[4, 5, 6]])]