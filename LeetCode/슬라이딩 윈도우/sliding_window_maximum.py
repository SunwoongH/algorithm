'''
문제 - 최대 슬라이딩 윈도우

배열 nums가 주어졌을 때 k 크기의 슬라이딩 윈도우를 오른쪽 끝까지 이동하면서 최대 슬라이딩 윈도우를 구하라.

>>> 처음 시도한 풀이는 투 포인터로 슬라이딩 윈도우를 이동하면서 이전 슬라이딩 윈도우 최댓값의 위치에 따라 조건을 나눈 후 다음 
슬라이딩 윈도우 최댓값을 계산하는 과정을 달리하여 풀이하였으나 시간 초과가 발생하였다. 만약 nums가 내림차순으로 주어진 경우 
매번 슬라이딩 윈도우 전체에서 최댓값을 계산해야 하기 때문에 O(k * n)의 시간이 걸리게 되어 시간 초과가 발생했다고 판단된다. 
따라서 최댓값 계산 과정을 최적화 해야하며 deque를 활용하여 유효한 값만을 저장하는 방식으로 해결하였다.
'''
from typing import List
import collections

# 투 포인터 풀이 - 시간 초과
class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        left, right = 0, k - 1
        start = True
        while right != len(nums):
            check = False
            if start:
                start = False
                max_i = nums.index(max(nums[left:right + 1]))
            else:
                if max_i == left - 1:
                    check = True
                if check:
                    new_max_i = right
                    if nums[max_i] > nums[new_max_i]:
                        max_i = new_max_i
                        for i in range(right - 1, left - 1, -1):
                            if nums[max_i] < nums[i]:
                                max_i = i
                    else:
                        max_i = new_max_i
                else:
                    if nums[max_i] <= nums[right]:
                        max_i = right
            results.append(nums[max_i])
            left += 1
            right += 1
        return results

# deque 활용 풀이 - O(n)
class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        for i, num in enumerate(nums):
            if window and i - window[0] == k:
                window.popleft()
            while window and nums[window[-1]] <= num:
                window.pop()
            window.append(i)
            if i + 1 >= k:
                results.append(nums[window[0]])
        return results