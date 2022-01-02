import sys

def knapsack(v, w, n, k):
    bag = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if w[i] <= j:
                if bag[i - 1][j] < v[i] + bag[i - 1][j - w[i]]: 
                    bag[i][j] = v[i] + bag[i - 1][j - w[i]]
                else: bag[i][j] = bag[i - 1][j]
            else: bag[i][j] = bag[i - 1][j]
    return bag[n][k]

n, k = map(int, sys.stdin.readline().split())
w = [0]
v = [0]
for i in range(n):
    inputW, inputV = map(int, sys.stdin.readline().split())
    w.append(inputW)
    v.append(inputV)
print(knapsack(v, w, n, k))