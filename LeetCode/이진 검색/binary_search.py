'''
문제 - 이진 검색

정렬된 nums를 입력받아 이진 검색으로 target에 해당하는 인덱스를 찾아라.
'''
from typing import List
import bisect

# 이진 검색 풀이 - 반복 구조
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

# 이진 검색 풀이 - 재귀 구조
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left: int, right: int) -> int:
            if left <= right:
                mid = (left + right) // 2
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    return binary_search(left, mid - 1)
                else:
                    return binary_search(mid + 1, right)
            return -1
        return binary_search(0, len(nums) - 1)

# bisect 모듈 활용 풀이
class Solution3:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect.bisect_left(nums, target)
        if i < len(nums) and target == nums[i]:
            return i
        return -1