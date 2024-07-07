'''
Created by sunwoong on 2024/07/07
'''
from itertools import permutations

def solution(ability):
    answer = 0
    for case in permutations(range(len(ability)), len(ability[0])):
        temp = 0
        for c, r in enumerate(case):
            temp += ability[r][c]
        answer = max(answer, temp)
    return answer