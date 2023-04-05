'''
Created by sunwoong on 2023/04/05
'''
import sys
input = sys.stdin.readline

def checking(line):
    prev_height = line[0]
    prev_count = 1
    check = [False for _ in range(len(line))]
    for i in range(1, len(line)):
        if line[i] == prev_height:
            if not check[i]:
                prev_count += 1
            else:
                prev_count = 0
            continue
        if line[i] > prev_height:
            if abs(line[i] - prev_height) > 1:
                return False
            if prev_count >= l:
                for k in range(i - 1, i - l - 1, -1):
                    check[k] = True
            else:
                return False
        prev_height = line[i]
        prev_count = 1
    prev_height = line[-1]
    prev_count = 1
    for i in range(len(line) - 2, -1, -1):
        if line[i] == prev_height:
            if not check[i]:
                prev_count += 1
            else:
                prev_count = 0
            continue
        if line[i] > prev_height:
            if abs(line[i] - prev_height) > 1:
                return False
            if prev_count >= l:
                for k in range(i + 1, i + l + 1):
                    check[k] = True
            else:
                return False
        prev_height = line[i]
        prev_count = 1 if not check[i] else 0
    return True

n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
count = 0
for line in board:
    result = checking(line)
    if result:
        count += 1
for line in zip(*board):
    result = checking(line)
    if result:
        count += 1
print(count)