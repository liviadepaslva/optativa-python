vetor = []

for i in range(9):
    vetor.append(int(input(f"Digite o número da posição {i}: ")))

for i in range(9):
    divisores = 0
    for j in range(1, vetor[i] + 1):
        if vetor[i] % j == 0:
            divisores += 1
    if divisores == 2:
        print(f"Número primo {vetor[i]} encontrado na posição {i}")