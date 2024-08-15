string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda: ")

if string2 in string1:
    posicao = string1.index(string2) + 1
    print(f"{string2} encontrado na posição {posicao}")
else:
    print(f"{string2} não encontrado na primeira string")

