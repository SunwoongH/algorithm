'''
Created by sunwoong on 2022/05/16
'''
import sys
import itertools

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
seen = set()
for i in range(1, n + 1):
    for card in itertools.combinations(cards, i):
        seen.add(sum(card))
print(sum(cards) - len(seen))