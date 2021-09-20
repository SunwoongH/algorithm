n = int(input())
scores = list(map(int, input().split()))

maxS = scores[0]
for score in scores:
    if maxS < score:
        maxS = score

for i in range(0, n):
    scores[i] = (scores[i] / maxS) * 100

result = 0
for score in scores:
    result += score

result /= n
print(result)