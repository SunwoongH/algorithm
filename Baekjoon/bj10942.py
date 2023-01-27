'''
Created by sunwoong on 2023/01/27
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
palindrome_table = defaultdict(bool)
for pivot in range(n):
    left, right = pivot - 1, pivot + 1
    while left >= 0 and right < n:
        if sequence[left] == sequence[right]:
            palindrome_table[(left, right)] = True
            left -= 1
            right += 1
        else:
            break
    palindrome_table[(pivot, pivot)] = True
for pivot in range(n - 1):
    left, right = pivot, pivot + 1
    while left >= 0 and right < n:
        if sequence[left] == sequence[right]:
            palindrome_table[(left, right)] = True
            left -= 1
            right += 1
        else:
            break
question = int(input())
for _ in range(question):
    i, j = map(int, input().split())
    if palindrome_table[(i - 1, j - 1)]:
        print(1)
    else:
        print(0)