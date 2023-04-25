'''
Created by sunwoong on 2023/04/25
'''

def solution(numbers):
    stack = []
    answer = [-1 for _ in range(len(numbers))]
    for i, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            j = stack.pop()
            answer[j] = number
        stack.append(i)
    return answer