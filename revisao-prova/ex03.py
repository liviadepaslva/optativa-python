conj1 = set()
conj2 = set()

for i in range(1, 11):
    if i % 2 == 0:
        conj1.add(i)
    else:
        conj2.add(i)

print(conj1 | conj2) # união
print(conj1 & conj2) # interseção
print(conj1 - conj2) # diferença

