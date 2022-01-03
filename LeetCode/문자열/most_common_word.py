'''
<가장 흔한 단어>

금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
대소문자 구분을 하지 않으며, 구두점 또한 무시한다.
'''
from typing import List
import re
import collections

class Solution1:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.split('[^\w]', paragraph)
        most = dict()
        for word in paragraph:
            if word.isalpha():
                if word.lower() not in most:
                    most[word.lower()] = 1
                else:
                    most[word.lower()] += 1
        for remove in banned:
            if remove.lower() in most:
                del most[remove.lower()]
        return max(most, key = most.get)
    
class Solution2:
    def mostCommonWord(self, paragragh: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragragh).lower().split() if word not in banned]
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1
        return max(counts, key = counts.get)