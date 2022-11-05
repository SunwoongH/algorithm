'''
Created by sunwoong on 2022/11/05
'''
import sys

test = int(sys.stdin.readline())
for _ in range(test):
    n, k = map(int, sys.stdin.readline().split())
    optimize = sys.maxsize
    answer = 0
    sequence = sorted(list(map(int, sys.stdin.readline().split())))
    left = 0
    right = n - 1
    while left < right:
        temp = sequence[left] + sequence[right]
        if abs(k - temp) <= optimize:
            if abs(k - temp) == optimize:
                answer += 1
            else:
                optimize = abs(k - temp)
                answer = 0
                answer += 1
        if temp == k:
            left += 1
            right -= 1
        elif temp < k:
            left += 1
        else:
            right -= 1
    print(answer)