'''
Created by sunwoong on 2022/04/20
'''
import sys

n, m = map(int, sys.stdin.readline().split())
table = dict()
for _ in range(n):
    address, password = sys.stdin.readline().split()
    table[address] = password
for _ in range(m):
    print(table[sys.stdin.readline().rstrip()])