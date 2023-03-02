'''
Created by sunwoong on 2023/03/02
'''

def palindrome(s, pos, is_odd):
    left = pos - 1
    right = pos + 1 if is_odd else pos + 2
    length = 1 if is_odd else 2
    while 0 <= left and right < len(s) and s[left] == s[right]:
        length += 2
        left -= 1
        right += 1
    return length

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer = max(answer, palindrome(s, i, True))
        if i == len(s) - 1 or s[i] != s[i + 1]:
            continue
        answer = max(answer, palindrome(s, i, False))
    return answer