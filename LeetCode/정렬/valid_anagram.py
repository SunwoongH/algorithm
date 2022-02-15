'''
문제 - 유효한 애너그램

t가 s의 애너그램인지 판별하라.
'''
import collections

# 내장 함수 sorted() 활용 풀이 - 정렬 후 pop() 연산을 진행하면서 값을 비교하는 방식
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        origin = sorted(s)
        test = sorted(t)
        while origin and test:
            if origin.pop() != test.pop():
                return False
        if origin or test:
            return False
        return True
    
# 내장 함수 sorted() 활용 풀이
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# 딕셔너리 풀이
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        table = collections.defaultdict(int)
        for c in s:
            table[c] += 1
        for c in t:
            table[c] -= 1
        return all(value == 0 for value in table.values())