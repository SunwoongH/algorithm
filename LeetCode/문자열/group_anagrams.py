'''
<그룹 애너그램>

문자열 배열을 받아 애너그램 단위로 그룹핑하라.
'''
from typing import List
import collections

# 풀이 실패 - 시간초과
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        while strs:
            pos = 0
            temp = []
            temp.append(strs[pos])
            c_word1 = ''.join(sorted(strs[pos]))
            strs.remove(strs[pos])
            while pos < len(strs):
                c_word2 = ''.join(sorted(strs[pos]))
                if c_word1 == c_word2:
                    temp.append(strs[pos])
                    strs.remove(strs[pos])
                else:
                    pos += 1
            result.append(temp[:])
            temp.clear()
        return result

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())