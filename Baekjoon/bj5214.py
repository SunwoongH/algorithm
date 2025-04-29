'''
Created by sunwoong on 2025/04/29
'''
import sys
from collections import deque, defaultdict

n, k, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for i in range(1, m + 1):
    stops = list(map(int, sys.stdin.readline().split()))
    for stop in stops:
        graph[stop].append(n + i)
    graph[n + i].extend(stops)

visited = [False for _ in range(n + m + 1)]
queue = deque([(1, 0)])
visited[1] = True

is_promising = False
while queue:
    stop, count = queue.popleft()
    if stop == n:
        is_promising = True
        print(count + 1)
        break

    for node in graph[stop]:
        if not visited[node]:
            visited[node] = True
            if node > n:
                queue.append((node, count + 1))
            else:
                queue.append((node, count))

if not is_promising:
    print(-1)