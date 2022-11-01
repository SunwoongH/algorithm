'''
Created by sunwoong on 2022/11/01
'''
import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
min_interval = sys.maxsize
result = []
for i in range(n):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if 0 >= sequence[i] + sequence[mid]:
            left = mid + 1
        else:
            right = mid - 1
    temp = None
    if 0 <= right:
        temp = sequence[right]
        index = right
        if left < n and abs(sequence[i] + temp) > abs(sequence[i] + sequence[left]):
            temp = sequence[left]
            index = left
    else:
        temp = sequence[left]
        index = left
    if temp == sequence[i]:
        if index == right:
            is_change = False
            if 0 <= right - 1:
                temp = sequence[right - 1]
                index = right - 1
                is_change = True
            if left < n:
                if is_change:
                    if abs(sequence[i] + temp) > abs(sequence[i] + sequence[left]):
                        temp = sequence[left]
                        index = left
                else:
                    temp = sequence[left]
                    index = left
        else:
            if left + 1 < n:
                temp = sequence[left + 1]
                index = left + 1
    if min_interval == abs(sequence[i] + temp):
        result.append((sequence[i], sequence[index]))
    elif min_interval > abs(sequence[i] + temp):
        result.clear()
        min_interval = abs(sequence[i] + temp)
        result.append((sequence[i], sequence[index]))
print(*sorted(result[0]))