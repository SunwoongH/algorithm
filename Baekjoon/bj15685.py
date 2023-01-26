'''
Created by sunwoong on 2023/01/26
'''
import sys
input = sys.stdin.readline

RIGHT = 0
TOP = 1
LEFT = 2
BOTTOM = 3
SIZE = 101
EMPTY = False
CHECK = True
init = {RIGHT : (1, 0), TOP : (0, -1), LEFT : (-1, 0), BOTTOM : (0, 1)}

def make_dragon_curve():
    end_x = coordinates[-1][0]
    end_y = coordinates[-1][1]
    next_coordinates = []
    for i in range(len(coordinates) - 2, -1, -1):
        dx = end_x - (coordinates[i][1] - end_y)
        dy = end_y + (coordinates[i][0] - end_x)
        board[dy][dx] = CHECK
        next_coordinates.append((dx, dy))
    coordinates.extend(next_coordinates)

def count_square():
    square_count = 0
    for r in range(SIZE - 1):
        for c in range(SIZE - 1):
            if board[r][c] and board[r + 1][c] and board[r][c + 1] and board[r + 1][c + 1]:
                square_count += 1
    return square_count

n = int(input())
board = [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)]
for _ in range(n):
    x, y, d, g = map(int, input().split())
    tail = (x, y)
    head = (x + init[d][0], y + init[d][1])
    coordinates = [tail, head]
    board[tail[1]][tail[0]] = CHECK
    board[head[1]][head[0]] = CHECK
    for _ in range(g):
        make_dragon_curve()
print(count_square())