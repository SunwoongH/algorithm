'''
Created by sunwoong on 2023/04/26
'''

def solution(n, s):
    if n > s:
        return [-1]
    element, temp = divmod(s, n)
    elements = [element for _ in range(n)]
    for i in range(len(elements) - 1, len(elements) - 1 - temp, -1):
        elements[i] += 1
    return elements