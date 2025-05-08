'''
Created by sunwoong on 2025/05/08
'''

go = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
back = {'U': (0, -1), 'D': (0, 1), 'R': (-1, 0), 'L': (1, 0)}

right = {'U':'R', 'R':'D', 'D':'L', 'L':'U'}
left = {'U':'L', 'L':'D', 'D':'R', 'R':'U'}

def solution(command):
    x, y = 0, 0
    
    direct = 'U'
    for c in command:
        if c == 'R':
            direct = right[direct]
        elif c == 'L':
            direct = left[direct]
        elif c == 'G':
            oper = go[direct]
            x = x + oper[0]
            y = y + oper[1]
        else:
            oper = back[direct]
            x = x + oper[0]
            y = y + oper[1]
    
    return [x, y]