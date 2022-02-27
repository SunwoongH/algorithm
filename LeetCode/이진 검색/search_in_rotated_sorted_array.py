'''
문제 - 회전 정렬된 배열 검색

특정 피벗을 기준으로 회전하여 정렬된 배열에서 target 값의 인덱스를 출력하라.
'''
from typing import List

# 이진 검색 풀이 - 구간을 먼저 나눈 후 비교
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

# pivot 활용 이진 검색 풀이 - pivot은 회전된 정도를 의미
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)
            if target == nums[mid_pivot]:
                return mid_pivot
            elif target < nums[mid_pivot]:
                right = mid - 1
            else:
                left = mid + 1
        return -1