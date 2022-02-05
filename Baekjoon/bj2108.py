import sys
import operator

n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))

sNum = sorted(num)

avg = round(sum(num) / n)
midValue = sNum[n // 2]
rangeV = sNum[n - 1] - sNum[0]

numDic = {}
for v in sNum:
    if v not in numDic:
        numDic[v] = 1
    else:
        numDic[v] += 1

result = sorted(numDic.items(), key = operator.itemgetter(1))
result.reverse()
maxIValue = result[0][1]
check = False
result2 = [result[0][0]]
for i in range(1, len(result)):
    if maxIValue == result[i][1]:
        result2.append(result[i][0])
    else:
        break
result2 = sorted(result2)
minV = result2[0]
for i in range(1, len(result2)):
    if minV != result2[i]:
        minV = result2[i]
        break

print(avg)
print(midValue)
print(minV)
print(rangeV)