'''
Created by sunwoong on 2024/07/07
'''

def find(gen, order):
    if gen == 1:
        return "Rr"
    cut = 4 ** (gen - 2)
    if order <= cut:
        return 'RR'
    elif cut * 3 < order:
        return 'rr'
    return find(gen - 1, order % cut if order % cut > 0 else cut)

def solution(queries):
    answer = []
    for query in queries:
        answer.append(find(query[0], query[1]))
    return answer