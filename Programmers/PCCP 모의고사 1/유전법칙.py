'''
Created by sunwoong on 2025/05/02
'''
def calculate(n, p):
    if n == 1:
        return 'Rr'
    standard = 4 ** (n - 2)
    if p <= standard:
        return 'RR'
    if p > standard * 3:
        return 'rr'
    np = (p - standard) % standard
    if np == 0:
        np = standard
    return calculate(n - 1, np)

def solution(queries):
    answer = []
    for query in queries:
        answer.append(calculate(query[0], query[1]))
    return answer