'''
Created by sunwoong on 2022/08/11
'''
import sys
from typing import List
import collections

def is_bingo(board: List[int], n: int):
    count = 0
    diagonal_right = []
    diagonal_left = []
    for horizontal in board:
        if not any(horizontal):
            count += 1
    for vertical in zip(*board):
        if not any(vertical):
            count += 1
    for r in range(n):
        diagonal_right.append(board[r][r])
        diagonal_left.append(board[r][n - r - 1])
    if not any(diagonal_right):
        count += 1
    if not any(diagonal_left):
        count += 1
    if count >= 3:
        return True
    return False

board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
order = collections.deque()
for _ in range(5):
    nums = list(map(int, sys.stdin.readline().split()))
    order.extend(nums)
start = 0
bingo = False
while order:
    num = order.popleft()
    start += 1
    for r in range(5):
        for c in range(5):
            if board[r][c] == num:
                board[r][c] = 0
                if start >= 12 and is_bingo(board, 5):
                    bingo = True
                    break
        if bingo:
            break
    if bingo:
        print(start)
        break