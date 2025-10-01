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
variance_value = np.var(data)
print("Variance:", variance_value)

#Minimum and Maximum
min_value = np.min(data)
max_value = np.max(data)
print("Min:", min_value)
print("Max:", max_value)

#argmin and argmax
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
cumsum_value = np.cumsum(data)
print("Cumulative Sum:", cumsum_value)
