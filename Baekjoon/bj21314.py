'''
Created by sunwoong on 2022/08/09
'''
import sys

string = sys.stdin.readline().rstrip()
max_num, min_num = '', ''

n = 0
for char in string:
    if char == 'K':
        max_num += str(10 ** n * 5)
        min_num += str(10 ** n + 5) if n != 0 else '5'
        n = 0
        continue
    n += 1
if n:
    max_num += '1' * n
    min_num += str(10 ** (n - 1))
        
print(max_num, min_num, sep='\n')