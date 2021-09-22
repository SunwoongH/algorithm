n = int(input())
num = input()
numList = list(num)

result = 0
for newNum in numList:
    result += int(newNum)
print(result)