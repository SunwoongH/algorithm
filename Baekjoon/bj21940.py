'''
Created by sunwoong on 2023/05/31
'''
import sys
input = sys.stdin.readline

def floyd():
    for k in range(1, n + 1):
        for r in range(1, n + 1):
            for c in range(1, n + 1):
                graph[r][c] = min(graph[r][c], graph[r][k] + graph[k][c])

def calculate_optimize_cost(target_city):
    optimize_cost = 0
    for city in citys:
        optimize_cost = max(optimize_cost, graph[city][target_city] + graph[target_city][city])
    return optimize_cost

def find_optimize_city():
    optimize_cost = sys.maxsize
    optimize_city = []
    for i in range(1, n + 1):
        temp = calculate_optimize_cost(i)
        if temp >= sys.maxsize:
            continue
        if optimize_cost > temp:
            optimize_cost = temp
            optimize_city = [i]
        elif optimize_cost == temp:
            optimize_city.append(i)
    optimize_city.sort()
    return optimize_city

n, m = map(int, input().split())
graph = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b, time = map(int, input().split())
    graph[a][b] = time
for i in range(1, n + 1):
    graph[i][i] = 0
k = int(input())
citys = list(map(int, input().split()))
floyd()
print(*find_optimize_city())