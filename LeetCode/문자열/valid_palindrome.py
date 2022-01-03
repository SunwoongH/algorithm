'''
<유효한 팰린드롬>

주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며,
영문자와 숫자만을 대상으로 한다.
'''
import collections
from typing import Deque
import re

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        input_str = list(s)
        strs = []
        for v in input_str:
            if v.isalpha():
                strs.append(v.lower())
            elif v.isdigit():
                strs.append(v)
        r_strs = strs.copy()
        r_strs.reverse()
        if ''.join(strs) == ''.join(r_strs): return True
        else: return False
        
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True
    
class Solution3:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True
    
class Solution4:
    def isPalindromes(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]