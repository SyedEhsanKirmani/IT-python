import numpy as np

# 1D Array
array_1d = np.array([10, 20, 30, 40, 50])
print("Original 1D Array:", array_1d)

# Slicing elements from index 1 to 3 (exclusive)
print("Sliced 1D Array (index 1 to 3):", array_1d[1:4])

# Slicing with a step
print("Sliced 1D Array with step 2:", array_1d[::2])
