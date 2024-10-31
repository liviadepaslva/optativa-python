import numpy as np


def matSum(_x):
    sum = 0
    for array in _x:
        for i in array:
            sum += i
            
    return sum


A = np.zeros((5,5))

for i in range(5):
    for j in range(5):
        A[i][j] = i + j
        
print(A)
print(matSum(A))