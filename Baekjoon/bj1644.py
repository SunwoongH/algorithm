'''
Created by sunwoong on 2022/08/27
'''
import sys

n = int(sys.stdin.readline())
sequence = [True for _ in range(n + 1)]
prime_sequence = []
for i in range(2, int(n ** 0.5) + 1):
    if sequence[i] == True:
        j = 2
        while i * j <= n:
            sequence[i * j] = False
            j += 1
for i in range(2, n + 1):
    if sequence[i] == True:
        prime_sequence.append(i)
left = right = 0
target = 0
count = 0
while right < len(prime_sequence):
    target += prime_sequence[right]
    right += 1
    while target > n:
        target -= prime_sequence[left]
        left += 1
    if target == n:
        count += 1
        target -= prime_sequence[left]
        left += 1
print(count)