'''
Created by sunwoong on 2022/10/18
'''
import sys
import collections

def bfs(start: int):
    queue = collections.deque([(start, 0)])
    visited = [False for _ in range(SIZE * SIZE + 1)]
    visited[start] = True
    while queue:
        position, count = queue.popleft()
        if position == SIZE * SIZE:
            return count
        for oper in move:
            dp = position + oper
            if 0 < dp <= SIZE * SIZE and not visited[dp]:
                if event[dp]:
                    if not visited[event[dp]]:
                        visited[event[dp]] = True
                        queue.append((event[dp], count + 1))
                else:
                    visited[dp] = True
                    queue.append((dp, count + 1))
                    
SIZE = 10
move = [1, 2, 3, 4, 5, 6]
event = collections.defaultdict(int)
n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    event[start] = end
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    event[start] = end
print(bfs(1))