'''
Created by sunwoong on 2024/07/05

풀이 시간 - 해설 참조
'''
def solution(board, skill):
    answer = 0
    reflaction = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    for data in skill:
        type, r1, c1, r2, c2, degree = data
        if type == 1:
            reflaction[r1][c1] -= degree
            if c2 + 1 < len(board[0]):
                reflaction[r1][c2 + 1] += degree
            if r2 + 1 < len(board):
                reflaction[r2 + 1][c1] += degree
            if c2 + 1 < len(board[0]) and r2 + 1 < len(board):
                reflaction[r2 + 1][c2 + 1] -= degree
        else:
            reflaction[r1][c1] += degree
            if c2 + 1 < len(board[0]):
                reflaction[r1][c2 + 1] -= degree
            if r2 + 1 < len(board):
                reflaction[r2 + 1][c1] -= degree
            if c2 + 1 < len(board[0]) and r2 + 1 < len(board):
                reflaction[r2 + 1][c2 + 1] += degree
    for r in range(len(board)):
        for c in range(len(board[0]) - 1):
            reflaction[r][c + 1] += reflaction[r][c]
    for c in range(len(board[0])):
        for r in range(len(board) - 1):
            reflaction[r + 1][c] += reflaction[r][c]
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] + reflaction[r][c] > 0:
                answer += 1
    return answer