'''
Created by sunwoong on 2022/04/28
'''
import sys

a, b = map(int, sys.stdin.readline().split())
a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))
print(len(a ^ b))