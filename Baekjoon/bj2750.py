n = int(input())

num = []
for i in range(n):
    inputNum = int(input())
    num.append(inputNum)


for i in range(0, n - 1):
    min = i
    for j in range(i + 1, n):
        if num[min] > num[j]:
            min = j
    if min != i:
        temp = num[i]
        num[i] = num[min]
        num[min] = temp

for i in range(n):
    print(num[i])