'''
Created by sunwoong on 2022/04/11
'''
import sys

test = int(sys.stdin.readline())
for _ in range(test):
    h, w, n = map(int, sys.stdin.readline().split())
    floor, room = (h, n // h) if n % h == 0 else (n % h, n // h + 1)
    print(f'{floor}0{room}' if room < 10 else f'{floor}{room}')