'''
Created by sunwoong 2022/05/12
'''
import sys
import collections

n = int(sys.stdin.readline())
words = collections.defaultdict(int)
for _ in range(n):
    word = sorted(list(sys.stdin.readline().rstrip()))
    words[''.join(word)] += 1
print(len(words.keys()))