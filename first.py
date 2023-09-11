# import numpy

# arr = numpy.array([1, 2, 3, 4, 5])

# print(arr)
# importing numpy and giving its alias as np
import numpy as np
# one dimentional array
# arr = np.array([1, 2, 3, 4, 5])

# print(arr)
# print(type(arr))
# print(np.__version__)

# arr1 = np.array(42)

# print(arr1)

# Two dimentional array
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# print(arr2)

#Three dimentional array

# arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(arr3)

# Check number of dimentions

# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

arr = np.array([1, 2, 3, 4], ndmin=10)

print(arr)
print('number of dimensions :', arr.ndim)

# Accessing numpy array elements

# arr = np.array([1, 2, 3, 4])

# print(arr[2])