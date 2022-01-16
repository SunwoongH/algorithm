'''
문제 - 상위 k 빈도 요소

상위 k번 이상 등장하는 요소를 추출하라.
'''
from typing import List
import collections
import heapq

# Counter 풀이
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_table = collections.Counter(nums)
        k_most = count_table.most_common(k)
        result = []
        for value in k_most:
            result.append(value[0])
        return result

# 우선순위 큐(heap) 풀이
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count_table = collections.defaultdict(int)
        for num in nums:
            count_table[num] += 1
        for key, value in count_table.items():
            heapq.heappush(heap, (-value, key))
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

# packing, unpacking 풀이
class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]