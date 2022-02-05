import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline()))
result = 0
index = len(coin) - 1
while k != 0 and index >= 0:
    check = k // coin[index]
    if check > 0:
        k = k % coin[index]
        result += check
    index -= 1
print(result)