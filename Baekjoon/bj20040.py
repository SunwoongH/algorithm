'''
Created by sunwoong on 2023/06/10
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
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

n, m = map(int, input().split())
parent = [i for i in range(n)]
sequence = None
for i in range(1, m + 1):
    a, b = map(int, input().split())
    if sequence is not None:
        continue
    parent_a = find(a)
    parent_b = find(b)
    if parent_a == parent_b:
        sequence = i
        continue
    union(parent_a, parent_b)
print(sequence) if sequence is not None else print(0)