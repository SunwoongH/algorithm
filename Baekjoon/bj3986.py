'''
Created by sunwoong 2022/04/30
'''
import sys

n = int(sys.stdin.readline())
result = 0
for _ in range(n):
    word = list(sys.stdin.readline().rstrip())
    stack = []
    for char in word:
        if not stack or stack[-1] != char:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
    if not stack:
        result += 1
print(result)