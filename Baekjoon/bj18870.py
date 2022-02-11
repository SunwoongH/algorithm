'''
문제 - 좌표 압축

풀이 방법 - 딕셔너리와 enumerate를 활용해 압축된 좌표 결과를 저장하는 mapping 풀이
'''
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
compressed = {}
for i, num in enumerate(sorted(set(nums))):
    compressed[num] = i
print(' '.join(map(str, map(lambda x: compressed[x], nums))))