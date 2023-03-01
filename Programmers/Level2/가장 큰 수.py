'''
Created by sunwoong on 2023/03/01
'''
from functools import cmp_to_key

def compare(a, b):
    temp_a = int(a + b)
    temp_b = int(b + a)
    if temp_a > temp_b:
        return 1
    elif temp_a < temp_b:
        return -1
    return 0

def solution(numbers):
    numbers = map(str, numbers)
    numbers = sorted(numbers, key=cmp_to_key(compare), reverse=True)
    answer = ''.join(numbers)
    return answer if answer[0] != "0" else "0"