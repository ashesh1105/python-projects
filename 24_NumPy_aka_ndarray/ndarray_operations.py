from basics import *

"""
Most of the method calls in this file call methods defined in basics.py
"""

# Iterating array using nditer()
# Helps avoid nested for loops
arr_3d = three_dimensional_array()
my_nditer = get_nditer(arr_3d)
for x in my_nditer:
    print(x)

"""
Iterating arrays with different data types
We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other 
space to perform this action, that extra space is called buffer, and in order to enable it in nditer() 
we pass flags=['buffered'].
"""
arr = array_with_type([1,2,3], 'S')
my_nditer_with_type = get_nditer_with_type(arr, type)
for x in my_nditer_with_type:
    print(x)    # prints b'1' b'2' b'3'

"""
Iterating with different step size
"""
arr = create_nd_array([[1, 2, 3, 4], [5, 6, 7, 8]], 2)
print(arr)  # print [[1, 2, 3, 4], [5, 6, 7, 8]]
my_nditer_with_step_size = nditer_with_step_size_2d_arr(arr, 2)
for x in my_nditer_with_step_size:
    print(x)    # prints 1 3 5 7

print(arr_3d)
my_nditer_with_step_size = nditer_with_step_size_3d_arr(arr_3d, 2)
for x in my_nditer_with_step_size:
    print(x)    # Prints 1st, 3rd, 5th.. elements of every inner most array element

"""
Enumerated Iteration - get index as well as each element while iterating
NumPy.ndenumerate(arr)
"""
arr = create_nd_array([1,2,3], 1)
my_ndenumerated_iter = get_ndenumerated_iter(arr)
for idx, x in my_ndenumerated_iter:
    print(idx, x)

arr_2d = create_nd_array([[1, 2, 3, 4], [5, 6, 7, 8]], 2)
print(arr_2d)
my_en_nd_iter = get_ndenumerated_iter(arr_2d)
for idx, x in my_en_nd_iter:
    print(f'At index: {idx[0]},{idx[1]}: element: {x}')

"""
Join arrays: NumPy.concatenate function
"""
arr1 = create_nd_array([1,2,3], 1)
arr2 = create_nd_array([4,5,6], 1)
# axis needs to be 0 (default) for 1d arrays
result = concatenate_arr(arr1, arr2, 0)
print(result)
# Let's check if concetenated array is a view or a copy, meaning editing this will affect original arrays or not
print(result.base)  # prints None, meaning it is a view. Change in result will reflect changes in original arrays!

# Join 2d array on axis=1
arr1 = create_nd_array([[1,2], [3,4]], 2)   # arr1: [[1,2], [3,4]]
arr2 = create_nd_array([[5,6], [7,8]], 2)   # arr2: [[5,6], [7,8]]
print(concatenate_arr(arr1, arr2, 1))   # prints [[1 2 5 6] [3 4 7 8]] - since axis passed as 1
print(concatenate_arr(arr1, arr2, 0))   # prints [[1,2] [3,4] [5,6] [7,8]] - since axis passed as 0

# Array Split
arr = create_nd_array([1,2,3,4,5,6], 1)
new_arr = array_split(arr, 3)
print(new_arr)  # Returns [array([1, 2]), array([3, 4]), array([5, 6])]
# You can access the individual arrays with indices
print(new_arr[0])   # Prints [1,2]
print(new_arr[1])   # Prints [3,4]
print(new_arr[2])   # Prints [5,6]

"""
Searching an array. NumPy's where() method does it. Returns index of the element, if found
"""
arr = create_nd_array([1,2,3,4,5,6,5,6,5], 1)
idx_arr = search(arr, 5)
print(f'Found element at index: {idx_arr}') # Prints (array([4, 6, 8]),)
print(len(idx_arr[0]))  # Prints 3
for idx in idx_arr[0]:
    print(idx)  # prints 4 6 and 8

# Seach even elements. Say way we can search odd elements too!
idx_arr = search_even_elem(arr)
print(idx_arr)  # prints (array([1, 3, 5, 7]),)
for idx in idx_arr[0]:
    print(idx)  # Prints 1 3 5 7

"""
Filter an array. Takes an array of booleans equal in length as the array
"""
arr = create_nd_array([41, 42, 43, 44], 1)
# Similar to below, you can apply any condition. This applies to each of arr elements and return array of booleans!
filter_arr = arr > 42
filtered_array = arr[filter_arr]
print(filtered_array)   # Prints [43, 44]
# Filter to get even number elements only
filter_arr = arr % 2 == 0
print(arr[filter_arr])  # Prints [42 44]






if __name__=="__main__":
    pass