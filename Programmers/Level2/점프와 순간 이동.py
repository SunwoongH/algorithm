'''
Created by sunwoong on 2023/07/09
'''

def solution(n):
    answer = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            answer += 1
    return answer