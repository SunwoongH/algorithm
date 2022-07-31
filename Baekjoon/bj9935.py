'''
Created by sunwoong on 2022/07/31
'''
import sys

curr_string = list(sys.stdin.readline().rstrip())
target = list(sys.stdin.readline().rstrip())
pivot = len(target)
string = []
i = 0
for char in curr_string:
    string.append(char)
    if target[i] == char:
        i += 1
    else:
        i = 0
        if target[i] == char:
            i += 1
    if i == pivot:
        while i > 0:
            string.pop()
            i -= 1
        if string:
            if len(string) >= pivot - 1:
                s_i = -pivot + 1
            else:
                s_i = -len(string)
            while s_i < 0:
                if target[i] == string[s_i]:
                    i += 1
                else:
                    i = 0
                    if target[i] == string[s_i]:
                        i += 1
                s_i += 1
print(''.join(string)) if string else print('FRULA')