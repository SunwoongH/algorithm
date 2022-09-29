'''
Created by sunwoong on 2022/09/29
'''
import heapq

def solution(scoville, K):
    length = len(scoville)
    heapq.heapify(scoville)
    count = 0
    while len(scoville) > 1 and scoville[0] < K:
        count += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
    return count if scoville[0] >= K else -1