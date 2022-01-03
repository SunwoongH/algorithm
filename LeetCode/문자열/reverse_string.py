'''
<문자열 뒤집기>

문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며,
반환 없이 리스트 내부를 직접 조작하라.
'''
from typing import List

class Solution1:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        
class Solution2:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1