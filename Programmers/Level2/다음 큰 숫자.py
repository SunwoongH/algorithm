'''
Created by sunwoong on 2023/01/28
'''

def solution(n):
    origin = bin(n).count('1')
    while True:
        n += 1
        if origin == bin(n).count('1'):
            return n