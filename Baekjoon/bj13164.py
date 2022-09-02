'''
Created by sunwoong on 2022/09/02
'''
import sys

n, k = map(int, sys.stdin.readline().split())
students = list(map(int, sys.stdin.readline().split()))
diff = []
for i in range(n - 1, 0, -1):
    diff.append(students[i] - students[i - 1])
diff.sort()
result = students[-1] - students[0]
while k > 1:
    result -= diff.pop()
    k -= 1
print(result)