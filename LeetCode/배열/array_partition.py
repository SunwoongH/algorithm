'''
문제 - 배열 파티션 1

n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
'''
from typing import List

class Solution1:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            sum += min(nums[i], nums[i + 1])
        return sum
    
class Solution2:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()
        for num in nums:
            pair.append(num)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        return sum
    
class Solution3:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n
        return sum
    
class Solution4:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])