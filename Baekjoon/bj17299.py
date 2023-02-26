'''
Created by sunwoong on 2023/02/26
'''
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
answer = [-1 for _ in range(n)]
count = Counter(sequence)
stack = []
max_count = 0
for i in range(n - 1, -1, -1):
    if count[sequence[i]] <= max_count:
        while stack and stack[-1][0] <= count[sequence[i]]:
            stack.pop()
        if stack and stack[-1][0] > count[sequence[i]]:
            answer[i] = sequence[stack[-1][1]]
        stack.append((count[sequence[i]], i))
    else:
        stack = []
        max_count = count[sequence[i]]
        stack.append((count[sequence[i]], i))
print(*answer)