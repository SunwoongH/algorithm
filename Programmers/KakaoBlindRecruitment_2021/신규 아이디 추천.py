'''
Created by sunwoong on 2022/09/16

풀이 시간 - 33분
'''

def solution(new_id):
    is_possible = {'-', '_', '.'}
    step_two = ""
    for char in new_id.lower():
        if char.isalnum() or char in is_possible:
            step_two += char
    step_three = ""
    double_check = 0
    for char in step_two:
        if char == '.':
            double_check += 1
        else:
            if double_check > 0:
                step_three += '.'
                double_check = 0
            step_three += char
    start, end = 0, len(step_three)
    if len(step_three) > 0 and step_three[0] == '.':
        start += 1
    if len(step_three) > 1 and step_three[end - 1] == '.':
        end -=1
    step_after_four = step_three[start:end]
    if not step_after_four:
        step_after_four = "a"
    if len(step_after_four) >= 16:
        step_after_four = step_after_four[:15] if step_after_four[14] != '.' \
                            else step_after_four[:14]
    else:
        if len(step_after_four) <= 2:
            last_char = step_after_four[-1]
            while len(step_after_four) < 3:
                step_after_four += last_char
    return step_after_four