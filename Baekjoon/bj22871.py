'''
Created by sunwoong on 2022/12/19
'''
import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
low, high = 1, 4_999_000_000
while low <= high:
    mid = (low + high) // 2
    visited = [False for _ in range(n)]
    visited[0] = True
    for j in range(1, n):
        for i in range(j):
            if visited[i] and (j - i) * (1 + abs(sequence[j] - sequence[i])) <= mid:
                visited[j] = True
                break
    if visited[n - 1]:
        high = mid - 1
    else:
        low = mid + 1
print(low)