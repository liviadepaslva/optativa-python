numsprimos = 0
num = 1
while numsprimos <= 10:
    contador = 0
    for n in range(1, num+1):
        if num % n == 0:
            contador += 1
    if contador == 2:
        print(num, " \n")
        numsprimos +=1
    num += 1