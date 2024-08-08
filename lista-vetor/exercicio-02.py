x = []

for i in range(10):
    valor = int(input("\nDigite um valor para a posição " + str(i) + ": "))
    x.append(valor)

for i in range(10):
    if x[i] % 2 == 0:
        x[i] = x[i] * i
    else:
        x[i] = i

print("Lista atualizada:", x)