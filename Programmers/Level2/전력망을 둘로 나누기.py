'''
Created by sunwoong on 2022/12/07
'''
from collections import defaultdict

def solution(n, wires):
    def dfs(curr):
        visited[curr] = True
        count = 1
        for next in graph[curr]:
            if not visited[next]:
                count += dfs(next)
        return count
    graph = defaultdict(list)
    answer = float('inf')
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    for wire in wires:
        graph[wire[0]].pop(graph[wire[0]].index(wire[1]))
        graph[wire[1]].pop(graph[wire[1]].index(wire[0]))
        visited = [False for _ in range(n + 1)]
        table = [dfs(wire[0]), dfs(wire[1])]
        answer = min(answer, abs(table[0] - table[1]))
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    return answer