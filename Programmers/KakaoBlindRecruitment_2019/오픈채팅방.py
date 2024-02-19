'''
Created by sunwoong on 2024/02/19

풀이 시간 - 20분
'''

def solution(record):
    sentence = ("님이 들어왔습니다.", "님이 나갔습니다.")
    nickname = dict()
    answer = []
    for data in record:
        temp = data.split()
        if len(temp) == 2:
            answer.append([temp[1], sentence[1]])
            continue
        if temp[0] == 'Enter':
            nickname[temp[1]] = temp[2]
            answer.append([temp[1], sentence[0]])
        elif temp[0] == 'Change':
            nickname[temp[1]] = temp[2]
    return [nickname[answer[i][0]] + answer[i][1] for i in range(len(answer))]