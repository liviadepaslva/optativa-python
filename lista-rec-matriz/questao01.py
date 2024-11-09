n = int(input("Digite a ordem da matriz: "))

matriz = []

print("Matriz 1")

for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

matriz2 = []

print("Matriz 2")

for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz2.append(linha)

soma = 0

for i in range(n):
    for j in range(n):
        soma = matriz[i][j] + matriz2[i][j]

print(f"A soma das matrizes é {soma}")
    

