'''
Created by sunwoong on 2024/02/15

풀이 시간 - 200분
'''
diagonal_a = [(-1, 1), (1, -1)]
diagonal_b = [(1, 1), (-1, -1)]

def check(board, char):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c] == char:
                count += 1
        if count == 3:
            return True
    for r in range(3):
        count = 0
        for c in range(3):
            if board[c][r] == char:
                count += 1
        if count == 3:
            return True
    count = 0
    for r in range(3):
        if board[r][r] == char:
            count += 1
    if count == 3:
        return True
    count = 0
    for r in range(3):
        if board[r][2 - r] == char:
            count += 1
    if count == 3:
        return True
    return False

def solution(board):
    o_count = 0
    x_count = 0
    for r in range(3):
        for c in range(3):
            if board[r][c] == 'O':
                o_count += 1
            elif board[r][c] == 'X':
                x_count += 1
    if o_count > x_count + 1:
        return 0
    elif o_count == x_count + 1:
        if check(board, 'X'):
            return 0
    elif o_count == x_count:
        if check(board, 'O'):
            return 0
    elif o_count < x_count:
        return 0
    return 1