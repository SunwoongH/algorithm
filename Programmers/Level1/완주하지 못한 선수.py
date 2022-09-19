'''
Created by sunwoong on 2022/09/19
'''
from collections import defaultdict

def solution(participant, completion):
    completion_table = defaultdict(int)
    for person in completion:
        completion_table[person] += 1
    for person in participant:
        completion_table[person] -= 1
        if completion_table[person] < 0:
            return person