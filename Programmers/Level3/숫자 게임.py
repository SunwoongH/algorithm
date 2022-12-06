'''
Created by sunwoong on 2022/12/06
'''

def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    i = 0
    count = 0
    for a in A:
        if a < B[i]:
            count += 1
            i += 1
    return count