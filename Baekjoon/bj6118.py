'''
Created by sunwoong on 2022/06/27
'''
import sys
import collections
from typing import Tuple

n, m = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start: int) -> Tuple[int]:
    visited = [False] * (n + 1)
    visited[start] = True
    queue = collections.deque([(start, 0)])
    result = collections.defaultdict(list)
    while queue:
        u, distance = queue.popleft()
        result[distance].append(u)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append((v, distance + 1))
    distance = max(result.keys())
    return min(result[distance]), distance, len(result[distance])

print(*bfs(1))