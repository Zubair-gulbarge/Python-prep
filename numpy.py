# Creating NumPy Arrays:

import numpy as np

# Create a 1D array
arr1 = np.array([1, 2, 3, 4, 5])

# Create a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Create a range of values using np.arange
arr3 = np.arange(0, 10, 2)  # Generates [0, 2, 4, 6, 8]

print("1D Array:", arr1)
print("2D Array:", arr2)
print("Range Array:", arr3)


# Array Operations:

# Perform element-wise operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

sum_arr = arr1 + arr2
product_arr = arr1 * arr2

print("Sum Array:", sum_arr)
print("Product Array:", product_arr)


# Indexing and Slicing:

# Access and slice elements in arrays
arr = np.array([0, 1, 2, 3, 4, 5])

element = arr[3]  # Access element at index 3
slice_arr = arr[1:4]  # Slice elements from index 1 to 3

print("Element at Index 3:", element)
print("Slice Array:", slice_arr)

# Reshaping and Transposing:

# Reshape and transpose arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])

reshaped_arr = arr.reshape(3, 2)  # Reshape to 3x2
transposed_arr = arr.T  # Transpose the array

print("Reshaped Array:")
print(reshaped_arr)
print("Transposed Array:")
print(transposed_arr)


#  Statistical Operations:

# Compute mean, median, and standard deviation
arr = np.array([10, 20, 30, 40, 50])

mean_val = np.mean(arr)
median_val = np.median(arr)
std_dev = np.std(arr)

print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)


# Element-wise Comparison and Filtering:

# Compare elements and create a boolean array
arr = np.array([1, 2, 3, 4, 5])

greater_than_3 = arr > 3  # Creates a boolean array
filtered_arr = arr[greater_than_3]  # Filter elements

print("Boolean Array (Greater than 3):", greater_than_3)
print("Filtered Array:", filtered_arr)


# Matrix Operations:

# Perform matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

product_matrix = np.dot(matrix1, matrix2)

print("Matrix Multiplication Result:")
print(product_matrix)


# Random Number Generation:

# Generate random numbers
random_numbers = np.random.randint(1, 100, size=(3, 3))

print("Random Numbers:")
print(random_numbers)
