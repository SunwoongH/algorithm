'''
Created by sunwoong on 2022/12/27
'''
import sys
input = sys.stdin.readline

SMALL = -1
BIG = 1
UNKNOWN = 0

def update():
    for k in range(n):
        for r in range(n):
            for c in range(n):
                if graph[r][c] == UNKNOWN:
                    if graph[r][k] == graph[k][c]:
                        graph[r][c] = graph[r][k]

def calculate():
    answer = 0
    for c in range(n):
        count = 0
        for r in range(n):
            if graph[r][c] == UNKNOWN:
                count += 1
        if count == 1:
            answer += 1
    return answer

n, m = map(int, input().split())
graph = [[UNKNOWN for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = SMALL
    graph[b - 1][a - 1] = BIG
update()
print(calculate())