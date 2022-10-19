'''
Created by sunwoong on 2022/10/19
'''

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    for i, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            prev_i, _ = stack.pop()
            answer[prev_i] = i - prev_i
        stack.append((i, price))
    while stack:
        prev_i, _ = stack.pop()
        answer[prev_i] = len(prices) - 1 - prev_i
    return answer