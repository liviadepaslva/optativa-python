x = []

print("Vetor X:")

for i in range(5):
    valor = int(input("\nDigite um valor para a posição " + str(i) + ": "))
    x.append(valor)

y = []

print("\nVetor Y:")

for i in range(5):
    valor = int(input("\nDigite um valor para a posição " + str(i) + ": "))
    y.append(valor)

z = []

print("\nVetor Z: a soma de X e Y")

for i in range(5):
    z.append(x[i] + y[i])
    print(z[i], " ")