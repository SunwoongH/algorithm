'''
Created by sunwoong on 2022/06/13
'''
import sys
import collections

def bfs(r: int, c: int, n: int) -> None:
    move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    visited[r][c] = 0
    queue = collections.deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if dr > 0 and dr <= n and dc > 0 and dc <= n and visited[dr][dc] == -1:
                visited[dr][dc] = visited[r][c] + 1
                queue.append((dr, dc))

n, m = map(int, sys.stdin.readline().split())
start_r, start_c = map(int, sys.stdin.readline().split())
visited = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
bfs(start_r, start_c, n)
result = []
for _ in range(m):
    target_r, target_c = map(int, sys.stdin.readline().split())
    result.append(visited[target_r][target_c])
print(*result)