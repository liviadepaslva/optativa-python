dicionario = { "Arthur": 10,
               "Brian": 0,
               "Livia": 9}

aluno = input("Digite o nome do aluno: ")

if aluno in dicionario:
    print(f"A nota de {aluno} é {dicionario[aluno]}")
else:
    print(f"{aluno} não está no dicionário")