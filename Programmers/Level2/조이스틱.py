'''
Created by sunwoong on 2024/06/21

풀이 시간 - 240분
'''

def solution(name):
    answer = 0
    distance = len(name) - 1
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        distance = min(distance, 2 * i + len(name) - next_i, 2 * (len(name) - next_i) + i)
    return answer + distance