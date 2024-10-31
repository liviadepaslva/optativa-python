import numpy as np

def calculadora(op,x,y):
    result = 0
    match op:
        case "adição":
            result = x + y
        case "subtração":
            result = x - y
        case "multiplicação":
            result = x * y
        case "divisão":
            result = x / y
        case _:
            print("Há algo de errado")
    return result

n1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador(por extenso com acento): ")
n2 = float(input("Digite o segundo número: "))

print(calculadora(operador,n1,n2))
        