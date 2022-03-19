'''
Created by sunwoong on 2022/03/19

>>> 스도쿠 풀이 문제로 상당히 어려웠다. 또한 Python3는 시간 초과가 발생했고 PyPy3로만 통과되었다.
파이썬은 다른 언어에 비해 시간이 오래 걸리는 언어적 특성 때문에 최적화 방법에 대해 더욱 고민해야 하는 것 같다.
풀이는 찾고자 하는 위치(0)의 행, 열, 3 * 3 정사각형을 각각 탐색하여 promising 한 number를 찾아 순차적으로
값을 넣은 후 정답 여부를 재귀적으로 확인하는 풀이이다.
'''
from typing import List
import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
missing = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

def promising(r: int, c: int) -> List[int]:
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for k in range(9):
        if board[r][k] != 0:
            num.remove(board[r][k])
    for k in range(9):
        if board[k][c] in num:
            num.remove(board[k][c])
    for i in range((r // 3) * 3, (r // 3) * 3 + 3):
        for j in range((c // 3) * 3, (c // 3) * 3 + 3):
            if board[i][j] in num:
                num.remove(board[i][j])
    return num

def solve(start: int) -> None:
    if start == len(missing):
        for line in board:
            print(*line)
        sys.exit(0)
    r, c = missing[start]
    number = promising(r, c)
    for num in number:
        board[r][c] = num
        solve(start + 1)
        board[r][c] = 0
solve(0)