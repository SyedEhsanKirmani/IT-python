import numpy as np
# 2D Array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nOriginal 2D Array:\n", array_2d)

# Slicing rows and columns (subarray)
print("Sliced 2D Array (rows 0-1, columns 1-2):\n", array_2d[0:2, 1:3])

# Slicing entire rows or columns
print("First row:", array_2d[0, :])
print("First column:", array_2d[:, 0])
