'''
Created by sunwoong on 2023/03/06
'''

def solution(land):
    SIZE = 4
    for r in range(1, len(land)):
        for c in range(SIZE):
            temp = []
            for k in range(SIZE):
                if c == k:
                    continue
                temp.append(land[r - 1][k])
            land[r][c] += max(temp)
    return max(land[len(land) - 1])