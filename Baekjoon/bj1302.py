'''
Created by sunwoong on 2022/04/19
'''
import sys
import collections

n, book = int(sys.stdin.readline()), collections.defaultdict(int)
for _ in range(n):
    book[sys.stdin.readline().rstrip()] += 1
print(sorted(book.items(), key=lambda x: (-x[1], x[0]))[0][0])