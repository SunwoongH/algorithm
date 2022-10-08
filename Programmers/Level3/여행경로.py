'''
Created by sunwoong on 2022/10/08
'''
from collections import defaultdict, deque

def solution(tickets):
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    for airport in graph.keys():
        graph[airport].sort(reverse=True)
    answer = deque()
    def dfs(curr):
        while graph[curr]:
            next = graph[curr].pop()
            dfs(next)
        answer.appendleft(curr)
    dfs('ICN')
    return list(answer)