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
        board[coordinates[i][0] - end_x + end_y][end_y - coordinates[i][1] + end_x] = CHECK
        next_coordinates.append((end_y - coordinates[i][1] + end_x, coordinates[i][0] - end_x + end_y))
    coordinates.extend(next_coordinates)

n = int(input())
board = [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)]
for _ in range(n):
    x, y, d, g = map(int, input().split())
    coordinates = [(x, y), (x + init[d][0], y + init[d][1])]
    board[y][x] = CHECK
    board[y + init[d][1]][x + init[d][0]] = CHECK
    for _ in range(g):
        make_dragon_curve()
square_count = 0
for r in range(SIZE - 1):
    for c in range(SIZE - 1):
        if board[r][c] and board[r + 1][c] and board[r][c + 1] and board[r + 1][c + 1]:
            square_count += 1
print(square_count)