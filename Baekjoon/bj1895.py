'''
Created by sunwoong on 2022/07/01
'''
import sys
from typing import List

n, m = map(int, sys.stdin.readline().split())
image = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
target = int(sys.stdin.readline())

def median_filter(image: List[List[int]]) -> int:
    count = 0
    temp = []
    for r in range(1, n - 1):
        for c in range(1, m - 1):
            for margin_r in range(-1, 2):
                for margin_c in range(-1, 2):
                    temp.append(image[r + margin_r][c + margin_c])
            temp.sort()
            if temp[4] >= target:
                count += 1
            temp.clear()
    return count

print(median_filter(image))