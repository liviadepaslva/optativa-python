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

w = []
print("\nVetor W: o produto de X pelo inverso de Y")

y.reverse()

for i in range(5):
    w.append(x[i] * y[i])
    print(w[i], end=" ")