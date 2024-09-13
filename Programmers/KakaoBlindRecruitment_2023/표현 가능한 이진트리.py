'''
Created by sunwoong on 2024/09/13
'''

def is_valid_binary_tree(number, parent):
    if not number:
        return True
    pos = len(number) // 2
    if number[pos] == '1' and parent == '0':
        return False
    is_valid = True
    is_valid = is_valid_binary_tree(number[:pos], number[pos])
    if not is_valid:
        return is_valid
    is_valid = is_valid_binary_tree(number[pos + 1:], number[pos])
    return is_valid

def solution(numbers):
    count = [1, 3, 7, 15, 31, 63]
    answer = []
    for number in numbers:
        number = str(bin(number))[2:]
        zero = 0
        for i in range(len(count)):
            if count[i] >= len(number):
                zero = count[i] - len(number)
                break
        number = "0" * zero + number
        is_valid = False
        if number[len(number) // 2] == '1':
            is_valid = is_valid_binary_tree(number, '1')
        if is_valid:
            answer.append(1)
        else:
            answer.append(0)
    return answer