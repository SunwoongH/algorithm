'''
Created by sunwoong on 2023/02/03
'''
import sys
input = sys.stdin.readline

move = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1), 5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}
diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

def move_clouds(clouds, direction, step):
    after_clouds = []
    oper = move[direction]
    for cloud in clouds:
        r, c = cloud
        for _ in range(step):
            r = (r + n + oper[0]) % n
            c = (c + n + oper[1]) % n
        after_clouds.append((r, c))
    return after_clouds

def rain_from_the_clouds(clouds):
    for cloud in clouds:
        r, c = cloud
        board[r][c] += 1

def water_copy_magic(clouds):
    for cloud in clouds:
        count = 0
        r, c = cloud
        for oper in diagonal:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < n and board[dr][dc] > 0:
                count += 1
        board[r][c] += count
    return set(clouds)

def make_new_clouds(before_clouds):
    clouds = []
    for r in range(n):
        for c in range(n):
            if (r, c) not in before_clouds and board[r][c] > 1:
                clouds.append((r, c))
                board[r][c] -= 2
    return clouds

def sum_of_water():
    total = 0
    for r in range(n):
        for c in range(n):
            total += board[r][c]
    return total

n, m = map(int, input().split())
board = []
orders = []
for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)
for _ in range(m):
    direction, step = map(int, input().split())
    orders.append((direction, step))
clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
for i in range(m):
    clouds = move_clouds(clouds, orders[i][0], orders[i][1])
    rain_from_the_clouds(clouds)
    clouds = water_copy_magic(clouds)
    clouds = make_new_clouds(clouds)
print(sum_of_water())