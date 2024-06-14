'''
Created by sunwoong on 2024/06/14

풀이 시간 - 90분
'''
from collections import defaultdict

def find(seen, count, start, graph, route):
    is_route = False
    for end in graph[start]:
        ticket = (start, end)
        if seen[ticket] > 0:
            seen[ticket] -= 1
            is_route = find(seen, count - 1, end, graph, route)
            seen[ticket] += 1
        if is_route:
            route.append(start)
            break
    if count == 0:
        route.append(start)
        return True
    return is_route
            
def solution(tickets):
    count = len(tickets)
    start = 'ICN'
    seen = defaultdict(int)
    graph = defaultdict(list)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        seen[(ticket[0], ticket[1])] += 1
    for key in graph.keys():
        graph[key].sort()
    route = []
    find(seen, count, start, graph, route)
    route.reverse()
    return route