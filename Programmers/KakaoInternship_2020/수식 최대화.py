'''
Created by sunwoong on 2024/04/03

풀이 시간 - 44분
'''
from collections import defaultdict
from itertools import permutations
import re

def calculate(numbers, expressions, case, pos, count):
    if not expressions:
        return numbers[0]
    result = None
    if count[case[pos]] == 0:
        result = calculate(numbers, expressions, case, pos + 1, count)
    else:
        p = 0
        for i in range(len(expressions)):
            if expressions[i] == case[pos]:
                count[case[pos]] -= 1
                p = i
                break
        new_numbers = numbers[:p]
        if case[pos] == '*':
            new_numbers.append(numbers[p] * numbers[p + 1])
        elif case[pos] == '+':
            new_numbers.append(numbers[p] + numbers[p + 1])
        else:
            new_numbers.append(numbers[p] - numbers[p + 1])
        result = calculate(new_numbers + numbers[p + 2:], expressions[:p] + expressions[p + 1:], case, pos, count)
    return result

def solution(expression):
    answer = 0
    target = ['-', '*', '+']
    count = defaultdict(int)
    expressions = []
    for char in expression:
        if char in target:
            count[char] += 1
            expressions.append(char)
    numbers = list(map(int, re.sub('[^0-9]', ' ', expression).split()))
    for case in permutations(target, 3):
        result = abs(calculate(numbers, expressions, case, 0, count.copy()))
        answer = max(answer, result)
    return answer