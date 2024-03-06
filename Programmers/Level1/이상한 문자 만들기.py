'''
Created by sunwoong on 2024/03/06

풀이 시간 - 40분
'''

def solution(s):
    answer = []
    is_start = False
    i = 0
    temp = []
    blank = []
    for char in s:
        if char.isalpha():
            if not is_start:
                is_start = True
                i = 0
                if blank:
                    answer.append(''.join(blank))
                    blank.clear()
            if i % 2 == 0:
                temp.append(char.upper())
            else:
                temp.append(char.lower())
            i += 1
        else:
            if is_start:
                is_start = False
                answer.append(''.join(temp))
                temp.clear()
            blank.append(' ')
    answer.append(''.join(temp))
    if blank:
        answer.append(''.join(blank))
    return ''.join(answer)

def solution(s):
    s = list(s)
    count = 0
    for i in range(len(s)):
        if s[i] == ' ':
            count = 0
            continue
        if count % 2 == 0:
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
        count += 1
    return ''.join(s)