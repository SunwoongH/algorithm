'''
Created by sunwoong on 2023/06/07
'''
from collections import Counter

def solution(weights):
    answer = 0
    counting_table = Counter(weights)
    seen = set(weights)
    cases = [(1, 1), (1, 2), (2, 3), (3, 4)]
    for weight in seen:
        for left, right in cases:
            if left == 1 and right == 1:
                answer += counting_table[weight] * (counting_table[weight] - 1) // 2
            else:
                if (weight * right / left) in seen:
                    answer += counting_table[weight * right / left] * counting_table[weight]
    return answer