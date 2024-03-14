import numpy as np

######################################################################
#Question1
arr = np.array([[1, 1, 1] , [1, 2, 3] , [2, 2, 2]])
def find_equal(arr):
    output_arr = np.array([])
    for i in range(len(arr)):
        if len(np.unique(arr[i])) == 1:
            output_arr = np.append(output_arr, arr[i])
    return output_arr.reshape((-1, len(arr[0])))

######################################################################
#Question2
def checkerboard():
    dim = 9 # need an odd number to properly create a checkerboard
    arr = np.ones((dim**2,1))
    arr[1:-1:2] = 0
    return arr.reshape(dim, dim)[0:8, 0:8]
#print(checkerboard())

######################################################################
# Question 3
def spaceBetween(arr):
    out_arr = np.array([])
    for val in arr:
        out_arr = np.append(out_arr, " ".join(val))
    return out_arr
myarr = np.array(['python', 'is', 'cool!'])
#print(spaceBetween(myarr))

######################################################################
#Question4

random_arr = np.array([[35,38,30,2,37],[42,38,35,30,2],[15,42,28,17,10],[12,14,11,18,19]])
print(np.sort(random_arr, axis=0))