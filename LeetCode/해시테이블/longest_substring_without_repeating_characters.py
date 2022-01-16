'''
문제 - 중복 문자 없는 가장 긴 부분 문자열

중복 문자가 없는 가장 긴 부분 문자열의 길이를 반환하라.
'''

# 투 포인터 풀이
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            left, right = i, i + 1
            cur_length = 1
            while right < len(s) and s[right] not in s[left:right]:
                cur_length += 1
                right += 1
            max_length = max(max_length, cur_length)
        return max_length

# 해시테이블, 가변 슬라이딩 윈도우 풀이
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        max_lenth = start = 0
        for i, char in enumerate(s):
            if char in table and start <= table[char]:
                start = table[char] + 1
            else:
                max_lenth = max(max_lenth, i - start + 1)
            table[char] = i
        return max_lenth