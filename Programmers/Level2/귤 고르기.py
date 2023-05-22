'''
Created by sunwoong on 2023/05/22
'''
from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    for _, count in counter.most_common():
        if k == 0:
            break
        elif count <= k:
            k -= count
        else:
            k -= k
        answer += 1
    return answer