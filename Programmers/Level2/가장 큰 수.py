'''
Created by sunwoong on 2024/04/22
'''
from functools import cmp_to_key

def compare(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    if num1 + num2 > num2 + num1:
        return -1
    elif num1 + num2 < num2 + num1:
        return 1
    return 0

def solution(numbers):
    numbers = sorted(numbers, key=cmp_to_key(compare))
    return str(int(''.join(map(str, numbers))))