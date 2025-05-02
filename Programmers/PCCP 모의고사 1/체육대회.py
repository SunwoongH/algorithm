'''
Created by sunwoong on 2025/05/02
'''
from itertools import permutations

def solution(ability):
    length = len(ability)
    answer = 0
    
    for case in permutations(range(0, length), len(ability[0])):
        total = 0
        for i in range(len(ability[0])):
            total += ability[case[i]][i]
        answer = max(answer, total)

    return answer