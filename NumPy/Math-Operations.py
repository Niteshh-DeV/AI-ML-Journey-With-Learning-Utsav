import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)       # elementwise add
print(a * b)       # elementwise multiply
print(a ** 2)      # power
print(np.sqrt(a))  # universal functions
print(np.mean(a))  # mean
print(np.max(b))   # max
print(np.min(b))   # min

#Broadcasting
A = np.array([[1,2,3], [4,5,6], [7,8,9]])
B = np.array([1,0,1])

print(A + B)  # each row of A has B added to it
print(A * 2)  # each element of A is multiplied by 2

print(B+10) # add 10 to each element of b