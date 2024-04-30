'''
Created by sunwoong on 2024/04/30

풀이 시간 - 10분
'''

def solution(record):
    answer = []
    user = dict()
    for data in record:
        data = data.split()
        if data[0] == 'Enter':
            answer.append([data[1], "님이 들어왔습니다."])
            user[data[1]] = data[2]
        elif data[0] == 'Leave':
            answer.append([data[1], "님이 나갔습니다."])
        else:
            user[data[1]] = data[2]
    return [''.join([user[data[0]], data[1]]) for data in answer]