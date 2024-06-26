'''
Created by sunwoong on 2024/06/26

풀이 시간 - 25분
'''
from collections import defaultdict

def solution(id_list, report, k):
    reported = defaultdict(set)
    count = defaultdict(int)
    for data in report:
        a, b = data.split()
        reported[b].add(a)
    for target in id_list:
        if len(reported[target]) >= k:
            for user in reported[target]:
                count[user] += 1
    answer = []
    for user in id_list:
        answer.append(count[user])
    return answer