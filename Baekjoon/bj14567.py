'''
Created by sunwoong on 2022/09/23
'''
import sys
import collections
from typing import List

def topology_sort() -> List[int]:
    queue = collections.deque()
    minimum_term = [None for _ in range(n + 1)]
    for subject in range(1, n + 1):
        if indegree[subject] == 0:
            queue.append((subject, 1))
    while queue:
        subject, term = queue.popleft()
        minimum_term[subject] = term
        for adj_subject in subjects[subject]:
            indegree[adj_subject] -= 1
            if indegree[adj_subject] == 0:
                queue.append((adj_subject, term + 1))
    return minimum_term

n, m = map(int, sys.stdin.readline().split())
subjects = collections.defaultdict(list)
indegree = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    subjects[a].append(b)
    indegree[b] += 1
minimum_term = topology_sort()
print(*minimum_term[1:])