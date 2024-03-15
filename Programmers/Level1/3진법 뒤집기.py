'''
Created by sunwoong on 2024/03/15

풀이 시간 - 20분
'''
def converter(number, n):
    answer = []
    while number != 0:
        number, mod = divmod(number, n)
        answer.append(str(mod))
    return ''.join(answer)

def solution(n):
    return int(converter(n, 3), 3)