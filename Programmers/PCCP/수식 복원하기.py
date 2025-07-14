'''
Created by sunwoong on 2025/07/15
'''

def n_to_ten(n, value):
    return int(value, n)

def ten_to_n(n, value):
    result = []
    while value > 0:
        value, num = divmod(value, n)
        result.append(str(num))
    if not result:
        return 0
    result.reverse()
    return int(''.join(result))
    
def solution(expressions):
    hint = []
    answer = []
    
    start = 0
    
    for e in expressions:
        num1, oper, num2, _, result = e.split(' ')
        
        for i in range(len(num1)):
            start = max(start, int(num1[i]))
        for i in range(len(num2)):
            start = max(start, int(num2[i]))
        
        if result != 'X':
            for i in range(len(result)):
                start = max(start, int(result[i]))
            hint.append(e)
        else:
            answer.append(e)
            
    promising = []
        
    for n in range(start + 1, 10):
        is_promising = True
        for h in hint:
            num1, oper, num2, _, result = h.split(' ')
            if oper == '+' and n_to_ten(n, num1) + n_to_ten(n, num2) != n_to_ten(n, result):
                is_promising = False
                break
            if oper == '-' and n_to_ten(n, num1) - n_to_ten(n, num2) != n_to_ten(n, result):
                is_promising = False
                break
        if is_promising:
            promising.append(n)
    
    result = []
    for a in answer:
        num1, oper, num2, _, _ = a.split(' ')
        valid = set()
        for n in promising:
            if oper == '+':
                total = n_to_ten(n, num1) + n_to_ten(n, num2)
                valid.add(ten_to_n(n, total))
            if oper == '-':
                total = n_to_ten(n, num1) - n_to_ten(n, num2)
                valid.add(ten_to_n(n, total))
        if len(valid) == 1:
            result.append(num1 + ' ' + oper + ' ' + num2 + ' = ' + str(valid.pop()))
        else:
            result.append(num1 + ' ' + oper + ' ' + num2 + ' = ?')
    
    return result