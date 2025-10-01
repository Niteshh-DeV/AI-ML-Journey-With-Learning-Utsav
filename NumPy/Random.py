import numpy as np

# Random number generation
# Generating random numbers from a uniform distribution over [0.0, 1.0)

rand_nums = np.random.rand(5)  # array of 5 random numbers
print(rand_nums)

# Generating random integers between a specified range [low, high)
rand_ints = np.random.randint(1, 10, size=5)  # array of 5 random integers between 1 and 10
print(rand_ints)

# Normal distribution
# Generating random numbers from a normal (Gaussian) distribution with mean 0 and standard deviation 1
normal_nums = np.random.randn(5)  # array of 5 random numbers from standard normal distribution
print(normal_nums)

# random.choice
# Randomly selecting elements from a given array
arr = np.array([10, 20, 30, 40, 50])
chosen_elements = np.random.choice(arr, size=3, replace=False)  # choose 3 unique elements
print(chosen_elements)
