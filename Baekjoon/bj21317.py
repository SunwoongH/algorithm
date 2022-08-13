'''
Created by sunwoong on 2022/08/13
'''
import sys

n = int(sys.stdin.readline())
energy = [[0, 0]]
for _ in range(n - 1):
    energy.append(list(map(int, sys.stdin.readline().split())))
k = int(sys.stdin.readline())

result = sys.maxsize
def dfs(start, target, select):
    if start > n:
        return
    if start == n:
        global result
        result = min(result, target)
        return
    dfs(start + 1, target + energy[start][0], select)
    dfs(start + 2, target + energy[start][1], select)
    if select:
        dfs(start + 3, target + k, False)
dfs(1, 0, True)
print(result)