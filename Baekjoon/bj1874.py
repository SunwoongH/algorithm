import sys

n = int(sys.stdin.readline())
sequence = []
stack = [0]
result = []

for i in range(n):
    sequence.append(int(sys.stdin.readline()))

num = 1
check = True
for i in range(n):
    if stack[-1] < sequence[i]:
        while stack[-1] < sequence[i]:
            stack.append(num)
            result.append('+')
            num += 1
    elif stack[-1] > i:
        while stack[-1] > sequence[i]:
            stack.pop()
            result.append('-')
    temp = stack.pop()
    if temp != sequence[i]: 
        check = False
        print('NO')
        break
    result.append('-')

if check:
    for i in result:
        print(i)