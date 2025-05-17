'''
Created by sunwoong on 2025/05/17
'''

move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def is_finished(board, r, c):
    for oper in move:
        dr = r + oper[0]
        dc = c + oper[1]
        if 0 <= dr < len(board) and 0 <= dc < len(board[0]) and board[dr][dc]:
            return False
    return True

def dfs(board, cr, cc, nr, nc):
    if is_finished(board, cr, cc):
        return [False, 0]
    if cr == nr and cc == nc:
        return [True, 1]
    
    max_turn = 0
    min_turn = int(1e9)
    winner = False
    
    for oper in move:
        dr = cr + oper[0]
        dc = cc + oper[1]
        if dr < 0 or dr >= len(board) or dc < 0 or dc >= len(board[0]) or not board[dr][dc]:
            continue
        board[cr][cc] = 0
        result = dfs(board, nr, nc, dr, dc)
        board[cr][cc] = 1
        
        if not result[0]:
            winner = True
            min_turn = min(min_turn, result[1])
        elif not winner:
            max_turn = max(max_turn, result[1])
    
    turn = min_turn if winner else max_turn
    
    return [winner, turn + 1]

def solution(board, aloc, bloc):
    return dfs(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]