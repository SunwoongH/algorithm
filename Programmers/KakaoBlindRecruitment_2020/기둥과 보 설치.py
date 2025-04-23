'''
Created by sunwoong on 2025/04/23
'''

def is_promising(c, r, a, board):
    if a == 0:
        if r == 0:
            return True
        if board[r][c][2] or board[r][c][3]:
            return True
        if board[r][c][0]:
            return True
    else:
        if board[r][c][0] or board[r][c + 1][0]:
            return True
        if board[r][c][2] and board[r][c + 1][3]:
            return True
    return False

def solution(n, build_frame):
    board = [[[0, 0, 0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    seen = set()
    
    for frame in build_frame:
        c, r, a, b = frame
        if b == 1:
            promising = is_promising(c, r, a, board)
            if promising:
                if a == 0:
                    board[r][c][1] = 1
                    board[r + 1][c][0] = 1
                    seen.add((c, r, 0))
                else:
                    board[r][c][3] = 1
                    board[r][c + 1][2] = 1
                    seen.add((c, r, 1))
        else:
            if a == 0:
                board[r][c][1] = 0
                board[r + 1][c][0] = 0
                seen.remove((c, r, 0))
            else:
                board[r][c][3] = 0
                board[r][c + 1][2] = 0
                seen.remove((c, r, 1))
            for item in seen:
                promising = is_promising(item[0], item[1], item[2], board)
                if not promising:
                    if a == 0:
                        board[r][c][1] = 1
                        board[r + 1][c][0] = 1
                        seen.add((c, r, 0))
                    else:
                        board[r][c][3] = 1
                        board[r][c + 1][2] = 1
                        seen.add((c, r, 1))
                    break
    
    return sorted(seen)