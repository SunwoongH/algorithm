'''
Created by sunwoong on 2024/08/09
'''
import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)

n, m, k = map(int, sys.stdin.readline().split())
candy = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(curr, visited):
    global count
    count += 1
    total = 0
    visited[curr] = True
    total += candy[curr - 1]
    for next in graph[curr]:
        if not visited[next]:
            total += dfs(next, visited)
    return total

visited = [False for _ in range(n + 1)]
promising = []

for i in range(1, n + 1):
    if not visited[i]:
        count = 0
        total = dfs(i, visited)
        promising.append((count, total))

dp = [[0 for _ in range(k)] for _ in range(len(promising) + 1)]

for r in range(1, len(promising) + 1):
    for c in range(1, k):
        if promising[r - 1][0] > c:
            dp[r][c] = dp[r - 1][c]
        else:
            dp[r][c] = max(dp[r - 1][c - promising[r - 1][0]] + promising[r - 1][1], dp[r - 1][c])

print(dp[len(promising)][k - 1])