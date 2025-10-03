import numpy as np

# Mean
data = np.array([1, 2, 3, 4, 5])
mean_value = np.mean(data)
print("Mean:", mean_value)

# Median
median_value = np.median(data)
print("Median:", median_value)

# Standard Deviation
std_dev = np.std(data)
print("Standard Deviation:", std_dev)

# Variance
# Variance measures how far a set of numbers are spread out from their average value.
variance_value = np.var(data)
print("Variance:", variance_value)

#Minimum and Maximum
min_value = np.min(data)
max_value = np.max(data)
print("Min:", min_value)
print("Max:", max_value)

#argmin and argmax
# argmin and argmax return the indices of the minimum and maximum values in the array. 
# For example: The armin of [1, 2, 3, 4, 5] is 0 (the index of the first element, which is 1),
argmin_index = np.argmin(data)
argmax_index = np.argmax(data)
print("Index of Min:", argmin_index)
print("Index of Max:", argmax_index)

#sum and product
sum_value = np.sum(data)
product_value = np.prod(data)
print("Sum:", sum_value)
print("Product:", product_value)

#Cumsum
# Cumsum returns the cumulative sum of the elements along a given axis. 
# For example: The cumsum of [1, 2, 3, 4, 5] is [1, 3, 6, 10, 15].
cumsum_value = np.cumsum(data)
print("Cumulative Sum:", cumsum_value)
