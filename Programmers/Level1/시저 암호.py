'''
Created by sunwoong on 2024/03/06

풀이 시간 - 10분
'''

def solution(s, n):
    alphabet = 26
    answer = []
    for char in s:
        if char.isalpha():
            if char.isupper():
                answer.append(chr((ord(char) - 65 + n) % alphabet + 65))
            else:
                answer.append(chr((ord(char) - 97 + n) % alphabet + 97))
        else:
            answer.append(char)
    return ''.join(answer)