'''
Created by sunwoong on 2024/03/15

풀이 시간 - 70분
'''

def solution(new_id):
    patterns = ['-', '_', '.']
    answer = list(new_id)
    #1단계
    for i in range(len(answer)):
        if answer[i].isupper():
            answer[i] = answer[i].lower()
    #2단계
    new_answer = []
    for char in answer:
        if not char.isalpha() and not char.isdigit() and char not in patterns:
            continue
        new_answer.append(char)
    answer = new_answer
    #3단계
    flag = False
    new_answer = []
    for char in answer:
        if not flag:
            if char == '.':
                flag = True
                new_answer.append('.')
                continue
            new_answer.append(char)
        else:
            if char != '.':
                new_answer.append(char)
                flag = False
    answer = new_answer
    #4단계
    if len(answer) > 1:
        if answer[0] == '.' and answer[-1] == '.':
            answer = answer[1:len(answer) - 1]
        else:
            if answer[0] == '.':
                answer = answer[1:len(answer)]
            elif answer[-1] == '.':
                answer = answer[:len(answer) - 1]
    elif len(answer) == 1 and answer[0] == '.':
        answer = []
    #5단계
    if len(answer) == 0:
        answer.append('a')
    #6단계
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer.pop()
    #7단계
    if len(answer) <= 2:
        char = answer[-1]
        answer.extend([char for _ in range(3 - len(answer))])
    return ''.join(answer)