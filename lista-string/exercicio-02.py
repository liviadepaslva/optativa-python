nome = input("Digite seu nome: ")

nome = nome.upper()

for i in range(len(nome)):
    print(nome[:i+1])