'''
Created by sunwoong on 2022/09/21

풀이 시간 - 120분
'''
import sys

def solution(n, s, a, b, fares):
    graph = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0
    for u, v, cost in fares:
        graph[u][v] = cost
        graph[v][u] = cost
    for k in range(1, n + 1):
        for r in range(1, n + 1):
            for c in range(1, n + 1):
                graph[r][c] = min(graph[r][c], graph[r][k] + graph[k][c])          
    return min([graph[s][k] + graph[k][a] + graph[k][b] for k in range(1, n + 1)])