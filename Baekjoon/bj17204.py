'''
Created by sunwoong on 2022/06/12
'''
import sys
import collections

n, k = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for i in range(n):
    u = int(sys.stdin.readline())
    graph[i].append(u)

visited = [False for _ in range(n)]
def dfs(u: int, target: int, cnt: int) -> int:
    if target == u:
        return cnt
    visited[u] = True
    count = -1
    for v in graph[u]:
        if not visited[v]:
            count = dfs(v, target, cnt + 1)
    return count
print(dfs(0, k, 0))