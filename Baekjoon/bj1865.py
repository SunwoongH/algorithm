'''
Created by sunwoong on 2022/07/23
'''
import sys
import collections

def bellman_ford(n: int, start: int) -> bool:
    distance = [sys.maxsize] * (n + 1)
    distance[start] = 0
    for i in range(n):
        for u in graph.keys():
            for v, cost in graph[u]:
                if distance[u] != sys.maxsize and distance[v] > distance[u] + cost:
                    if i == n - 1:
                        return True
                    distance[v] = distance[u] + cost
    return False

test = int(sys.stdin.readline())
for _ in range(test):
    graph = collections.defaultdict(list)
    n, m, w = map(int, sys.stdin.readline().split())
    path = False
    for _ in range(m):
        u, v, time = map(int, sys.stdin.readline().split())
        graph[u].append((v, time))
        graph[v].append((u, time))
    for _ in range(w):
        u, v, time = map(int, sys.stdin.readline().split())
        graph[u].append((v, -time))
    for u in range(1, n + 1):
        graph[0].append((u, 0))        
    print("YES") if bellman_ford(n + 1, 0) else print("NO")