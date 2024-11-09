
print("Primeira lista")

lista1 = []
for i in range(5):
    valor = int(input(f"Digite o valor para a posição {i}: "))
    lista1.append(valor)

print("Segunda lista")

lista2 = []
for i in range(5):
    valor = int(input(f"Digite o valor para a posição {i}: "))
    lista2.append(valor)

for i in range(5):
    lista1[i] = lista1[i] * lista2[i]

print("Multiplicação das listas")

for i in range(5):
    print(lista1[i])