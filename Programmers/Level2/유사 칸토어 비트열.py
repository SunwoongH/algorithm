'''
Created by sunwoong on 2025/05/27
'''
cache = {}

def counting(n, l, r):
    if (n, l, r) in cache:
        return cache[(n, l, r)]
    
    if l == 1 and r == 5 ** n:
        cache[(n, l, r)] = 4 ** n
        return 4 ** n
    
    count = 0
    for i in range(5):
        if i == 2:
            continue
            
        start = 5 ** (n - 1) * i + 1
        end = 5 ** (n - 1) * (i + 1)
        
        if l > end or r < start:
            continue
        
        count += counting(n - 1, max(1, l - start + 1), min(5 ** (n - 1), r - start + 1))
        
    cache[(n, l, r)] = count
    
    return count

def solution(n, l, r):
    return counting(n, l, r)