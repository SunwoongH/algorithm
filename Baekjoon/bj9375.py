'''
Created by sunwoong on 2022/04/24
'''
import sys, collections, math

n = int(sys.stdin.readline())
for _ in range(n):
    clothes, m = collections.defaultdict(int), int(sys.stdin.readline())
    for _ in range(m):
        _ , kind = sys.stdin.readline().split()
        clothes[kind] += 1
    print(math.prod(map(lambda x: x + 1, clothes.values())) - 1)