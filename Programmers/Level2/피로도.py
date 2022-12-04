'''
Created by sunwoong on 2022/12/04
'''
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for sequence in permutations(dungeons, len(dungeons)):
        count = 0
        life = k
        for essential, consume in sequence:
            if life >= essential:
                count += 1
                life -= consume
        answer = max(answer, count)
    return answer