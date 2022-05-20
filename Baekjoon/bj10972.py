'''
Created by sunwoong on 2022/05/20
'''
import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

for i in range(n - 1, 0, -1):
    if sequence[i - 1] < sequence[i]:
        for j in range(n - 1, i - 1, -1):
            if sequence[i - 1] < sequence[j]:
                sequence[i - 1], sequence[j] = sequence[j], sequence[i - 1]
                sequence = sequence[:i] + sorted(sequence[i:])
                print(*sequence)
                sys.exit(0)
print(-1)