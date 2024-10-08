'''
Created by sunwoong on 2024/10/08
'''

def insert(start_r, start_c, key, board):
    for r in range(len(key)):
        for c in range(len(key)):
            board[start_r + r][start_c + c] += key[r][c]

def delete(start_r, start_c, key, board):
    for r in range(len(key)):
        for c in range(len(key)):
            board[start_r + r][start_c + c] -= key[r][c]

def rotate(size, origin, temp):
    for r in range(size):
        for c in range(size):
            temp[r][c] = origin[c][size - 1 - r]
    for r in range(size):
        for c in range(size):
            origin[r][c] = temp[r][c]
            
def check(start_r, start_c, size, board):
    is_valid = True
    for r in range(start_r, start_r + size):
        for c in range(start_c, start_c + size):
            if board[r][c] != 1:
                is_valid = False
                return is_valid
    return is_valid
                
def solution(key, lock):
    answer = False
    
    board = [[0 for _ in range(len(key) * 2 + len(lock))] for _ in range(len(key) * 2 + len(lock))]
    temp = [[0 for _ in range(len(key))] for _ in range(len(key))]
    
    for r in range(len(key), len(key) + len(lock)):
        for c in range(len(key), len(key) + len(lock)):
            board[r][c] = lock[r - len(key)][c - len(key)]
            
    for r in range(1, len(key) + len(lock)):
        for c in range(1, len(key) + len(lock)):
            for _ in range(4):
                rotate(len(key), key, temp)
                insert(r, c, key, board)
                answer = check(len(key), len(key), len(lock), board)
                if answer:
                    return answer
                delete(r, c, key, board)

    return answer
