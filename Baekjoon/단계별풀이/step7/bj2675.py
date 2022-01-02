t = int(input())
test = []
for i in range(0, t):
    r, s = map(str, input().split())
    test.append([r, s])

for i in test:
    n = int(i[0])
    newS = list(i[1])
    resultS = ""
    for j in newS:
        resultS += j * n
    print(resultS)