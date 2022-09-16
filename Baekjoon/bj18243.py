'''
Created by sunwoong on 2022/09/16
'''
import sys

def floyd():
    for k in range(n):
        for r in range(n):
            for c in range(n):
                graph[r][c] = min(graph[r][c], graph[r][k] + graph[k][c])

def check():
    is_possible = True
    for r in range(n):
        for c in range(n):
            if graph[r][c] == sys.maxsize or graph[r][c] > 6:
                is_possible = False
                break
    return is_possible

n, k = map(int, sys.stdin.readline().split())
graph = [[sys.maxsize for _ in range(n)] for _ in range(n)]
for r in range(n):
    for c in range(n):
        if r == c:
            graph[r][c] = 0
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

floyd()
print("Small World!") if check() else print("Big World!")