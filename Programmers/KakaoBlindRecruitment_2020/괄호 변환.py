'''
Created by sunwoong on 2024/06/17

풀이 시간 - 60분
'''

trans = {'(': ')', ')': '('}

def is_correct_by(str):
    stack = []
    is_correct = True
    for char in str:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                is_correct = False
                break
            else:
                stack.pop()
    return is_correct

def find_split_idx(str):
    u = v = ""
    left = right = 0
    for i in range(len(str)):
        if str[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return i
    return None

def convert(str):
    if str == "":
        return str
    is_correct = is_correct_by(str)
    if is_correct:
        return str
    u = v = ""
    i = find_split_idx(str)
    u += str[:i + 1]
    if i < len(str) - 1:
        v += str[i + 1:]
    is_correct = is_correct_by(u)
    if is_correct:
        u += convert(v)
        return u
    new = "(" + convert(v) + ")"
    trans_u = ''.join(list(map(lambda x: trans[x], u[1:len(u) - 1])))
    new += trans_u
    return new

def solution(p):
    return convert(p)