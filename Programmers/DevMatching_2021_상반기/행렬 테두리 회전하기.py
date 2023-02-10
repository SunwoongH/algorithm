'''
Created by sunwoong on 2023/02/10

풀이 시간 - 26분
'''

def lotate(start_r, start_c, end_r, end_c, board):
    temp = min_value = board[start_r][start_c]
    for r in range(start_r + 1, end_r + 1):
        board[r - 1][start_c] = board[r][start_c]
        min_value = min(min_value, board[r - 1][start_c])
    for c in range(start_c + 1, end_c + 1):
        board[end_r][c - 1] = board[end_r][c]
        min_value = min(min_value, board[end_r][c - 1])
    for r in range(end_r - 1, start_r - 1, -1):
        board[r + 1][end_c] = board[r][end_c]
        min_value = min(min_value, board[r + 1][end_c])
    for c in range(end_c - 1, start_c, -1):
        board[start_r][c + 1] = board[start_r][c]  
        min_value = min(min_value, board[start_r][c + 1])
    board[start_r][start_c + 1] = temp
    return min_value
    
def solution(rows, columns, queries):
    board = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]
    answer = []
    for query in queries:
        answer.append(lotate(query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1, board))
    return answer