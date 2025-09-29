import numpy as np

array1 = np.array([1,2,3,4,5])
arr = np.array([[1, 2, 3], [4, 5, 6]])

#Array Indexing
print(array1)
print("Array:\n", arr)

print("First Element of 1d array is :", array1[0]) # First element of 1d array

print("First Element of 2d array is :", arr[0,0]) # First element of 2d array

print("Last Element of 1d array is :", array1[-1])

print("Last Element of 2d array is :", arr[-1,-1])

print("Last Element of 2d array is :", arr[1,2])

print ("4th Element of 1d array is :", array1[3])