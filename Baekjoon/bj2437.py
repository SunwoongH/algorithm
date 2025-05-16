'''
Created by sunwoong on 2025/05/16
'''
import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
sequence.sort()

section = [0, 0]
for num in sequence:
    new_section = [section[0] + num, section[1] + num]
    if section[1] + 1 < new_section[0]:
        break
    section = [section[0], new_section[1]]
print(section[1] + 1)