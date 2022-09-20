'''
Created by sunwoong on 2022/09/20

풀이 시간 - 실패 (풀이 참고)
'''
from itertools import combinations
from bisect import bisect_left

def make_cases(processed_info):
    cases = []
    for k in range(5):
        for item in combinations([0, 1, 2, 3], k):
            case = []
            for i in range(4):
                if i not in item:
                    case.append(processed_info[i])
                else:
                    case.append('-')
            cases.append(''.join(case))
    return cases

def solution(info, query):
    answer = []
    all_cases = {}
    
    for item in info:
        processed_info = item.split()
        cases = make_cases(processed_info)
        for case in cases:
            if case not in all_cases:
                all_cases[case] = [int(processed_info[4])]
            else:
                all_cases[case].append(int(processed_info[4]))
    for case in all_cases:
        all_cases[case].sort()
    
    for item in query:
        processed_query = item.replace(' and ', ' ').split()
        target = ''.join(processed_query[:4])
        num = int(processed_query[4])
        if target in all_cases:
            answer.append(len(all_cases[target]) - bisect_left(all_cases[target], num))
        else:
            answer.append(0)
    return answer