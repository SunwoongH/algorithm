'''
Created by sunwoong on 2022/11/27
'''

def solution(elements):
    answer = set()
    length = len(elements)
    elements = [0] + elements
    elements.extend(elements)
    for i in range(1, len(elements)):
        elements[i] += elements[i - 1]
    interval = 1
    while interval <= length:
        for i in range(length):
            total = elements[i + interval] - elements[i]
            if total not in answer:
                answer.add(total)
        interval += 1
    return len(answer)