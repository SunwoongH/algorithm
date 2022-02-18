'''
문제 - 두 배열의 교집합

두 배열의 교집합을 구하라.
'''
from typing import List
import bisect

class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))

# 브루트 포스 풀이 - O(n^2)
class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    result.add(num1)
        return result

# 이진 검색 풀이 - O(nlogn)
class Solution3:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums2.sort()
        for num in nums1:
            i = bisect.bisect_left(nums2, num)
            if i < len(nums2) and num == nums2[i]:
                result.add(num)
        return result

# 정렬 후 투 포인터 풀이 - O(nlogn)
class Solution4:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        return result