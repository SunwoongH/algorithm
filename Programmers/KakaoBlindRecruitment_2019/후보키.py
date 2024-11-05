'''
Created by sunwoong on 2024/11/05

풀이 시간 - 40분
'''

from itertools import combinations

def solution(relation):
    candidate = set()
    
    for i in range(1, len(relation[0]) + 1):
        for case in combinations(range(0, len(relation[0])), i):
            temp = set(case)
            
            is_seen = True
            for key in candidate:
                is_seen = True
                for c in key:
                    if c not in temp:
                        is_seen = False
                        break
                if is_seen:
                    break
            
            if is_seen and len(candidate) > 0:
                continue
                
            seen = set()
            
            is_candidate_key = True
            for i in range(len(relation)):
                item = ''
                for pos in case:
                    item += relation[i][pos]
                if item not in seen:
                    seen.add(item)
                else:
                    is_candidate_key = False
                    break
            
            if is_candidate_key:
                candidate.add(case[:])

    return len(candidate)