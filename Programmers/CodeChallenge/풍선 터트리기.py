'''
Created by sunwoong on 2025/04/02
'''

def solution(a):
    if len(a) == 1:
        return 1
    
    answer = 2
    left = a[:]
    right = a[:]
    
    for i in range(1, len(a)):
        left[i] = min(left[i - 1], left[i])
    for i in range(len(a) - 2, -1, -1):
        right[i] = min(right[i + 1], right[i])
        
    for i in range(1, len(a) - 1):
        if left[i - 1] < a[i] and right[i + 1] < a[i]:
            continue
        answer += 1
    
    return answer