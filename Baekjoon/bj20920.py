'''
Created by sunwoong on 2022/05/22
'''
import sys

n, m = map(int, sys.stdin.readline().split())
words = dict()
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if word not in words and len(word) >= m:
        words[word] = 1
    elif word in words:
        words[word] += 1
words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for word in words:
    print(word[0], end=' ')