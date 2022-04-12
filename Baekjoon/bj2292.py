'''
Created by sunwoong on 2022/04/12
'''
import sys

n = int(sys.stdin.readline())
result, pivot = 1, 1
while pivot < n:
    pivot += 6 * result
    result += 1
print(result)