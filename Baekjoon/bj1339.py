'''
Created by sunwoong on 2022/12/17 (시간 초과......)
'''
import sys
from itertools import permutations
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
words = []
seen = set()
for _ in range(n):
    word = list(input().rstrip())
    words.append(word)
    seen = seen.union(set(word))
seen = list(seen)
max_total = 0
for items in permutations(range(10), len(seen)):
    table = defaultdict(int)
    for i in range(len(seen)):
        table[seen[i]] = items[i]
    total = 0
    for word in words:
        number = ""
        for char in word:
            number += str(table[char])
        if number[0] == '0':
            if len(number) > 1:
                total += int(number[1:])
        else:
            total += int(number)
    max_total = max(max_total, total)
print(max_total)