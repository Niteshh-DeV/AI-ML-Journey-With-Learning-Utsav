import numpy as np

#Slicing of 1D array
array1 = np.array([1,2,3,4,5])
print("1D Array:", array1)
print("Elements from index 1 to 4:", array1[1:4])
print("Elements from start to index 3:", array1[:3])
print("Elements from index 2 to end:", array1[2:])

#Negetive Slicing of 1D array
print("Elements from index -4 to -1:", array1[-4:-1])
print("Elements from start to index -2:", array1[:-2])
print("Elements from index -3 to end:", array1[-3:])

#Slicing of 2D array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("2D Array:\n", arr)
print("Elements from row 0 to 2 and column 0 to 2:\n", arr[0:2, 0:2])

print("Elements from row 1 to end and column 1 to end:\n", arr[1:, 1:])

#Negetive Slicing of 2D array
print("Elements from row -2 to end and column -2 to end:\n", arr[-2:, -2:])
print("Elements from row -3 to -1 and column -3 to -1:\n", arr[-3:-1, -3:-1])