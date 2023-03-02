'''
Created by sunwoong on 2023/03/02
'''
import sys
input = sys.stdin.readline

def check(t, length):
    if length == len(s):
        if s == t:
            return True
        return False
    if t[-1] == 'A':
        if check(t[:len(t) - 1], length - 1):
            return True
    if t[0] == 'B':
        if check(t[1:][::-1], length - 1):
            return True
    return False

s = input().rstrip()
t = input().rstrip()
print(1) if check(t, len(t)) else print(0)