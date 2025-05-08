'''
Created by sunwoong on 2025/05/08
'''
import heapq

def solution(ability, number):
    heapq.heapify(ability)
    
    for _ in range(number):
        num1 = heapq.heappop(ability)
        num2 = heapq.heappop(ability)
        heapq.heappush(ability, num1 + num2)
        heapq.heappush(ability, num1 + num2)
    
    return sum(ability)