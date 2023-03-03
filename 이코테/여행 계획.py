'''
Created by sunwoong on 2023/03/03
'''
import sys
input = sys.stdin.readline

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())
parent = [i for i in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
for r in range(n):
    for c in range(r + 1, n):
        if graph[r][c]:
            union(find(r), find(c))
order = list(map(int, input().split()))
check = None
is_yes = True
for node in order:
    if check is None:
        check = find(node)
        continue
    if check != find(node):
        is_yes = False
        break
print("YES") if is_yes else print("NO")