'''
문제 - 전화번호 문자 조합

2에서 9까지 숫자가 주어졌을 때 전화번호로 조합 가능한 모든 문자를 출력하라.
'''
from typing import List

# DFS(재귀) 완전탐색 풀이
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl",
               "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        result = []
        def dfs(i, path):
            if len(path) == len(digits):
                result.append(path)
                return
            for c in phone[digits[i]]:
                 dfs(i + 1, path + c)
        dfs(0, "")
        return result