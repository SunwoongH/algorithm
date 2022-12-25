'''
Created by sunwoong on 2022/12/25
'''
WIN = 1
LOSE = -1
UNKNOWN = 0

def update(n, graph):
    for k in range(n):
        for r in range(n):
            for c in range(n):
                if graph[r][c] == UNKNOWN:
                    choice = graph[r][k] + graph[k][c]
                    if choice == 2:
                        graph[r][c] = WIN
                    elif choice == -2:
                        graph[r][c] = LOSE
               
def solution(n, results):
    graph = [[UNKNOWN for _ in range(n)] for _ in range(n)]
    for r, c in results:
        graph[r - 1][c - 1] = WIN
        graph[c - 1][r - 1] = LOSE
    update(n, graph)
    answer = 0
    for c in range(n):
        count = 0
        for r in range(n):
            if graph[r][c] == UNKNOWN:
                count += 1
        if count == 1:
            answer += 1
    return answer