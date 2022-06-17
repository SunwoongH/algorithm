'''
Created by sunwoong on 2022/06/17
'''
import sys

n = int(sys.stdin.readline())
array_a = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
array_b = sorted(list(map(int, sys.stdin.readline().split())))

result = 0
while array_a and array_b:
    result += array_a.pop() * array_b.pop()
print(result)