'''
Created by sunwoong 2022/05/02
'''
import sys
import collections

table = collections.defaultdict(int)
while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    table[tree] += 1
length = sum(table.values())
result = sorted(table.items(), key=lambda x: x[0])
for tree in result:
    print("%s %.4f" %(tree[0], tree[1] / length * 100))