'''
Created by sunwoong on 2024/04/22

풀이 시간 - 40분
'''

def solution(n, times):
    low = 1
    high = max(times) * n
    while low < high:
        mid = (low + high) // 2
        available = 0
        for time in times:
            available += mid // time
        if n <= available:
            high = mid
        else:
            low = mid + 1
    return low