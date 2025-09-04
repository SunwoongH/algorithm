'''
Created by sunwoong on 2025/09/04
'''
import sys
sys.setrecursionlimit(10 ** 6)

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if count[a] < count[b]:
        parent[b] = a
    else:
        parent[a] = b

n, m, k = map(int, sys.stdin.readline().split())
count = [0] + list(map(int, sys.stdin.readline().split()))
ban = set()
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    ban.add((min(s, e), max(s, e)))
parent = [i for i in range(n + 1)]

for i in range(1, n):
    if (i, i + 1) not in ban:
        union(i, i + 1)
if (1, n) not in ban:
    union(1, n)

result = 0
total = 0
for i in range(1, n + 1):
    if parent[i] == i:
        result += 1
        total += count[i]

if result == 1:
    print('YES')
elif total <= k:
    print('YES')
else:
    print('NO')