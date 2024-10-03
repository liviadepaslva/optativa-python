M = []
for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f"Digite o valor para M[{i}][{j}]: "))
        linha.append(valor)
    M.append(linha)

soma_linha_4 = sum(M[3])

print(f"A soma de todos os valores da linha 4 é: {soma_linha_4}")
