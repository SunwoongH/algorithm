'''
문제 - 색 정렬

빨간색을 0, 흰색을 1, 파란색을 2라 할 때 순서대로 인접하는 제자리(in-place) 정렬을 수행하라.

>>> 처음에는 간단히 오름차순 정렬을 수행하는 문제로 판단하고 쉽게 풀이하였다. 그러나 이 문제는 퀵 정렬의
활용에 대해서 배울 수 있는 좋은 문제였다. 일반적인 퀵 정렬은 pivot을 기준으로 두 부분 분할하여 정렬을 수행하는 
알고리즘이다. 이러한 퀵 정렬의 특징에서 분할하는 부분을 늘리는 개선 방안을 생각해 볼 수 있다. 즉, 주어진 문제에서
0, 1, 2를 각각의 부분으로 분할하여 정렬하는 것이다. 정렬을 위해 총 세 개의 포인터가 필요하며 red는 1 구간의 시작 위치,
blue는 2 구간의 시작 위치를 가리키도록 하고 white 포인터로 순차 탐색을 진행하며 white가 가리키는 요소의 값에 따라서
red 혹은 blue가 가리키는 요소와 swap하는 방식으로 O(n)에 정렬이 가능한 풀이이다.
'''
from typing import List

# 내장 함수 sort() 활용 풀이
class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()

# 삽입 정렬 풀이
class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            j = i - 1
            target = nums[i]
            while j >= 0 and target < nums[j]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
                j -= 1
            nums[j + 1] = target

# 퀵 정렬 풀이 - 기존 퀵 정렬의 두 부분 분할을 세 부분 분할로 개선한 방식
class Solution3:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)
        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue -= 1
                nums[blue], nums[white] = nums[white], nums[blue]
            else:
                white += 1