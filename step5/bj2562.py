num = []
for i in range(0, 9):
    inputNum = int(input())
    num.append(inputNum)

maxI = 0
for i in range(0, 9):
    if num[maxI] < num[i]:
        maxI = i
maxV = num[maxI]
print(maxV)
print(maxI + 1)