'''
Created by sunwoong on 2022/07/07
'''
import sys

while True:
    word = sys.stdin.readline().rstrip()
    if word == '*':
        break
    check = True
    for pivot in range(1, len(word) - 1):
        seen = set()
        left, right = 0, pivot
        while right < len(word):
            target = word[left] + word[right]
            if target not in seen:
                seen.add(target)
            else:
                check = False
                break
            left, right = left + 1, right + 1
        if not check:
            break
    if not check:
        print(f'{word} is NOT surprising.')
    else:
        print(f'{word} is surprising.')