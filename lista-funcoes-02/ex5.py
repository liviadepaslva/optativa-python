import numpy as np

def diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma


matriz = np.zeros((5,5))
for i in range(len(matriz)):
    for j in range(len(matriz)):
        matriz[i][j] = int(input("Digite um número:"))

print(diagonal(matriz))