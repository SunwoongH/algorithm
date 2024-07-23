'''
Created by sunwoong on 2024/07/23
'''
import heapq

def solution(ability, number):
    heap = []
    for score in ability:
        heapq.heappush(heap, score)
    for num in range(number):
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a + b)
        heapq.heappush(heap, a + b)
    return sum(heap)
