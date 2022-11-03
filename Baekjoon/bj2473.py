'''
Created by sunwoong on 2022/11/03
'''
import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
sequence.sort()
min_value = sys.maxsize
result = []
is_result = False
for i in range(n - 1):
    left = i + 1
    right = n - 1
    while left < right:
        target = sequence[i] + sequence[left] + sequence[right]
        if abs(target) < min_value:
            min_value = abs(target)
            result = [sequence[i], sequence[left], sequence[right]]
        if target == 0:
            print(*result)
            sys.exit(0)
        elif target < 0:
            left += 1
        else:
            right -= 1
print(*result)