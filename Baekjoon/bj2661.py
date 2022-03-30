'''
Created by sunwoong on 2022/03/30
'''
import sys

n = int(sys.stdin.readline())
sequence = []

def promising() -> bool:
    left, right = 0 if len(sequence) % 2 == 0 else 1, len(sequence) - len(sequence) // 2
    for gap in range(len(sequence) // 2, 0, -1):
        if left >= 0 and sequence[left:left + gap] == sequence[right:right + gap]:
            return False
        left, right = left + 2, right + 1
    return True

def dfs() -> None:
    if len(sequence) == n:
        print(''.join(map(str, sequence)))
        sys.exit(0)
    for num in [1, 2, 3]:
        sequence.append(num)
        if promising():
            dfs()
        sequence.pop()
dfs()