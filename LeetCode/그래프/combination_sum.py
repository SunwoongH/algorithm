'''
문제 - 조합의 합

숫자 집합 candidates를 조합하여 합이 target이 되는 원소를 나열하라.
각 원소는 중복으로 나열 가능하다.
'''
from typing import List

# DFS(재귀) 풀이
class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def dfs(sum_elements, start, path):
            if sum_elements == target:
                results.append(path[:])
            elif sum_elements > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(sum_elements + candidates[i], i, path)
                path.pop()
        dfs(0, 0, [])
        return results

# DFS(재귀) 풀이
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def dfs(csum, start, path):
            if csum < 0:
                return
            elif csum == 0:
                results.append(path)
                return
            for i in range(start, len(candidates)):
                dfs(csum - candidates[i], start, path + [candidates[i]])
        dfs(target, 0, [])
        return results