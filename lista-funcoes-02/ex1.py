import numpy as np

def intersec(A,B):
    A = set(A)
    B = set(B)
    C = A - B
    C = list(C)
        
    return C

a = np.zeros(10)
b = np.zeros(10)

for i in range(10):
    a[i] = i + 1
    b[i] = i - 1

c = intersec(a,b)

print(a)
print(b)
print(c)
print(c[1])