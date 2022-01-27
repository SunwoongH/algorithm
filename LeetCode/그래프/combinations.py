'''
문제 - 조합

전체 수 n을 입력받아 k개의 조합을 반환하라.
'''
from typing import List
import itertools

# DFS(재귀) 풀이
class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        def dfs(path, start: int):
            if len(path) == k:
                results.append(path)
                return
            for i in range(start, n + 1):
                next_path = path[:]
                next_path.append(i)
                dfs(next_path, i + 1)
        dfs([], 1)
        return results

# DFS(재귀) 풀이
class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()
        dfs([], 1, k)
        return results

# itertools 풀이
class Solution3:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))