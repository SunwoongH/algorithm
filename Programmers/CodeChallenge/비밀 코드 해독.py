'''
Created by sunwoong on 2025/02/15
'''

from itertools import combinations

def solution(n, q, ans):
    sequence = range(1, n + 1)
    q = list(map(set, q))
    answer = 0
    
    for case in combinations(sequence, 5):
        case = set(case)
        promising = True
        for i in range(len(q)):
            if len(case & q[i]) != ans[i]:
                promising = False
                break
        if promising:
            answer += 1
        
    return answer