import numpy as np

a = np.array([[1,2,3], [4,5,6]])
print(a.shape)  # (2, 3)

# Stacking arrays
# Stacking arrays is the process of joining two or more arrays along a specified axis.

b = np.array([[7,8,9], [10,11,12]])
print(b.shape)  # (2, 3)

# Vertical stacking
# Stacking arrays vertically means stacking them row-wise (along axis 0).

v_stack = np.vstack((a, b))
print(v_stack)
print(v_stack.shape)  # (4, 3)

# Horizontal stacking
# Stacking arrays horizontally means stacking them column-wise (along axis 1).

h_stack = np.hstack((a, b))
print(h_stack)
print(h_stack.shape)  # (2, 6)


#Column stacking
# Column stacking is similar to horizontal stacking, but it treats 1-D arrays as columns.

c = np.array([13, 14])
print(c.shape)  # (2,)  # 1-D array
col_stack = np.column_stack((a, c))
print(col_stack)
print(col_stack.shape)  # (2, 4)

#Concatenation
# Concatenation is a more general way of joining arrays along an existing axis.

concat1 = np.concatenate((a, b), axis=0)  # axis = 0 means along rows
print(concat1)
print(concat1.shape)  # (4, 3)

concat2 = np.concatenate((a, b), axis=1)  # axis = 1 means along columns
print(concat2)
print(concat2.shape)  # (2, 6)