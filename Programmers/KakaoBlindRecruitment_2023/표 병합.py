'''
Created by sunwoong on 2024/09/13

풀이 시간 - 60분
'''

def solution(commands):
    answer = []
    board = [[[None, set([(r, c)])] for c in range(51)] for r in range(51)]
    for command in commands:
        data = command.split()
        if data[0] == 'UPDATE':
            if len(data) == 4:
                promising = board[int(data[1])][int(data[2])][1]
                for r, c in promising:
                    board[r][c][0] = data[3]
            else:
                for r in range(1, 51):
                    for c in range(1, 51):
                        if board[r][c][0] == data[1]:
                            promising = board[r][c][1]
                            for i_r, i_c in promising:
                                board[i_r][i_c][0] = data[2]
        elif data[0] == 'MERGE':
            if data[1] == data[3] and data[2] == data[4]:
                continue
            value_a = board[int(data[1])][int(data[2])][0]
            value_b = board[int(data[3])][int(data[4])][0]
            promising_a = board[int(data[1])][int(data[2])][1]
            promising_b = board[int(data[3])][int(data[4])][1]
            for r, c in promising_a.union(promising_b):
                board[r][c][1] = promising_a.union(promising_b)
            if value_a:
                for r, c in promising_a.union(promising_b):
                    board[r][c][0] = value_a
            elif value_b:
                for r, c in promising_a.union(promising_b):
                    board[r][c][0] = value_b
        elif data[0] == 'UNMERGE':
            promising = board[int(data[1])][int(data[2])][1]
            for r, c in promising:
                if r == int(data[1]) and c == int(data[2]):
                    board[r][c][1] = set([(r, c)])
                    continue
                board[r][c][0] = None
                board[r][c][1] = set([(r, c)])
        else:
            answer.append(board[int(data[1])][int(data[2])][0] if board[int(data[1])][int(data[2])][0] else 'EMPTY')
                
    return answer