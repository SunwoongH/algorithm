'''
Created by sunwoong on 2023/03/03
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[sys.maxsize for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c)
for i in range(n):
    graph[i][i] = 0
for k in range(n):
    for r in range(n):
        for c in range(n):
            graph[r][c] = min(graph[r][c], graph[r][k] + graph[k][c])
for r in range(n):
    for c in range(n):
        if graph[r][c] == sys.maxsize:
            print(0, end=' ')
        else:
            print(graph[r][c], end=' ')
    print()