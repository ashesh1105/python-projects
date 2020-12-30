from basics import *

'''
What is NumPy?
NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear 
algebra, fourier transform, and matrices.

NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.

NumPy stands for Numerical Python.

Why Use NumPy?
In Python we have lists that serve the purpose of arrays, but they are slow to process. NumPy aims to provide 
an array object that is up to 50x faster than traditional Python lists.

The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with 
ndarray very easy. Arrays are very frequently used in data science, where speed and resources are very important.

Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving 
information from it.

Why is NumPy Faster Than Lists?
NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate 
them very efficiently. This behavior is called locality of reference in computer science. This is the main reason 
why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.

Which Language is NumPy written in?
NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation 
are written in C or C++.

Where is the NumPy Codebase?
The source code for NumPy is located at this github repository https://github.com/numpy/numpy

Install NumPy by: pip install numpy
'''
# Methods being called here are not NumPy methods, they are from dependent modules here like ./basics.py, etc.


# Create ann ndarray
arr = create_ndarray()
print(f'Array created: {arr}')
print(f'Type: {type(arr)} \n')


# Check NumPy version
print(f'NumPy version: {numpy_version()} \n')

# 0-D arrays
arr_0d = zero_dimensional_array()
print(f'Zero dimentional array example: {arr_0d} \n')
# arr_0d[0] # this will not be allowed since this has no dimension on it :)

arr_1d = create_ndarray()
print(f'One dimensional array example: {arr_1d}')
print(f'arr_1d[0]: {arr_1d[0]}\n')

arr_2d = two_dimensional_array()
arr_3d = three_dimensional_array()
print(f'Two dimensional array example: {arr_2d}')
print(f'Three dimensional array example: {arr_3d} \n')

# Check dimensions of an array
print(f'Array Dimension: {dimension(arr_3d)}')

# Create array of n dimensions
arr = create_nd_array([1,2,3,4,5], 5)
print('Created array dimension: ', arr.ndim)

# Accessing 1D array is easy, let's access a 2D array
print(f'\nAccessing [1,3] element from 2D array \n{arr_2d}: \n{arr_2d[1,3]}')
print(f'\nAccessing [1,1,1] element from 3D array \n{arr_3d}: \n{arr_3d[1,1,1]}')

# Negative indexing is allowed in Python. -1 means last element
print(f'\nAccessing [1,1,1] element from 3D array \n{arr_3d}: \n{arr_3d[1,-1,-1]}')

# Slicing arrays. Does not include specified end index
print(f'\nSlicing [1:3] elements from array \n{arr_1d}: \n{arr_1d[1:3]}')
print(f'\nSlicing [1:] elements from array \n{arr_1d}: \n{arr_1d[1:]}')
print(f'\nSlicing [:4] elements from array \n{arr_1d}: \n{arr_1d[:4]}')
print(f'\nSlicing [-1:-3] elements from array \n{arr_1d}: \n{arr_1d[-3:-1]}')   # Returns [3,4]

# Like with strings, you can use STEP too with slicing
print(f'\nSlicing [1:5:2] elements from array \n{arr_1d}: \n{arr_1d[1:5:2]}')   # Returns [2,4]

# Slicing arrays 2D, 3D, etc
print(f'\nSlicing [1, 1:3] elements from array \n{arr_2d}: \n{arr_2d[1, 1:3]}')   # Returns [5,6]

# dtype of arrays
print(f'\nData type of array \n{arr_1d}: \n{arr_1d.dtype}')     # Returns int64
fruit_tuple = ('orange', 'apple', 'guava')
# Now, pass tupple to basic.str_array and get the ndarray
str_arr = str_array(fruit_tuple)
print(f'\nData type of array \n{str_arr}: \n{str_arr.dtype}')   # Returns <U6

# You can pass a dtype while creating an ndarray
my_list = [1,2,3,4,5,6,7]
str_arr2 = array_with_type(my_list, 'S')
print(f'\nData type of array \n{str_arr2}: \n{str_arr2.dtype}')   # Returns <|S1

# You'll get a ValueError if you try this
my_list = ['a', '2', '3']
try:
    str_arr3 = array_with_type(my_list, 'i')    # meaning create an integer array
except ValueError as err:
    print(err)  # You'll see: "invalid literal for int() with base 10: 'a'" on console

"""
Data Types allowed in nparray:
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

# Let's try converting data types of arrays
my_list = [1.2, 4.56, 45.78, 12.34]
arr = array_with_type(my_list, 'f')
print(f'\nData type of array \n{arr}: \n{arr.dtype}')   # Returns [ 1.2 4.56 45.78 12.34]: float32
# Let's convert float array to int array. You can also do astype(int) for same result
arr_i = arr.astype('i')
print(f'\nData type of array \n{arr_i}: \n{arr_i.dtype}')   # Returns [ 1 4 45 12]: int32

"""
ndarray .copy() and .view()
.copy() creates a brand new array, change that one, it won't affect original. Great for ensuring immutability!
.view() - change view, it changes original array
Call .base on copied array, it will return original array day, meaning new arrays owns its data
Call .base on a view, it will return None, meaning views do not own its data!
TODO: try it out!
"""

"""
shape of an ndarray returns a tuple with each index having its corresponding element with it
Example (M, N, P), for M x N x P for a 3 dimensional array

You can reshape an array if you want, say change 1d array to 3d by applying arr.reshape(2, 3, 2)
"""
print(f'\nshape of array \n{arr}: \n{arr.shape}')   # Returns (4,), meaning 1d array with 4 elements in it!
print(f'\nshape of array \n{arr_2d}: \n{arr_2d.shape}')   # Returns (3, 4), meaning 2d array 3x4!
print(f'\nshape of array \n{arr_3d}: \n{arr_3d.shape}')   # Returns (2, 2, 3), meaning 3d array 2x2x3!
# Let's create a 5 dimensional array using basics.create_nd_array(list, dimension)
arr = create_nd_array([1,2,3,4,5], 5)
# Now, let's check its shape
print(f'\nshape of array \n{arr}: \n{arr.shape}')   # Returns (1, 1, 1, 1, 5), meaning 5d array 1x1x1x1x5!

# You can create a multi dimensional array from a 1d array by using reshape!
arr = create_nd_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 1)   # Created a 1d array
# Below will create a 4x3 2d array using elements of 1d array like below:
# Note: Total number of elements supplied must be equal to multiplication of dimensions (in this case 4*3)!!!
"""
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
"""
arr_43 = arr.reshape(4, 3)
print(f'\nshape of array \n{arr_43}: \n{arr_43.shape}')   # Returns (4, 3), meaning 2d array 4x3!

# Also note, reshape creates a view, meaning change that and it changes your original array!!
print(f'arr_43.base: {arr_43.base}')    # returns original array: [ 1  2  3  4  5  6  7  8  9 10 11 12]

# You can skip a dimension by passing -1 on .reshape() method and NumPy will calculate it for you.

"""
Flatening of an ndarray: .reshape(-1) => returns you a 1D array using elements in all the dimensions
"""
arr_flattened = arr_3d.reshape(-1)
print(f'\nshape of flattened array \n{arr_flattened}: \n{arr_flattened.shape}') # Returns (12,) meaning 1d array
print(f'Lets check base of a flattened array arr_flattened: {arr_flattened.base}')  # Returns original 3D array, meaning its a view!


# Some random int and float type number generation examples
import random
# randrange gives random integer between range specified
print('\n\n\n')
random_int = random.randrange(80, 100)
print(f'random float: {random_int}')
# random.uniform gives random floating pt number with uniform distribution
random_float = random.uniform(80.0, 100.0)
print(f'random_float: {random_float}')

random_random = random.random() * 100
print(f'random_random: {random_random}')

# Now, this is how you can get random floating point number with precision
random_float_precision_2 = round(random.uniform(70, 100), 2)
print(f'random_float_precision_2: {random_float_precision_2}')

# Below will also work, except it random() method does not take range
random_float_prcision_2_by_random = round(random.random() * 100, 2)
print(f'random_float_prcision_2_by_random: {random_float_prcision_2_by_random}')



if __name__=="__main__":
    pass






