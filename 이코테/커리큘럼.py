'''
Created by sunwoong on 2023/02/24
'''
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
time = [0 for _ in range(n + 1)]
time_table = [0 for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
graph = defaultdict(list)
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for j in range(1, len(data) - 1):
        graph[data[j]].append(i)
        indegree[i] += 1

def topology_sort():
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            time_table[i] = time[i]
            queue.append(i)
    while queue:
        curr = queue.popleft()
        for next in graph[curr]:
            time_table[next] = max(time_table[next], time_table[curr] + time[next])
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)

topology_sort()
print(*time_table[1:], sep='\n')