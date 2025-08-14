'''
Created by sunwoong on 2025/08/14
'''
import sys

n = int(sys.stdin.readline())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [False for _ in range(max(nums, key=lambda x: x[0])[0] + 1)]
visited[0] = True
answer = 0
nums.sort(key=lambda x: -x[1])

for num in nums:
    pos = num[0]
    if not visited[pos]:
        visited[pos] = True
        answer += num[1]
        continue
    while pos > 0 and visited[pos]:
        pos -= 1
    if pos <= 0:
        continue
    visited[pos] = True
    answer += num[1]

print(answer)