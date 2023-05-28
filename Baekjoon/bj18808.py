'''
Created by sunwoong on 2023/05/28
'''
import sys
input = sys.stdin.readline

PROMISING = 1
EMPTY = 0

def search_and_is_promising(sticker, r, c, count):
    for i in range(n - r + 1):
        for j in range(m - c + 1):
            temp = 0
            for k in range(i, i + r):
                for l in range(j, j + c):
                    if notebook[k][l] == EMPTY and sticker[k - i][l - j] == PROMISING:
                        temp += 1
            if temp == count:
                for k in range(i, i + r):
                    for l in range(j, j + c):
                        if notebook[k][l] == EMPTY and sticker[k - i][l - j] == PROMISING:
                            notebook[k][l] = PROMISING
                return True
    return False

def rotate_sticker(sticker, r, c):
    sticker.reverse()
    sticker = list(zip(*sticker))
    return sticker, c, r

def count_sticker_on_notebook():
    count = 0
    for i in range(n):
        for j in range(m):
            if notebook[i][j] == PROMISING:
                count += 1
    return count

n, m, k = map(int, input().split())
notebook = [[EMPTY for _ in range(m)] for _ in range(n)]
stickers = []
for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    count = 0
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == PROMISING:
                count += 1
    stickers.append((sticker, r, c, count))

for data in stickers:
    sticker, r, c, count = data
    case_count = 0
    while case_count < 4:
        case_count += 1
        result = search_and_is_promising(sticker, r, c, count)
        if result:
            break
        if case_count == 4:
            break
        sticker, r, c = rotate_sticker(sticker, r, c)
print(count_sticker_on_notebook())