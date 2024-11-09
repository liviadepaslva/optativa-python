carros = ["Gol", "Voyage", "Passati", "Fiesta", "Astra"]
consumo = [10, 9, 8, 12, 7]

maispos = 0
maiskm = 0

for i in range(5):
    if consumo[i] > maiskm:
        maiskm = consumo[i]
        maispos = i

print(f"O carro mais economico é o {carros[maispos]}")

print("Cada carro consome em 1000km:")

for i in range(5):
    print(f"{carros[i]}: {1000*consumo[i]} litros")