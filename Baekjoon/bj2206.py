'''
Created by sunwoong on 2022/07/04
'''
import sys
import collections

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

def bfs(start_r: int, start_c: int, end_r: int, end_c: int) -> int:
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
    is_origin = 1
    visited[start_r][start_c][is_origin] = 1
    queue = collections.deque([(start_r, start_c, is_origin)])
    while queue:
        r, c, is_origin = queue.popleft()
        if r == end_r and c == end_c:
            return visited[r][c][is_origin]
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if dr >= 0 and dr < n and dc >= 0 and dc < m:
                if board[dr][dc] == 0 and visited[dr][dc][is_origin] == 0:
                    visited[dr][dc][is_origin] = visited[r][c][is_origin] + 1
                    queue.append((dr, dc, is_origin))
                elif board[dr][dc] == 1 and is_origin == 1:
                    visited[dr][dc][0] = visited[r][c][is_origin] + 1
                    queue.append((dr, dc, 0))
    return -1
print(bfs(0, 0, n - 1, m - 1))