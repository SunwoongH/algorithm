'''
문제 - 가장 긴 반복 문자 대체

대문자로 구성된 문자열 s가 주어졌을 때 k번만큼의 변경으로 만들 수 있는 연속으로 반복된 문자열의 가장 긴 길이를 출력하라.
'''
import collections

# 투 포인터 & 슬라이딩 윈도우 풀이
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        count_table = collections.Counter()
        for right in range(1, len(s) + 1):
            count_table[s[right - 1]] += 1
            max_count = count_table.most_common(1)[0][1]
            if right - left > max_count + k:
                count_table[s[left]] -= 1
                left += 1
        return right - left