'''
Created by sunwoong on 2023/05/30
'''
import sys
input = sys.stdin.readline

parent = None

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(parent_a, parent_b):
    if parent_a < parent_b:
        if parent_b in seen:
            parent[parent_a] = parent_b
        else:
            parent[parent_b] = parent_a
    else:
        if parent_a in seen:
            parent[parent_b] = parent_a
        else:
            parent[parent_a] = parent_b

def kruskal(edges):
    total = 0
    while edges:
        a, b, cost = edges.pop()
        parent_a = find(a)
        parent_b = find(b)
        if (parent_a != parent_b) and not (parent_a in seen and parent_b in seen):
            union(parent_a, parent_b)
            total += cost
    return total

n, m, k = map(int, input().split())
edges = []
seen = set(map(int, input().split()))
parent = [i for i in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))
edges.sort(key=lambda x: x[2], reverse=True)
print(kruskal(edges))