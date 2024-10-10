lista = []

for i in range(5):
    valor = int(input(f"Digite o valor para a posição {i} da lista: "))
    lista.append(valor)

del lista[4]

for i in range(4):
    print(f"posição {i}: {lista[i]}")

maior = lista[0]
menor = lista[0]

for i in range(4):
    if lista[i] > maior:
        maior = lista[i]

    if lista[i] < menor:
        menor = lista[i]

print(f"O maior valor é {maior} e o menor valor é {menor}")