'''
Created by sunwoong on 2023/02/24
'''
import sys
input = sys.stdin.readline

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal():
    edge_count = 0
    total = 0
    while edges:
        a, b, cost = edges.pop()
        parent_a = find(a)
        parent_b = find(b)
        if parent_a != parent_b:
            union(parent_a, parent_b)
            edge_count += 1
            if edge_count == n - 1:
                return total
            total += cost

n, m = map(int, input().split())
edges = []
parent = [i for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
edges.sort(key=lambda x: x[2], reverse=True)
print(kruskal())