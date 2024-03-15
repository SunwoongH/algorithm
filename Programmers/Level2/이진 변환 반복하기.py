'''
Created by sunwoong on 2024/03/15

풀이 시간 - 10분
'''

def solution(s):
    temp = None
    answer_count = zero_count = 0
    while temp != "1":
        answer_count += 1
        count = s.count('0')
        zero_count += count
        length = len(s) - count
        temp = bin(length)[2:]
        s = temp
    return [answer_count, zero_count]