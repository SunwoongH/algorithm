'''
Created by sunwoong on 2023/02/12
'''
import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
temp = []
for num in sequence:
    if not temp or temp[-1] < num:
        temp.append(num)
        continue
    left, right = 0, len(temp)
    while left < right:
        mid = (left + right) // 2
        if temp[mid] < num:
            left = mid + 1
        else:
            right = mid
    temp[left] = num
print(len(temp))