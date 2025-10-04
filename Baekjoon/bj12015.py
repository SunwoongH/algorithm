'''
Created by sunwoong on 2025/10/04
'''
import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
answer = []

for num in sequence:
    if not answer or answer[-1] < num:
        answer.append(num)
        continue
    pos = bisect_left(answer, num)
    answer[pos] = num

print(len(answer))