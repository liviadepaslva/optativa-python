import numpy as np

def zerNeg(A):
    for i in range(len(A)):
        if A[i] < 0:
            A[i] = 0
    return A
            
V = np.zeros(15)

for i in range(15):
    V[i] = int(input("Digite um número: "))

print(V)
print(zerNeg(V))
