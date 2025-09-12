'''
Created by sunwoong on 2025/09/12
'''
import sys
from collections import defaultdict

def find(a):
    if friends[a] != a:
        friends[a] = find(friends[a])
    return friends[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        friends[b] = a
        counts[a] += counts[b]
        counts[b] = 0
    else:
        friends[a] = b
        counts[b] += counts[a]
        counts[a] = 0

test = int(sys.stdin.readline())
friends = None
counts = None
answers = []

for _ in range(test):
    friends = defaultdict(str)
    counts = defaultdict(int)
    edge = int(sys.stdin.readline())
    for _ in range(edge):
        a, b = sys.stdin.readline().split()
        if a not in friends:
            friends[a] = a
            counts[a] = 1
        if b not in friends:
            friends[b] = b
            counts[b] = 1
        if find(a) != find(b):
            union(a, b)
        count = counts[find(a)]
        answers.append(count)
for answer in answers:
    print(answer)