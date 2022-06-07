'''
Created by sunwoong on 2022/06/07
'''
import sys
import collections

n = int(sys.stdin.readline())
start_r, start_c, end_r, end_c = map(int, sys.stdin.readline().split())
move = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

def bfs(r: int, c: int, target_r: int, target_c: int, n: int) -> int:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[r][c] = 1
    queue = collections.deque([(r, c, 0)])
    while queue:
        r, c, count = queue.popleft()
        if r == target_r and c == target_c:
            return count
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if dr >= 0 and dr < n and dc >= 0 and dc < n and visited[dr][dc] == 0:
                visited[dr][dc] = 1
                queue.append((dr, dc, count + 1))
    return -1
print(bfs(start_r, start_c, end_r, end_c, n))