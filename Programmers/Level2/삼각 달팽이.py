'''
Created by sunwoong on 2024/03/04

풀이 시간 - 60분
'''

def solution(n):
    board = [[0] * (i + 1) for i in range(n)]
    move = [(1, 0), (0, 1), (-1, -1)]
    number = 1
    r, c = -1, 0
    pos = 0
    for i in range(n):
        for _ in range(i, n):
            r, c = r + move[pos][0], c + move[pos][1]
            board[r][c] = number
            number += 1
        pos = (pos + 1) % len(move)
    return [board[r][c] for r in range(n) for c in range(r + 1)]