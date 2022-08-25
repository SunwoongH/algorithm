'''
Created by sunwoong on 2022/08/25
'''
import sys
from math import log2

k = int(sys.stdin.readline())
string = '00110100110010110'
count = 0
while k > 16:
    count += 1
    if log2(k).is_integer():
        k = k // 2
    else:
        k -= 2 ** int(log2(k))
print(string[k]) if count % 2 == 0 else print(0) if string[k] == '1' else print(1)