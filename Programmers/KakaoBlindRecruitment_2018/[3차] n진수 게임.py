'''
Created by sunwoong on 2025/01/14

'''

def convert(n, num):
    if num == 0:
        return str(0)
    table = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    new_num = []
    value = num
    while value != 0:
        value, mod = divmod(value, n)
        if mod in table:
            new_num.append(str(table[mod]))
        else:
            new_num.append(str(mod))
    new_num.reverse()
    return ''.join(new_num)

def solution(n, t, m, p):
    answer = ''
    
    sequence = ""
    num = 0
    while len(sequence) < 1000 * 100:
        sequence += convert(n, num)
        num += 1
    for i in range(p - 1, len(sequence), m):
        answer += sequence[i]
        if len(answer) == t:
            break    
    
    return answer