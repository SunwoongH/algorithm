'''
문제 - 두 수의 합 Version 2

정렬된 배열을 입력 받아 덧셈하여 target을 만들 수 있는 배열의 두 숫자 인덱스를 반환하라.
'''
from typing import List
import bisect

# bisect 모듈 활용 풀이
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            expected = target - num
            j = bisect.bisect_left(numbers, expected, lo=i + 1, hi=len(numbers) - 1)
            if j < len(numbers) and expected == numbers[j]:
                return [i + 1, j + 1]

# 이진 검색 풀이
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            left, right = i + 1, len(numbers) - 1
            expected = target - num
            while left <= right:
                mid = left + (right - left) // 2
                if expected == numbers[mid]:
                    return [i + 1, mid + 1]
                elif expected < numbers[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

# 투 포인터 풀이
class Solution3:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left != right:
            num = numbers[left] + numbers[right]
            if target == num:
                return [left + 1, right + 1]
            elif target < num:
                right -= 1
            else:
                left += 1

# 딕셔너리 풀이
class Solution4:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        table = {}
        for i, num in enumerate(numbers):
            table[num] = i
        for i, num in enumerate(numbers):
            if target - num in table and i != table[target - num]:
                return [i + 1, table[target - num] + 1]

# 딕셔너리 풀이 - 조회 구조 개선
class Solution5:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        table = {}
        for i, num in enumerate(numbers):
            if target - num in table:
                return [table[target - num] + 1, i + 1]
            table[num] = i