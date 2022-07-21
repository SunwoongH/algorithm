'''
Created by sunwoong on 2022/07/21
'''
from math import factorial

n = int(input())
nums = list(str(factorial(n)))[::-1]
count = 0
check = False
for num in nums:
    if check:
        break
    elif num == '0':
        count += 1
    else:
        check = True
print(count)