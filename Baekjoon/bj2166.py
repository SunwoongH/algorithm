'''
Created by sunwoong on 2022/09/12
'''
import sys

n = int(sys.stdin.readline())
coordinate = []
for _ in range(n):
    coordinate.append(tuple(map(int, sys.stdin.readline().split())))
coordinate.append(coordinate[0][:])
sum_x = sum_y = 0
for i in range(1, n + 1):
    sum_x += coordinate[i - 1][1] * coordinate[i][0]
    sum_y += coordinate[i - 1][0] * coordinate[i][1]
area = abs(sum_y - sum_x) / 2
print("%.1f" %area)