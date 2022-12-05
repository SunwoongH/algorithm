'''
Created by sunwoong on 2022/12/05
'''

def solution(n, left, right):
    answer = []
    for r in range(left // n, right // n + 1):
        for c in range(n):
            if r == left // n and c < left % n:
                continue
            elif r == right // n and c > right % n:
                break
            answer.append(max(r + 1, c + 1))
    return answer