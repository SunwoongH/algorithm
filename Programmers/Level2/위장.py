'''
Created by sunwoong on 2022/12/26
'''
from collections import defaultdict

def solution(clothes):
    table = defaultdict(int)
    for _, kind in clothes:
        table[kind] += 1
    answer = 1
    for count in table.values():
        answer *= count + 1
    return answer - 1