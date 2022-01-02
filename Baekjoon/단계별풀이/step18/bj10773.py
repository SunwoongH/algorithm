import sys

k = int(sys.stdin.readline())
data = []
for i in range(k):
    data.append(int(sys.stdin.readline()))

result = []
for d in data:
    if d == 0:
        result.pop()
    else:
        result.append(d)

sum = 0
for d in result:
    sum += d
print(sum)