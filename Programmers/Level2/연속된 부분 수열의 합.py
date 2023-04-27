'''
Created by sunwoong on 2023/04/27
'''

def solution(sequence, k):
    length = 1_000_001
    answer = None
    start = end = len(sequence) - 1
    temp = 0
    while start >= 0:
        temp += sequence[start]
        while temp > k and start < end:
            temp -= sequence[end]
            end -= 1
        if temp == k:
            if length >= end - start + 1:
                answer = [start, end]
                length = end - start + 1
                temp -= sequence[end]
                end -= 1
        start -= 1
    return answer