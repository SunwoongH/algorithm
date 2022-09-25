'''
Created by sunwoong on 2022/09/25
'''
import sys
import collections
from typing import List

def topology_sort() -> List[int]:
    queue = collections.deque()
    for student in range(1, n + 1):
        if indegree[student] == 0:
            queue.append(student)
    path = []
    while queue:
        student = queue.popleft()
        path.append(student)
        for adj_student in students[student]:
            indegree[adj_student] -= 1
            if indegree[adj_student] == 0:
                queue.append(adj_student)
    return path

n, m = map(int, sys.stdin.readline().split())
students = collections.defaultdict(list)
indegree = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    students[a].append(b)
    indegree[b] += 1
print(*topology_sort())