'''
Created by sunwoong on 2022/09/18

풀이 시간 - 171분
'''
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for count in course:
        sample_space = []
        for order in orders:
            if len(order) < count:
                continue
            sample_space.extend(list(combinations(sorted(order), count)))
        if sample_space:
            sample_space = Counter(sample_space)
            most_count = sample_space.most_common(1)[0][1]
            if most_count < 2:
                continue
            for sample in sample_space:
                if sample_space[sample] < most_count:
                    continue
                answer.append(''.join(sample))
    return sorted(answer)