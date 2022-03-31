'''
Created by sunwoong on 2022/03/31
'''
import sys

n = int(sys.stdin.readline())
inequality_sign = list(sys.stdin.readline().split())

min_sequence, max_sequence, sequence = sys.maxsize, -sys.maxsize, []
def dfs(position: int) -> None:
    if len(sequence) == n + 1:
        global min_sequence, max_sequence
        temp = int(''.join(map(str, sequence)))
        min_sequence = ''.join(map(str, sequence)) if min(int(min_sequence), temp) == temp else min_sequence
        max_sequence = ''.join(map(str, sequence)) if max(int(max_sequence), temp) == temp else max_sequence
        return
    for num in range(10):
        is_promising = False
        if num not in sequence:
            if inequality_sign[position] == '<' and sequence[-1] < num or inequality_sign[position] == '>' and sequence[-1] > num:
                is_promising = True
            if is_promising:
                sequence.append(num)
                dfs(position + 1)
                sequence.pop()

for num in range(10):
    sequence.append(num)
    dfs(0)
    sequence.pop()
print(max_sequence, min_sequence, sep='\n')