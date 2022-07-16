'''
Created by sunwoong on 2022/07/16
'''
import sys

n = int(sys.stdin.readline())
word = list(sys.stdin.readline().rstrip())
blue = red = 0
is_blue = False
for i in range(len(word)):
    if i == 0:
        if word[i] == 'B':
            is_blue = True
            blue += 1
        else:
            red += 1
    elif word[i] == 'B':
        if is_blue:
            continue
        else:
            is_blue = True
            blue += 1
    else:
        if not is_blue:
            continue
        else:
            is_blue = False
            red += 1
print(min(blue, red) + 1)