n = int(input())
num = list(map(int, input().split()))

minV = num[0]
maxV = num[0]

for i in range(0, n):
    if minV > num[i]:
        minV = num[i]
    elif maxV < num[i]:
        maxV = num[i]
print(minV, maxV)