import sys

class Stack:
    def __init__(self):
        self.data = []
        self.top = -1
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else: return False

    def push(self, data):
        self.data.append(data)
        self.top += 1
    
    def pop(self):
        if self.isEmpty():
            return -1
        removed = self.data[self.top]
        del self.data[self.top]
        self.top -= 1
        return removed


data = []
while True:
    inputData = sys.stdin.readline().strip('\n')
    if inputData == '.': break
    data.append(inputData)

for d in data:
    check = True
    stack = Stack()
    for i in range(len(d)):
        if d[i] == '(' or d[i] == '[':
            stack.push(d[i])
        elif d[i] == ')':
            result = stack.pop()
            if result != '(':
                check = False
        elif d[i] == ']':
            result = stack.pop()
            if result != '[':
                check = False
    if not stack.isEmpty():
        check = False
    if check == True:
        print('yes')
    else:
        print('no')