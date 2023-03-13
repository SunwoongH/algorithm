'''
Created by sunwoong on 2023/03/13
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
string = input().rstrip()
seen = set()
count = defaultdict(int)
alpa = None
answer = 0
left = right = 0
while right < len(string):
    seen.add(string[right])
    count[string[right]] += 1
    alpa = len(seen)
    while alpa > n:
        count[string[left]] -= 1
        if count[string[left]] == 0:
            seen.remove(string[left])
            alpa = len(seen)
        left += 1
    answer = max(answer, right - left + 1)
    right += 1
print(answer)