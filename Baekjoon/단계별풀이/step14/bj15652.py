'''
문제 - N과 M (4)

풀이 방법 - 재귀 구조 DFS로 풀이
'''
import sys
n, m = map(int, sys.stdin.readline().split())
path = []
def dfs():
    if len(path) == m:
        print(*path)
        return
    for i in range(1, n + 1):
        if not path or path[-1] <= i:
            path.append(i)
            dfs()
            path.pop()
dfs()