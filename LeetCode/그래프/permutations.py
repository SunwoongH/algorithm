'''
문제 - 순열

서로 다른 정수를 입력받아 가능한 모든 순열을 반환하라.
'''
from typing import List
import itertools

# DFS(재귀) 풀이
class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(path):
            if len(path) == len(nums):
                result.append(path)
                return
            for num in nums:
                if num not in path:
                    next_path = path[:]
                    next_path.append(num)
                    dfs(next_path)
        dfs([])
        return result

# DFS(재귀) 풀이
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []
        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])
                return
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        dfs(nums)
        return result

# itertools 풀이
class Solution3:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
        #return list(map(list, itertools.permutations(nums)))