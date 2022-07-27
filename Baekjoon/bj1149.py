'''
Created by sunwoong on 2022/07/28
'''
import sys

n = int(sys.stdin.readline())
curr_case = [0 for _ in range(3)]
for i in range(n):
    red, green, blue = map(int, sys.stdin.readline().split())
    prev_case = curr_case[:]
    if i == 0:
        curr_case[0], curr_case[1], curr_case[2] = red, green, blue
        continue
    curr_case[0] = red + min(prev_case[1], prev_case[2])
    curr_case[1] = green + min(prev_case[0], prev_case[2])
    curr_case[2] = blue + min(prev_case[0], prev_case[1])
print(min(curr_case))