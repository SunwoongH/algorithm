'''
Created by sunwoong on 2023/05/29
'''
import sys
input = sys.stdin.readline

n = int(input())
position = list(map(int, input().split()))
position.sort()
print(position[(n - 1) // 2])