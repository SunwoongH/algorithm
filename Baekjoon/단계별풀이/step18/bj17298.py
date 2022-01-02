# -*- coding: cp949 -*- 
# 백준 17298번 오큰수 문제 풀이
# 풀이 방법 - 스택에 값이 아닌 인덱스를 넣어주는 목적으로 사용하여 해결
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
result = [-1] * n
indexStack = []

for i in range(n):
    while indexStack and num[indexStack[-1]] < num[i]:
        result[indexStack.pop()] = num[i]
    indexStack.append(i)

print(*result)