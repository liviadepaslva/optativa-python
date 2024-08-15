data_nascimento = input('Digite a data de nascimento (dd/mm/aaaa): ')

dia, mes, ano = data_nascimento.split('/')

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

print(f'Você nasceu em {dia} de {meses[int(mes) - 1]} de {ano}.')
