'''
Created by sunwoong on 2024/03/25

풀이 시간 - 5분
'''

def calculate(num, depth):
    if depth > 500:
        return -1
    if num == 1:
        return 0
    count = 1
    if num % 2 == 0:
        return_count = calculate(num // 2, depth + 1)
    else:
        return_count = calculate(num * 3 + 1, depth + 1)
    if return_count == -1:
        count = -1
    else:
        count += return_count
    return count

def solution(num):
    if num == 1:
        return 0
    return calculate(num, 1)