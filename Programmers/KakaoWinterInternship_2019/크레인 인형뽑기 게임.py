'''
Created by sunwoong on 2023/03/26

풀이 시간 - 20분
'''

def draw_a_doll(pos, board):
    for r in range(len(board)):
        if board[r][pos] != 0:
            doll = board[r][pos]
            board[r][pos] = 0
            return doll
    return None

def solution(board, moves):
    basket = []
    answer = 0
    for move in moves:
        doll = draw_a_doll(move - 1, board)
        if doll is None:
            continue
        if basket:
            if basket[-1] == doll:
                basket.pop()
                answer += 2
                continue
        basket.append(doll)
    return answer