matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = 0
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        soma += matriz[i][j]

for i in range(3):
    for j in range(3):
        print(f"{matriz[i][j]}", end=" ")
    print(" ")

print(f" a soma dos elementos da matriz é: {soma}")


