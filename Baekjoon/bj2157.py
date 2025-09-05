'''
Created by sunwoong 2025/09/05
'''
import sys
from collections import defaultdict, deque

def bfs(start):
    visited = [0 for _ in range(n + 1)]
    queue = deque([(start, 0, 1)])
    result = 0

    while queue:
        node, cost, count = queue.popleft()

        if count > m:
            continue

        if node == n:
            result = max(result, cost)

        for next_node, next_cost in graph[node]:
            if not visited[next_node] or visited[next_node] < cost + next_cost:
                visited[next_node] = cost + next_cost
                queue.append((next_node, visited[next_node], count + 1))
    
    return result

n, m, k = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
edges = []
for _ in range(k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a > b:
        continue
    edges.append((a, b, c))
edges.sort(key=lambda x: -x[2])
seen = set()

for i in range(len(edges)):
    a, b, c = edges[i]
    if (a, b) not in seen:
        graph[a].append((b, c))
        seen.add((a, b))

print(bfs(1))