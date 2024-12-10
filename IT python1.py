import numpy as np

# Original 1D array
array_1d = np.array([1, 2, 3])
print("Original 1D Array:", array_1d)

# Append a single element
array_1d = np.append(array_1d, 4)
print("1D Array after appending 4:", array_1d)

# Append multiple elements
array_1d = np.append(array_1d, [5, 6])
print("1D Array after appending [5, 6]:", array_1d)
