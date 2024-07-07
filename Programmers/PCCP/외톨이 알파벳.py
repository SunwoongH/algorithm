'''
Created by sunwoong on 2024/07/07
'''

from collections import Counter

def solution(input_string):
    stack = []
    for char in input_string:
        if stack and stack[-1] == char:
            continue
        stack.append(char)
    count = Counter(stack)
    promising = list(filter(lambda x: x[1] > 1, count.most_common()))
    if not promising:
        return "N"
    return ''.join(sorted(map(lambda x: x[0], promising)))