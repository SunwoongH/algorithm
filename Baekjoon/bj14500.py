'''
Created by sunwoong on 2022/10/16
'''
import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cases = [((0, 0), (0, 1), (0, 2), (0, 3)), ((0, 0), (1, 0), (2, 0), (3, 0)),
        ((0, 0), (0, 1), (1, 0), (1, 1)),
        ((0, 0), (1, 0), (2, 0), (2, 1)), ((0, 0), (1, 0), (2, 0), (2, -1)),
        ((0, 0), (0, 1), (0, 2), (-1, 2)), ((0, 0), (0, 1), (0, 2), (1, 2)),
        ((0, 0), (0, 1), (1, 0), (2, 0)), ((0, 0), (0, 1), (1, 1), (2, 1)),
        ((0, 0), (1, 0), (1, 1), (1, 2)), ((0, 0), (1, 0), (0, 1), (0, 2)),
        ((0, 0), (1, 0), (1, 1), (2, 1)), ((0, 0), (1, 0), (1, -1), (2, -1)),
        ((0, 0), (0, 1), (-1, 1), (-1, 2)), ((0, 0), (0, 1), (1, 1), (1, 2)),
        ((0, 0), (0, 1), (0, 2), (1, 1)), ((0, 0), (0, 1), (-1, 1), (0, 2)),
        ((0, 0), (1, 0), (2, 0), (1, 1)), ((0, 0), (0, 1), (-1, 1), (1, 1))]

result = -sys.maxsize
for r in range(n):
    for c in range(m):
        for case in cases:
            is_promising = True
            value = 0
            for oper in case:
                dr = r + oper[0]
                dc = c + oper[1]
                if dr < 0 or dr >= n or dc < 0 or dc >= m:
                    is_promising = False
                    break
                value += board[dr][dc]
            if is_promising:
                result = max(result, value)
print(result)