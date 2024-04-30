'''
Created by sunwoong on 2024/04/30

풀이 시간 - 5분
'''
from collections import defaultdict

def solution(clothes):
    table = defaultdict(int)
    for _, kind in clothes:
        table[kind] += 1
    answer = 1
    for kind in table.keys():
        answer *= table[kind] + 1
    return answer - 1