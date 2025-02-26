'''
Created by sunwoong on 2025/02/26
'''

def solution(players, m, k):
    out = [0 for _ in range(25)]
    answer = 0
    count = 0
    for i in range(len(players)):
        if out[i] > 0:
            count -= out[i]
        server = players[i] // m
        if server > count:
            need = server - count
            if i + k < len(out):
                out[i + k] += need
            count += need
            answer += need
    return answer