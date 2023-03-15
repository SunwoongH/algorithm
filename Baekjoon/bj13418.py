'''
Created by sunwoong on 2023/03/15
'''
import sys
input = sys.stdin.readline

parent = None

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal(choice):
    global parent
    parent = [i for i in range(n + 1)]
    edges.sort(key=lambda x: x[2], reverse=choice)
    edge_count = 0
    cost = 0
    for i in range(len(edges)):
        a, b, c = edges[i]
        parent_a = find(a)
        parent_b = find(b)
        if parent_a != parent_b:
            union(parent_a, parent_b)
            edge_count += 1
            cost += 1 if c == 0 else 0
        if edge_count == n:
            break
    return pow(cost, 2)

n, m = map(int, input().split())
edges = []
for _ in range(m + 1):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
print(kruskal(False) - kruskal(True))