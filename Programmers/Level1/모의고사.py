'''
Created by sunwoong on 2024/03/27

풀이 시간 - 15분
'''
from collections import defaultdict

def solution(answers):
    rules = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    count_table = defaultdict(int)
    for i in range(len(answers)):
        if answers[i] == rules[0][i % len(rules[0])]:
            count_table[1] += 1
        if answers[i] == rules[1][i % len(rules[1])]:
            count_table[2] += 1
        if answers[i] == rules[2][i % len(rules[2])]:
            count_table[3] += 1
    standard = max(count_table.items(), key=lambda x: x[1])[1]
    answer = sorted(list(map(lambda x: x[0], filter(lambda x: x[1] == standard, count_table.items()))))
    return answer