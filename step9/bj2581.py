import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

primeN = [False] + [False] + [True] * (n - 1)
for i in range(2, int(n ** 0.5) + 1):
    if primeN[i] == True:
        for j in range(i * 2, n + 1, i):
            primeN[j] = False

primeNumber = [i for i in range(m, n + 1) if primeN[i] == True]
if primeNumber:
    print(sum(primeNumber))
    print(primeNumber[0])
else: print(-1)