num = int(input("Digite o número que você quer o fatorial: "))
fatorial = num

for n in range(num-1, 1, -1):
    fatorial *= n
    
print("O fatorial de", num, "é", fatorial, "\n")