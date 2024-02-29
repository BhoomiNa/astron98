
import numpy as np
"""
if there is a problem with this line:
    do Command+shift+p or Ctrl+shift+p
    search Python: Select Interpreter
    select the 'base' or conda environment
"""
# add two arrays and add two lists


# sum of numbers
#Takes the sum of the numbers 0 to 100 with a loop

def loopSum(x):
    final_sum = 0
    for x in range(0,101,1):
        final_sum += x 
    return final_sum
print(loopSum(101))


#Takes the sum of the numbers 0 to 100 user Numpy

def arraySum():
    return np.sum(np.arange(101))

print(arraySum())


# slicing

def lastTwo(myarr):
    """
    Returns the last two columns of the array
    Try to make it work for any input array!
    >>> arr = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])
    >>> lastTwo(arr)
    array([[2, 3],
           [5, 6],
           [8, 9]])
    """
    return "YOUR CODE HERE"

def everyOther(way, myarr):
    """
    Returns every other row or column depending on input for way
    >>> arr = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])
    >>> everyOther("row", arr)
    array([[1, 2, 3],
           [7, 8, 9]])
    >>> everyOther("column", arr)
    array([[1, 3],
           [4, 6],
           [7, 9]])
    """
    if way == 'row':
        return "YOUR CODE HERE" 
    elif way == 'column':
        return "YOUR CODE HERE"
    else:
        return "YOUR CODE HERE" 

# useful functions

# only do this if time permits

print(f'I can make an array of zeros: {np.zeros(4)}')
print(f'I can make an array of random numbers: {np.random.random(5)}')
