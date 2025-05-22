'''
Created by sunwoong on 2025/05/22
'''
from collections import defaultdict

zero_count = 0
one_count = 0

def calculate(arr, n, r1, c1, r2, c2):
    global one_count
    global zero_count
    
    if r1 == r2 and c1 == c2:
        if arr[r1][c1] == n:
            one_count += 1
        else:
            zero_count += 1
        return
        
    count = defaultdict(int)
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            count[arr[r][c]] += 1
    
    if count[1] == n ** 2:
        one_count += 1
        return
    if count[0] == n ** 2:
        zero_count += 1
        return
    calculate(arr, n // 2, r1, c1, r2 - n // 2, c2 - n // 2)
    calculate(arr, n // 2, r1, c1 + n // 2, r2 - n // 2, c2)
    calculate(arr, n // 2, r1 + n // 2, c1, r2, c2 - n // 2)
    calculate(arr, n // 2, r1 + n // 2, c1 + n // 2, r2, c2)

def solution(arr):
    calculate(arr, len(arr), 0, 0, len(arr) - 1, len(arr) - 1)

    return [zero_count, one_count]