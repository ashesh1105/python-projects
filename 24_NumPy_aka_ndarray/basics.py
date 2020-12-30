import numpy as np


def create_ndarray():
    return np.array([1,2,3,4,5])

def numpy_version():
    return np.__version__

def zero_dimensional_array():
    return np.array(42)

def two_dimensional_array():
    return np.array([
        [1,2,3,10],
        [4,5,6,11],
        [7,8,9,12]
    ])

def three_dimensional_array():
    return np.array([
        [[1, 2, 3], [4, 5, 6]],
        [[7, 8, 9], [10, 11, 12]]
    ])

# Dimension
def dimension(arr):
    return arr.ndim

# Return array of n dimensions
def create_nd_array(list_arg, dim):
    return np.array(list_arg, ndmin=dim)

def str_array(arg_tuple):
    return np.array(arg_tuple)

def array_with_type(list_arg, type):
    return np.array(list_arg, dtype=type)

def get_nditer(arr):
    return np.nditer(arr)

def get_nditer_with_type(arr, type):
    return np.nditer(arr, flags=['buffered'], op_dtypes=[type])

# will work with 2d array only
def nditer_with_step_size_2d_arr(arr_2d, step_size):
    return np.nditer(arr_2d[:, ::step_size])

# will work with 3d array only
def nditer_with_step_size_3d_arr(arr_3d, step_size):
    return np.nditer(arr_3d[:, :, ::step_size])

# Retunrs tuples of index and elements
def get_ndenumerated_iter(arr):
    return np.ndenumerate(arr)

# Join arrays
def concatenate_arr(arr1, arr2, axis=0):
    return np.concatenate((arr1, arr2), axis=axis)

# Array split
def array_split(arr, n):
    return np.array_split(arr, n)

# Search an array
def search(arr, elem):
    return np.where(arr==elem)

def search_even_elem(arr):
    return np.where(arr % 2 == 0)




