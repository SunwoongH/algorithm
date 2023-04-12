'''
Created by sunwoong on 2023/04/12
'''
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def topology_sort():
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            time[i] = cost[i]
            queue.append(i)
    while queue:
        curr = queue.popleft()
        for next in graph[curr]:
            indegree[next] -= 1
            time[next] = max(time[next], time[curr] + cost[next])
            if indegree[next] == 0:
                queue.append(next)

n = int(input())
time = [0 for _ in range(n + 1)]
cost = [0 for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
graph = defaultdict(list)
for i in range(n):
    data = list(map(int, input().split()))
    cost[i + 1] = data[0]
    for j in range(1, len(data) - 1):
        graph[data[j]].append(i + 1)
        indegree[i + 1] += 1
topology_sort()
for i in range(1, n + 1):
    print(time[i])