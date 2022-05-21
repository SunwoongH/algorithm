'''
Created by sunwoong on 2022/05/21
'''
import sys
import math

n, m = map(int, sys.stdin.readline().split())
result = math.factorial(n) // (math.factorial(n - m) * math.factorial(m))
print(result)