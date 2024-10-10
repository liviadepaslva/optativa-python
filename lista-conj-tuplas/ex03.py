l = []

for i in range(20):
    l.append(i)

print(l)

x = []
y = []

for i in range(20):
    if i % 2 == 0:
        x.append(l[i]) # nums pares
    else:
        y.append(l[i]) # num impares

aux = 0
aux2 = 0

for i in range(20):
    if i % 2 == 0:
        l[i] = y[aux2]
        aux2 += 1
    else:
        l[i] = x[aux]
        aux += 1

print(l)