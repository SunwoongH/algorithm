'''
Created by sunwoong on 2025/08/11
'''
import sys
import heapq

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
if n == 1:
    print(0)
else:
    answer = 0
    heapq.heapify(nums)

    while len(nums) > 1:
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        answer += a + b
        heapq.heappush(nums, a + b)
    
    print(answer)