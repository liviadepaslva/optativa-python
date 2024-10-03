matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

diagonal = [matriz[i][i] for i in range(5)]
print("Valores da diagonal principal:", diagonal)
