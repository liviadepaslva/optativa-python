M = []
for i in range(10):
    linha = []
    for j in range(10):
        valor = float(input(f"Digite o valor para M[{i}][{j}]: "))
        linha.append(valor)
    M.append(linha)

soma_coluna_2 = 0
for i in range(10):
    soma_coluna_2 += M[i][2]

soma_diagonal_principal = 0
for i in range(10):
    soma_diagonal_principal += M[i][i]

print(f"Somatório dos valores da coluna 2: {soma_coluna_2}")
print(f"Somatório dos valores da diagonal principal: {soma_diagonal_principal}")