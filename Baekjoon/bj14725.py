'''
Created by sunwoong on 2023/04/01
'''
import sys
input = sys.stdin.readline

layer = "--"
n = int(input())
info = []
for _ in range(n):
    data = input().rstrip()
    info.append(data)
info.sort(key=lambda x: x[2:])
root = None
prev = None
for i in range(n):
    data = info[i].split()
    if root is None:
        root = data[1]
        print(root)
    elif root != data[1]:
        root = data[1]
        print(root)
        prev = None
    check = False
    for j in range(2, int(data[0]) + 1):
        if not check:
            if prev is not None and prev[j] == data[j]:
                continue
            else:
                check = True
        print(layer * (j - 1) + data[j])
    prev = data