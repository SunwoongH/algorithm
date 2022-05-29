'''
Created by sunwoong on 2022/05/29
'''
from typing import List
import sys
import collections

n, m, k, x = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)

def bfs(start: int) -> List[int]:
    result = []
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    queue = collections.deque([(start, 0)])
    while queue:
        u, distance = queue.popleft()
        if distance == k:
            result.append(u)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append((v, distance + 1))
    return result

result = bfs(x)
print(*sorted(result), sep='\n') if result else print(-1)