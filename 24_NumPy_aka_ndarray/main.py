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
print(f'Zero dimentional array example: {zero_dimensional_array()}')
print(f'One dimensional array example: {arr}')
print(f'Two dimensional array example: {two_dimensional_array()}')
print(f'Three dimensional array example: {three_dimensional_arra()} \n')








