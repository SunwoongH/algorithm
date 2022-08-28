'''
Created by sunwoong on 2022/08/28
'''
import sys
import heapq

edges = []
n, m = map(int, sys.stdin.readline().split())
for _ in range(m):
    u, v, cost = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (cost, u, v))
    
parent = [-1 for _ in range(n + 1)]

def find(child: int) -> int:
    while parent[child] != -1:
        child = parent[child]
    return child

def union(u_parent: int, v_parent: int) -> None:
    if u_parent > v_parent:
        parent[u_parent] = v_parent
    else:
        parent[v_parent] = u_parent

def kruskal() -> int:
    result = 0
    edge = 0
    while edge < n - 1:
        cost, u, v = heapq.heappop(edges)
        u_parent = find(u)
        v_parent = find(v)
        if u_parent != v_parent:
            union(u_parent, v_parent)
            edge += 1
            if edge == n - 1:
                continue
            result += cost     
    return result
print(kruskal())