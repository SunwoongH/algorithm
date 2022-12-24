'''
Created by sunwoong on 2022/12/24
'''

def solution(s):
    s = sorted(map(int, s.split()))
    return str(s[0]) + ' ' + str(s[-1])