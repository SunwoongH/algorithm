'''
Created by sunwoong on 2025/07/22

'''
import math
from collections import defaultdict

def dfs(node, cost, sales, graph):
    cost[node][0] = 0
    cost[node][1] = sales[node]
    
    if not graph[node]:
        return
    
    extra_cost = math.inf
    for next_node in graph[node]:
        dfs(next_node, cost, sales, graph)
        if cost[next_node][0] < cost[next_node][1]:
            cost[node][0] += cost[next_node][0]
            cost[node][1] += cost[next_node][0]
            extra_cost = min(extra_cost, cost[next_node][1] - cost[next_node][0])
        else:
            cost[node][0] += cost[next_node][1]
            cost[node][1] += cost[next_node][1]
            extra_cost = 0
    cost[node][0] += extra_cost

def solution(sales, links):
    graph = defaultdict(list)
    for u, v in links:
        graph[u - 1].append(v - 1)
        
    cost = [[0, 0] for _ in range(len(sales))]
    dfs(0, cost, sales, graph)

    return min(cost[0])