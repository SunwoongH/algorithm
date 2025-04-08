'''
Created by sunwoong on 2025/04/08
'''

def solution(n, cores):
    if n <= len(cores):
        return n
    n -= len(cores)
    left = 1
    right = max(cores) * n
    
    while left < right:
        mid = (left + right) // 2
        throughput = 0
        for core in cores:
            throughput += mid // core
        if throughput >= n:
            right = mid
        else:
            left = mid + 1
    
    for core in cores:
        n -= (right - 1) // core
    
    for i in range(len(cores)):
        if right % cores[i] == 0:
            n -= 1
            if n == 0:
                return i + 1
    