'''
Created by sunwoong on 2025/05/02
'''
from collections import Counter

def solution(input_string):
    stack = []
    for char in input_string:
        if not stack:
            stack.append(char)
            continue
        while stack and stack[-1] == char:
            stack.pop()
        stack.append(char)

    counting = Counter(stack)
    promising = list(map(lambda x: x[0], filter(lambda x: x[1] >= 2, counting.items())))
    if not promising:
        return "N"
    
    promising.sort()
    return ''.join(promising)