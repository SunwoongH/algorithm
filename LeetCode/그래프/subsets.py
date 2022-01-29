'''
문제 - 부분 집합

모든 부분 집합을 반환하라.
'''
from typing import List

# DFS(재귀) 풀이
class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        def dfs(start, path, case):
            if len(path) == case:
                results.append(path[:])
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path, case)
                path.pop()
        for case in range(len(nums)):
            dfs(0, [], case + 1)
        return results

# DFS(재귀) 풀이
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        def dfs(start, path):
            results.append(path)
            for i in range(start, len(nums)):
                dfs(i + 1, path + [nums[i]])
        dfs(0, [])
        return results