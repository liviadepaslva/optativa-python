import numpy as np

tamanho = 6
vetor = np.zeros(tamanho)

for i in range(tamanho):
    vetor[i] = i+1

for i in range(tamanho-1, -1, -1):
    print(vetor[i])