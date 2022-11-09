'''
Created by sunwoong on 2022/11/09
'''
import sys
from collections import deque, defaultdict

PROMISING = 0
APPLE = 2
SNAKE = 3
SIZE = 4

def snake_game() -> int:
    snake = deque([(0, 0)])
    head = 1
    game_time = 0
    board[0][0] = SNAKE
    while True:
        head_r, head_c = snake[-1][0], snake[-1][1]
        next_head_r = head_r + forward[head][0]
        next_head_c = head_c + forward[head][1]
        game_time += 1
        if next_head_r < 0 or next_head_r >= n or next_head_c < 0 or next_head_c >= n \
            or board[next_head_r][next_head_c] == SNAKE:
            return game_time
        elif board[next_head_r][next_head_c] == PROMISING:
            tail_r, tail_c = snake.popleft()
            board[tail_r][tail_c] = PROMISING
        snake.append((next_head_r, next_head_c))
        board[next_head_r][next_head_c] = SNAKE
        if orientation[game_time] in orders:
            if orientation[game_time] == 'L':
                head = (head + SIZE - 1) % SIZE
            else:
                head = (head + 1) % SIZE

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
board = [[PROMISING for _ in range(n)] for _ in range(n)]
forward = {0 : (-1, 0), 1 : (0, 1), 2 : (1, 0), 3 : (0, -1)}
orders = {'L', 'D'}
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    board[r - 1][c - 1] = APPLE
orientation = defaultdict(str)
l = int(sys.stdin.readline())
for _ in range(l):
    time, order = map(str, sys.stdin.readline().split())
    orientation[int(time)] = order
print(snake_game())