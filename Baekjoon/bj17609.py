'''
Created by sunwoong on 2022/09/24
'''
import sys
from typing import List

def is_palindrome(sentence: List[str], chance: int) -> int:
    left, right = 0, len(sentence) - 1
    while left < right:
        if sentence[left] == sentence[right]:
            left += 1
            right -= 1
        else:
            if chance:
                check = False
                case_1 = case_2 = 3
                if sentence[left + 1] == sentence[right]:
                    case_1 = is_palindrome(sentence[left + 1:right + 1], 0)
                    check = True
                if sentence[left] == sentence[right - 1]:
                    case_2 = is_palindrome(sentence[left:right], 0)
                    check = True
                if check:
                    return min(case_1, case_2)
                if chance:
                    return 2
            else:
                return 2
    return 0 if chance else 1

n = int(sys.stdin.readline())
for _ in range(n):
    sentence = list(sys.stdin.readline().rstrip())
    print(is_palindrome(sentence, 1))