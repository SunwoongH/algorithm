'''
Created by sunwoong on 2022/04/22
'''
import sys
import collections

n = int(sys.stdin.readline())
cards = collections.defaultdict(int)
for _ in range(n):
    cards[int(sys.stdin.readline())] += 1
print(sorted(cards.items(), key=lambda x: (x[1], -x[0]), reverse=True)[0][0])