'''
Created by sunwoong on 2022/11/10
'''
import sys

def find(a):
    while parent[a] != -1:
        a = parent[a]
    return a

def union(a, b):
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def kruskal():
    edge_count = 0
    min_cost = 0
    while edge_count < n - 1:
        cost, a, b = edges.pop()
        parent_a = find(a)
        parent_b = find(b)
        if parent_a != parent_b:
            union(parent_a, parent_b)
            min_cost += cost
            edge_count += 1
    return min_cost

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
edges = []
parent = [-1 for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))
edges.sort(reverse=True)
print(kruskal())