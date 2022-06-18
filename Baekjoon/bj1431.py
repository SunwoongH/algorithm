'''
Created by sunwoong on 2022/06/18
'''
import sys

n = int(sys.stdin.readline())
serial = []
for _ in range(n):
    serial.append(sys.stdin.readline().rstrip())

def sum(element: str) -> int:
    result = 0
    for char in element:
        if char.isdigit():
            result += int(char)
    return result

serial = sorted(serial, key=lambda x: (len(x), sum(x), x))
print(*serial, sep='\n')