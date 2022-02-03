'''
문제 - 배열의 k번째 큰 요소

정렬되지 않은 배열에서 k번째 큰 요소를 추출하라.
'''
from typing import List
import heapq

# heapq 풀이 - heapify로 힙 특성을 만족하도록 재구축하는 방식
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return heapq.heappop(nums)

# heapq 풀이 - 삽입, 삭제를 반복하는 방식
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, (-num, num))
        result = None
        for _ in range(k):
            result = heapq.heappop(heap)
        return result[1]

# heapq 풀이 - nlargest 함수를 활용한 방식
class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

# 정렬 풀이  
class Solution4:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]