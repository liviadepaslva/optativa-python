palindromo = input('Digite uma palavra/frase: ')

palindromo = palindromo.strip().lower()

print(palindromo)

if palindromo == palindromo[::-1]:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')