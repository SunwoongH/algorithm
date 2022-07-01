'''
Created by sunwoong on 2022/07/02
'''
import sys
import collections

n, m = map(int, sys.stdin.readline().split())
table = collections.defaultdict(list)
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    table[word[0]].append(word)
count = 0
for _ in range(m):
    target = sys.stdin.readline().rstrip()
    if target[0] in table:
        for word in table[target[0]]:
            if target == word[:len(target)]:
                count += 1
                break
print(count)