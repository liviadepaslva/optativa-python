nums = []
numsprimos = []
posprimos = []

for i in range(9):
    nums.append(i)

for i in range(9):
    cont = 0
    for j in range(1, nums[i]+1):
        if nums[i] % j == 0:
            cont += 1
    if cont == 2:
        numsprimos.append(nums[i])
        posprimos.append(i)

for i in range(len(numsprimos)):
    print(f"O número {numsprimos[i]} é primo e está na posição {posprimos[i]}")
