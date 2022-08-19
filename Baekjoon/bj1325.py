'''
Created by sunwoong on 2022/08/19
'''
import sys
import collections

def bfs(start: int) -> int:
    visited = [False for _ in range(n + 1)]
    queue = collections.deque([start])
    visited[start] = True
    count = 0
    while queue:
        u = queue.popleft()
        count += 1
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    return count

n, m = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[v].append(u)
max_count = 0
result = []
for i in range(1, n + 1):
    count = bfs(i)
    if count > max_count:
        max_count = count
        result.clear()
        result.append(i)
    elif count == max_count:
        result.append(i)
print(*result)