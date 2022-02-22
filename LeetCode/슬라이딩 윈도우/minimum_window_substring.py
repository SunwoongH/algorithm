'''
문제 - 부분 문자열이 포함된 최소 윈도우

문자열 s와 t를 입력받아 O(n)에 t의 모든 문자가 포함된 s의 최소 윈도우를 찾아라.
'''
import collections

# 브루트 포스 풀이 - 시간 초과
class Solution1:
    def minWindow(self, s: str, t: str) -> str:
        for k in range(len(t) - 1, len(s)):
            start, end = 0, k
            while end <= len(s) - 1:
                temp = list(t)
                for i in range(start, end + 1):
                    if s[i] in temp:
                        temp.remove(s[i])
                if not temp:
                    return s[start:end + 1]
                start += 1
                end += 1
        return ""

# 투 포인터 & 슬라이딩 윈도우 풀이
class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = right = start = end = 0
        while right < len(s):
            missing -= need[s[right]] > 0
            need[s[right]] -= 1
            if not missing:
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if not end or right + 1 - left < end - start:
                    start, end = left, right + 1
                need[s[left]] += 1
                missing += 1
                left += 1
            right += 1
        return s[start:end]

# Counter 활용 풀이
class Solution3:
    def minWindow(self, s: str, t: str) -> str:
        t_count = collections.Counter(t)
        current_count = collections.Counter()
        start = end = 0
        left = 0
        for right, char in enumerate(s, 1):
            current_count[char] += 1
            while current_count & t_count == t_count:
                if not end or right - left < end - start:
                    start, end = left, right
                current_count[s[left]] -= 1
                left += 1
        return s[start:end]