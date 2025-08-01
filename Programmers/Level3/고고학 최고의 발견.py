'''
Created by sunwoong on 2025/08/01
'''

from itertools import product

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def rotate(board, r, c, n):
    board[r][c] = (board[r][c] + n) % 4
    for oper in move:
        dr = r + oper[0]
        dc = c + oper[1]
        if 0 <= dr < len(board) and 0 <= dc < len(board):
            board[dr][dc] = (board[dr][dc] + n) % 4

def solution(clockHands):
    board = None
    answer = int(1e9)

    for case in product(range(0, 4), repeat=len(clockHands)):
        count = 0
        board = [r[:] for r in clockHands]
        
        for c in range(len(board)):
            rotate(board, 0, c, case[c])
            count += case[c]
        
        for r in range(1, len(board)):
            for c in range(len(board)):
                if board[r - 1][c] == 0:
                    continue
                rotate_count = 4 - board[r - 1][c]
                rotate(board, r, c, rotate_count)
                count += rotate_count
        
        if any(board[len(board) - 1]):
            continue
        
        answer = min(answer, count)
                
    return answer