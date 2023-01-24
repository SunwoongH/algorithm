'''
Created by sunwoong on 2023/01/24
'''
import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
words = []
for _ in range(n):
    word = input().rstrip()
    words.append(word)
if k < 5:
    print(0)
    sys.exit(0)
seen = {'a', 'n', 't', 'i', 'c'}
new_seen = set()
parse_words = []
for word in words:
    parse_word = set(word[4:len(word) - 4]).difference(seen)
    parse_words.append(parse_word)
    new_seen = new_seen.union(parse_word)
answer = 0
for case in combinations(new_seen, len(new_seen) if k - 5 > len(new_seen) else k - 5):
    case = set(case)
    count = 0
    for parse_word in parse_words:
        if len(parse_word.difference(case)) == 0:
            count += 1
    answer = max(answer, count)
print(answer)