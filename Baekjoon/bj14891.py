'''
Created by sunwoong on 2022/10/28
'''
import sys
from collections import deque

def is_promising():
    for left in range(SIZE - 1):
        right = left + 1
        if wheels[left][check[0]] != wheels[right][check[1]]:
            promising[left] = True

def rotate_wheel(start, orientation):
    move = [0 for _ in range(SIZE)]
    queue = deque([(start, orientation)])
    move[start] = orientation
    visited = [False for _ in range(SIZE)]
    visited[start] = True
    while queue:
        pos, orientation = queue.popleft()
        for oper in [-1, 1]:
            dpos = pos + oper
            if 0 <= dpos < SIZE and not visited[dpos] and promising[(pos + dpos) // 2]:
                visited[dpos] = True
                move[dpos] = -1 if orientation == 1 else 1
                queue.append((dpos, move[dpos]))
        wheels[pos].rotate(orientation)
        
def calculate_wheel():
    result = 0
    scores = [1, 2, 4, 8]
    for i in range(SIZE):
        if wheels[i][0]:
            result += scores[i]
    return result

SIZE = 4
wheels = [deque(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(SIZE)]
k = int(sys.stdin.readline())
check = [2, 6]
for _ in range(k):
    start, orientation = map(int, sys.stdin.readline().split())
    promising = [False, False, False]
    is_promising()
    rotate_wheel(start - 1, orientation)
print(calculate_wheel())