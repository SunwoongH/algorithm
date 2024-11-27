'''
Created by sunwoong on 2024/11/27

'''

def solution(dartResult):
    answer = []
    temp = None
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i] == '1' and dartResult[i + 1] == '0':
                continue
            if temp is not None:
                answer.append(temp)
            if dartResult[i] == '0' and i - 1 >= 0 and dartResult[i - 1] == '1':
                temp = 10
                continue
            temp = int(dartResult[i])
            continue
        if dartResult[i] == 'S':
            temp = temp ** 1
        elif dartResult[i] == 'D':
            temp = temp ** 2
        elif dartResult[i] == 'T':
            temp = temp ** 3
        elif dartResult[i] == '*':
            if len(answer) > 0:
                answer[-1] *= 2
            temp *= 2
        else:
            temp *= -1
    answer.append(temp)
    
    return sum(answer)