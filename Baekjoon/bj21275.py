'''
Created by sunwoong on 2022/08/10
'''
import sys
from typing import List

def calculate_max_notation(string: str) -> int:
    result = 1
    for char in string:
        if char.isdigit():
            result = max(result, int(char) + 1)
        else:
            result = max(result, ord(char) - 87 + 1)
    return result

def compare_decimal_notation(a: str, b: str, max_a: int, max_b: int) -> List:
    result = []
    for i in range(max_a, 37):
        temp_a = 0
        count = len(a) - 1
        for char in a:
            if char.isdigit():
                temp_a += int(char) * (i ** count)
            else:
                temp_a += (ord(char) - 87) * (i ** count)
            count -= 1
        for j in range(max_b, 37):
            temp_b = 0
            count = len(b) - 1
            for char in b:
                if char.isdigit():
                    temp_b += int(char) * (j ** count)
                else:
                    temp_b += (ord(char) - 87) * (j ** count)
                count -= 1
            if temp_a == temp_b and i != j and temp_a < 2 ** 63 and temp_b < 2 ** 63:
                result.append((temp_a, i, j))
    return result

a, b = map(str, sys.stdin.readline().split())
max_a = calculate_max_notation(a)
max_b = calculate_max_notation(b)
result = compare_decimal_notation(a, b, max_a, max_b)
print('Impossible') if not result else print('Multiple') if len(result) > 1 else print(*result[0])