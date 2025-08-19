'''
Created by sunwoong on 2025/08/19
'''
import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10 ** 6)

parent = None

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, sys.stdin.readline().split())
s, e = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
parent = [i for i in range(n + 1)]

edges.sort(key=lambda x: x[2])
count = 0

while edges and count < n - 1:
    u, v, cost = edges.pop()
    u_parent = find(u)
    v_parent = find(v)

    if u_parent != v_parent:
        union(u, v)
        graph[u].append((v, cost))
        graph[v].append((u, cost))
        count += 1

visited = [False for _ in range(n + 1)]
queue = deque([(s, int(1e9))])
visited[s] = True

while queue:
    node, cost = queue.popleft()
    
    if node == e:
        print(cost)
        exit()
    
    for next_node, next_cost in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            queue.append((next_node, min(cost, next_cost)))

print(0)