'''
Created by sunwoong on 2022/10/24
'''
import sys
from collections import defaultdict, deque
from typing import List, Tuple

def topology_sort() -> Tuple[bool, List[int]]:
    sequence = []
    visited = [False for _ in range(n + 1)]
    queue = deque()
    for i in range(1, n + 1):
        if not indegree[i]:
            queue.append(i)
    while queue:
        singer = queue.popleft()
        visited[singer] = True
        sequence.append(singer)
        for adj_singer in graph[singer]:
            indegree[adj_singer] -= 1
            if not indegree[adj_singer]:
                queue.append(adj_singer)
    return all(visited[1:]), sequence

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
indegree = [0 for _ in range(n + 1)]
for _ in range(m):
    length, *singers = map(int, sys.stdin.readline().split())
    prev = singers[0]
    for i in range(1, length):
        if singers[i] not in graph[prev]:
            graph[prev].append(singers[i])
            indegree[singers[i]] += 1
        prev = singers[i]
is_promising, result = topology_sort()
print(*result, sep='\n') if is_promising else print(0)