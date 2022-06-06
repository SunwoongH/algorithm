'''
Created by sunwoong on 2022/06/06
'''
import sys
import collections

n = int(sys.stdin.readline())
cards = collections.deque([num for num in range(1, n + 1)])
result = []
while len(cards) > 1:
    result.append(cards.popleft())
    cards.append(cards.popleft())
print(*result, cards[0], sep=' ')