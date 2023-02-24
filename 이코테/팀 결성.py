'''
Created by sunwoong on 2023/02/24
'''
import sys
input = sys.stdin.readline

def find(a):
    if team[a] != a:
        team[a] = find(team[a])
    return team[a]

def union(a, b):
    if a < b:
        team[b] = a
    else:
        team[a] = b

n, m = map(int, input().split())
team = [i for i in range(n + 1)]
for _ in range(m):
    order, a, b = map(int, input().split())
    if order == 0:
        union(find(a), find(b))
    else:
        print("NO") if find(a) != find(b) else print("YES")