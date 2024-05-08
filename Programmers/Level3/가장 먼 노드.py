'''
Created by sunwoong on 2024/05/08

풀이 시간 - 20분
'''
from collections import defaultdict, deque

def calculate_minimum_distance(n, start, graph):
    minimum_distance = []
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    queue = deque([(start, 0)])
    while queue:
        node, distance = queue.popleft()
        minimum_distance.append(distance)
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, distance + 1))
    return minimum_distance

def solution(n, edge):
    graph = defaultdict(list)
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    distance = calculate_minimum_distance(n, 1, graph)
    distance.sort(reverse=True)
    target = distance[0]
    return distance.count(target)