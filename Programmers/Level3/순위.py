'''
Created by sunwoong on 2024/05/09

풀이 시간 - 50분
'''
from collections import defaultdict, deque

def bfs(n, start, graph, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

def is_promising(n, start, graph, end):
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == end:
            return True
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
    return False

def solution(n, results):
    graph = defaultdict(list)
    for winner, loser in results:
        graph[loser].append(winner)
    answer = 0
    for i in range(1, n + 1):
        visited = [False for _ in range(n + 1)]
        bfs(n, i, graph, visited)
        available = True
        for j in range(1, n + 1):
            if not visited[j] and j != i:
                if not is_promising(n, j, graph, i):
                    available = False
                    break
        if available:
            answer += 1
    return answer

def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for winner, loser in results:
        win[loser].add(winner)
        lose[winner].add(loser)
    for player in range(1, n + 1):
        for winner in win[player]:
            lose[winner].update(lose[player])
        for loser in lose[player]:
            win[loser].update(win[player])
    for player in range(1, n + 1):
        if len(win[player]) + len(lose[player]) == n - 1:
            answer += 1
    return answer

def solution(n, results):
    answer = 0
    graph = [[None for _ in range(n + 1)] for _ in range(n + 1)]
    for winner, loser in results:
        graph[winner][loser] = "win"
        graph[loser][winner] = "lose"
    for i in range(1, n + 1):
        graph[i][i] = "self"
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] == "win" and graph[k][j] == "win":
                    graph[i][j] = "win"
                elif graph[i][k] == "lose" and graph[k][j] == "lose":
                    graph[i][j] = "lose"
    for i in range(1, n + 1):
        is_promising = True
        for j in range(1, n + 1):
            if not graph[i][j]:
                is_promising = False
                break
        if is_promising:
            answer += 1
    return answer