frase = input("Digite uma frase: ")
contagem_espacos = 0
contagem_vogais = 0

for c in frase:
    if c == ' ':
        contagem_espacos += 1
    elif c.lower in 'aeiou':
        contagem_vogais += 1

print("Número de espaços:", contagem_espacos)
print("Número de vogais:", contagem_vogais)