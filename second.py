# Import NumPy
import numpy as np

# Create a NumPy array from a list
arr = np.array([1, 2, 3, 4, 5])

# Basic array attributes
print("Array shape:", arr.shape)
print("Array data type:", arr.dtype)
print("Number of dimensions:", arr.ndim)
print("Number of elements:", arr.size)

# Reshape an array
reshaped_arr = arr.reshape(2, 3)
print("Reshaped array:")
print(reshaped_arr)

# Accessing elements and slices
print("Element at index 2:", arr[2])
print("Slicing from index 1 to 3:", arr[1:4])

# Array operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise operations
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# Dot product of two arrays
dot_product = np.dot(a, b)
print("Dot Product:", dot_product)

# Broadcasting (expanding dimensions)
c = np.array([1, 2, 3])
scalar = 2
result = c * scalar
print("Broadcasting Result:", result)

# NumPy functions
mean_value = np.mean(arr)
max_value = np.max(arr)
min_value = np.min(arr)
sum_value = np.sum(arr)

print("Mean:", mean_value)
print("Max:", max_value)
print("Min:", min_value)
print("Sum:", sum_value)

# Creating arrays
zeros_array = np.zeros((2, 3))
ones_array = np.ones((3, 3))
identity_matrix = np.eye(4)
random_array = np.random.rand(2, 2)

print("Zeros Array:")
print(zeros_array)
print("Ones Array:")
print(ones_array)
print("Identity Matrix:")
print(identity_matrix)
print("Random Array:")
print(random_array)
