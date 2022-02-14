'''
문제 - 가장 큰 수

항목들을 조합하여 만들 수 있는 가장 큰 수를 출력하라.

>>> functools 모듈의 cmp_to_key() 함수와 lambda를 활용해 볼 수 있는 좋은 문제였다.
단순한 조건의 정렬이 아닌 조금 복잡한 정렬을 하기 위해 직접 비교 함수를 구현하고 해당
함수를 cmp_to_key를 통해 키 함수로 변환하여 풀이하였다. 비교 함수는 두 개의 인자를
받아 서로 비교해서 첫 번째 인자가 두 번째 인자보다 작으면 음수, 같으면 0, 크면 양수
를 반환하도록 구현해야한다. 따라서 이러한 특징을 만족하도록 문제에 맞는 조건과 그에 따른
반환 값을 설정하고 sort() 함수의 정렬 조건으로 사용하여 문제를 해결하였다.
'''
from typing import List
import functools

# cmp_to_key 풀이
class Solution1:
    def compare(self, num1: int, num2: int) -> int:
        if int(str(num1) + str(num2)) > int(str(num2) + str(num1)):
            return -1
        return 1
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=functools.cmp_to_key(self.compare))
        return str(int(''.join(map(str, nums))))

# cmp_to_key & lambda 풀이
class Solution2:
    def largestNumber(self, nums: List[int]) -> str:
        compare = lambda x, y: int(str(y) + str(x)) - int(str(x) + str(y))
        nums.sort(key=functools.cmp_to_key(compare))
        return str(int(''.join(map(str, nums))))

# 삽입 정렬 풀이
class Solution3:
    @staticmethod
    def toSwap(num1: int, num2: int) -> bool:
        return str(num1) + str(num2) < str(num2) + str(num1)
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(1, len(nums)):
            j = i
            while j > 0 and self.toSwap(nums[j - 1], nums[j]):
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
        return str(int(''.join(map(str, nums))))