'''
Created by sunwoong on 2022/06/01
'''
import sys
import collections

move = [(-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, 2), (2, 1), (2, -1), (1, -2)]

def bfs(start_r: int, start_c: int, end_r: int, end_c: int, n: int) -> int:
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[start_r][start_c] = True
    queue = collections.deque([(start_r, start_c, 0)])
    while queue:
        r, c, cnt = queue.popleft()
        if r == end_r and c == end_c:
            break
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if dr >= 0 and dr < n and dc >= 0 and dc < n and not visited[dr][dc]:
                visited[dr][dc] = True
                queue.append((dr, dc, cnt + 1))
    return cnt

test = int(sys.stdin.readline())
for _ in range(test):
    n = int(sys.stdin.readline())
    start_r, start_c = map(int, sys.stdin.readline().split())
    end_r, end_c = map(int, sys.stdin.readline().split())
    print(bfs(start_r, start_c, end_r, end_c, n))