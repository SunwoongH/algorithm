'''
문제 - 보석과 돌

j는 보석이며 s는 갖고 있는 돌이다. s에는 보석이 몇 개나 있을까?
대소문자는 구분한다.
'''
import collections

# 해시 테이블 풀이
class Solution1:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        table = collections.defaultdict(int)
        for stone in stones:
            table[stone] += 1
        count = 0
        for jewel in jewels:
            count += table[jewel]
        return count

# Counter 풀이
class Solution2:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        count = 0
        for jewel in jewels:
            count += freqs[jewel]
        return count

# 리스트 컴프리헨션 풀이
class Solution3:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels for stone in stones)