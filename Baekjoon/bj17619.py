'''
Created by sunwoong on 2025/09/02
'''
import sys

parent = []

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

n, q = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]
items = []
for i in range(n):
    x1, x2, _ = map(int, sys.stdin.readline().split())
    items.append((x1, x2, i + 1))
items.sort()
longest = items[0]
for i in range(1, n):
    s, e, p = items[i]
    if s <= longest[1]:
        union(longest[2], p)
    if longest[1] < e:
        longest = items[i]
order = []
for i in range(q):
    a, b = map(int, sys.stdin.readline().split())
    order.append((a, b))
for i in range(q):
    a, b = order[i]
    if find(a) == find(b):
        print(1)
    else:
        print(0)