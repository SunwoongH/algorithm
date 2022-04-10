'''
Created by sunwoong on 2022/04/10
'''
import sys
import collections
n = int(sys.stdin.readline())
for i in range(n):
    sentence = list(sys.stdin.readline().split())
    stack = collections.deque()
    for char in sentence:
        stack.appendleft(char)
    print(f"Case #{i + 1}:", *stack)