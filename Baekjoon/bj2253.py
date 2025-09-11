'''
Created by sunwoong on 2025/09/11
'''
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
ban = set()
for _ in range(m):
    rock = int(sys.stdin.readline())
    ban.add(rock)

if 2 in ban:
    print(-1)
    exit()

maximum = int((n * 2) ** 0.5) + 2
visited = [[False for _ in range(maximum)] for _ in range(n + 1)]

def bfs(start):
    queue = deque([(start, 1, 1)])
    visited[start][1] = True

    while queue:
        node, step, count = queue.popleft()

        if node == n:
            print(count)
            return

        for jump in [step - 1, step, step + 1]:
            if node < node + jump <= n:
                if node + jump not in ban:
                    if not visited[node + jump][jump]:
                        visited[node + jump][jump] = True
                        queue.append((node + jump, jump, count + 1))

    print(-1)

bfs(2)