'''
Created by sunwoong on 2022/09/03
'''
import sys
import collections

n, m = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[end].append(start)
target = int(sys.stdin.readline())

def bfs(start: int) -> int:
    result = -1
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    queue = collections.deque([start])
    while queue:
        u = queue.popleft()
        result += 1
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    return result
print(bfs(target))