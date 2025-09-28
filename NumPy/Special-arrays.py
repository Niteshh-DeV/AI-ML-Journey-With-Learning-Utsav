import numpy as np

zeros = np.zeros((3,3)) # 3x3 array of zeros
print(zeros)
ones = np.ones((2,4)) # 2x4 array of ones
print(ones)
rand = np.random.rand(2,3)  # random floats
print(rand)
arange = np.arange(0,10,2)  # like range() but returns an array
print(arange)
linspace = np.linspace(0,1,5) # 5 values from 0 to 1
print(linspace)
identity = np.eye(3) # 3x3 identity matrix
print(identity)