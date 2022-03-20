'''
Created by sunwoong on 2022/03/20

>>> 어제 풀었던 스도쿠 문제와 거의 동일한 문제이다. Python3로 통과하였으며 시간 초과가 났던 코드를 최적화한 풀이이다.
promising한 number를 찾는 과정이 시간 초과가 발생한 주요한 이유였고 값을 제거해서 promising한 number를 찾는 것이 아닌
행, 열, 3 * 3 사각형에 해당하는 number table을 미리 만들어 bool 값으로 promising한 number를 확인하는 방식이다.
row, column, square의 의미는 각각 현재 같은 행, 열, 3 * 3 사각형내에 number가 존재하는지의 여부이다.
'''
import sys

board = [list(map(int, list(sys.stdin.readline().rstrip('\n')))) for _ in range(9)]
row = [[False for _ in range(10)] for _ in range(9)]
column = [[False for _ in range(10)] for _ in range(9)]
square = [[False for _ in range(10)] for _ in range(9)]
missing = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            missing.append((i, j))
        else:
            row[i][board[i][j]] = column[j][board[i][j]] = square[(i // 3) * 3 + (j // 3)][board[i][j]] = True

def solve(start: int) -> None:
    if start == len(missing):
        for line in board:
            print(''.join(map(str, line)))
        sys.exit(0)
    r, c = missing[start]
    for num in range(1, 10):
        if not row[r][num] and not column[c][num] and not square[(r // 3) * 3 + (c // 3)][num]:
            row[r][num] = column[c][num] = square[(r // 3) * 3 + (c // 3)][num] = True
            board[r][c] = num
            solve(start + 1)
            row[r][num] = column[c][num] = square[(r // 3) * 3 + (c // 3)][num] = False
            board[r][c] = 0
solve(0)