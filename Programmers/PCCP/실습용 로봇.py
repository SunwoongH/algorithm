'''
Created by sunwoong on 2024/07/23
'''
direct = ['T', 'R', 'B', 'L']
go_move = {'T': [0, 1], 'R': [1, 0], 'B': [0, -1], 'L': [-1, 0]}
back_move = {'T': [0, -1], 'R': [-1, 0], 'B': [0, 1], 'L': [1, 0]}

def solution(command):
    pos = [0, 0]
    d = 0
    for c in command:
        if c == 'R':
            d = (d + 1) % len(direct)
        elif c == 'L':
            d = (d - 1 + len(direct)) % len(direct)
        elif c == 'G':
            oper = go_move[direct[d]]
            pos[0] += oper[0]
            pos[1] += oper[1]
        else:
            oper = back_move[direct[d]]
            pos[0] += oper[0]
            pos[1] += oper[1]
    return pos