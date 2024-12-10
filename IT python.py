import numpy as np

# 1D Array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)

# Accessing elements in a 1D array
print("Element at index 2:", array_1d[2])

# 2D Array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(array_2d)

# Accessing elements in a 2D array
print("Element at row 1, column 2:", array_2d[1, 2])

# Slicing in 1D Array
print("\nSliced 1D Array (from index 1 to 3):", array_1d[1:4])

# Slicing in 2D Array
print("\nSliced 2D Array (rows 0 to 1, columns 1 to 2):")
print(array_2d[0:2, 1:3])

#
