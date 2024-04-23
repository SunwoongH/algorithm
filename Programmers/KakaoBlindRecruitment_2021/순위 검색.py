'''
Created by sunwoong on 2024/04/23

풀이 시간 - 70분
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

from bisect import bisect_left

def solution(info, query):
    answer = []
    data_table = dict()
    for lang in ['cpp', 'java', 'python', '-']:
        data_table[lang] = dict()
        for pos in ['backend', 'frontend', '-']:
            data_table[lang][pos] = dict()
            for exp in ['junior', 'senior', '-']:
                data_table[lang][pos][exp] = dict()
                for food in ['chicken', 'pizza', '-']:
                    data_table[lang][pos][exp][food] = list()
    for data in info:
        data = data.split()
        for lang in [data[0], '-']:
            for pos in [data[1], '-']:
                for exp in [data[2], '-']:
                    for food in [data[3], '-']:
                        data_table[lang][pos][exp][food].append(int(data[4]))
    for lang in ['cpp', 'java', 'python', '-']:
        for pos in ['backend', 'frontend', '-']:
            for exp in ['junior', 'senior', '-']:
                for food in ['chicken', 'pizza', '-']:
                    data_table[lang][pos][exp][food].sort()
    for request in query:
        request = request.replace('and', '')
        request = request.split()
        scores = data_table[request[0]][request[1]][request[2]][request[3]]
        pos = bisect_left(scores, int(request[4]))
        answer.append(len(scores) - pos)
    return answer