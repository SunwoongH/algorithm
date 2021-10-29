import sys

n, k = map(int, sys.stdin.readline().split())
data = []
for i in range(n):
    data.append(i + 1)

result = []
index = k - 1
while True:
    result.append(data[index])
    del data[index]
    size = len(data)
    if size == 0: break
    index = (index + k - 1) % size

print('<', end='')
print(*result, sep=', ', end='')
print('>', end='')