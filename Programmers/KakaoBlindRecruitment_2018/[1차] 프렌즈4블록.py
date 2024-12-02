'''
Created by sunwoong on 2024/12/02

'''
def check(m, n, board, remover):
    for r in range(m - 1):
        for c in range(n - 1):
            target = board[r][c]
            if target == "":
                continue
            is_valid = True
            for i in range(2):
                for j in range(2):
                    if board[r + i][c + j] != target:
                        is_valid = False
                        break
                if not is_valid:
                    break
            if is_valid:
                for i in range(2):
                    for j in range(2):
                        remover[r + i][c + j] = 1
                        
def counting(m, n, board, remover):
    count = 0
    for r in range(m):
        for c in range(n):
            if remover[r][c] == 1:
                count += 1
                remover[r][c] = 0
                board[r][c] = ""
    return count

def rebuilding(m, n, board):
    for c in range(n):
        for r in range(m - 1, 0, -1):
            if board[r][c] == "":
                for k in range(r - 1, -1, -1):
                    if board[k][c] != "":
                        board[r][c], board[k][c] = board[k][c], board[r][c]
                        break

def solution(m, n, board):
    answer = 0
    board = [list(line) for line in board]
    remover = [[0 for _ in range(n)] for _ in range(m)]
    
    while True:
        check(m, n, board, remover)

        count = counting(m, n, board, remover)
        if count == 0:
            return answer
        answer += count

        rebuilding(m, n, board)