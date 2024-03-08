'''
Created by sunwoong on 2024/03/08

풀이 시간 - 21분
'''
from collections import defaultdict

def solution(s):
    datas = []
    temp = None
    number = None
    is_start = False
    for char in s[1:len(s) - 1]:
        if char == '{':
            temp = []
            number = []
            is_start = True
        if is_start:
            if char.isdigit():
                number.append(char)
            elif char == ",":
                temp.append(int(''.join(number)))
                number = []
            elif char == '}':
                temp.append(int(''.join(number)))
                datas.append(temp)
                is_start = False
    table = defaultdict(int)
    for data in datas:
        for key in data:
            table[key] += 1
    return list(map(lambda x: x[0], sorted(table.items(), key=lambda x: -x[1])))