'''
Created by sunwoong on 2025/03/11
'''
import sys
from collections import defaultdict

n = int(sys.stdin.readline())
words = []
weights = defaultdict(int)
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    words.append(word)
    for i in range(len(word)):
        weight = 10 ** (len(word) - i)
        weights[word[i]] += weight
mapping = defaultdict(int)
sorted_weights = sorted(weights.items(), key=lambda x: -x[1])
sequence = 9
for item in sorted_weights:
    mapping[item[0]] = sequence
    sequence -= 1
answer = 0
for word in words:
    value = ""
    for c in word:
        value += str(mapping[c])
    answer += int(value)
print(answer)