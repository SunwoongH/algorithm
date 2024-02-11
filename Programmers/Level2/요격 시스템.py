'''
Created by sunwoong on 2024/02/11

풀이 시간 - 60분
'''

def solution(targets):
    targets = sorted(targets, key = lambda x: (x[0], -x[1]))
    p = targets[0][1]
    count = 0
    for i in range(1, len(targets)):
        if p <= targets[i][0]:
            count += 1
            p = targets[i][1]
        elif p > targets[i][1]:
            p = targets[i][1]
    return count + 1