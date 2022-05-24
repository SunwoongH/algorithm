'''
Created by sunwoong on 2022/05/24
'''
import sys
import collections

n = int(sys.stdin.readline())
table = collections.defaultdict(bool)
cards = list(map(int, sys.stdin.readline().split()))
for card in cards:
    table[card] = True
    
m = int(sys.stdin.readline())
target_cards = list(map(int, sys.stdin.readline().split()))
for target_card in target_cards:
    if table[target_card]:
        print(1, end=' ')
    else:
        print(0, end=' ')