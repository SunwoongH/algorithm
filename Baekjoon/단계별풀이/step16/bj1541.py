import sys
expression = list(sys.stdin.readline().rstrip('\n'))
start = 0
result_expression = []
for i in range(len(expression)):
    if expression[i] == '+' or expression[i] == '-':
        temp = ''.join(expression[start:i])
        start = i + 1
        result_expression.append(temp)
        result_expression.append(expression[i])
result_expression.append(''.join(expression[start:]))
result = 0
is_sub = False
temp = 0

for data in result_expression:
    if data.isdigit():
        if is_sub:
            temp += int(data)
        else:
            result += int(data)
    else:
        if data == '-' and is_sub:
            result -= temp
            temp = 0
        elif data == '-': is_sub = True
result -= temp
print(result)