import sys

class Stack:
    def __init__(self):
        self.data = []
        self.top = -1
    
    def isEmpty(self):
        if self.top == -1:
            return 1
        else: return 0

    def size(self):
        return self.top + 1

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
    
    def peek(self):
        if self.isEmpty():
            return -1
        return self.data[self.top]

stack = Stack()

n = int(sys.stdin.readline())

for i in range(0, n):
    choice = list(map(str, sys.stdin.readline().split()))
    if choice[0] == 'push':
        num = int(choice[1])
        stack.push(num)
    elif choice[0] == 'top':
        print(stack.peek())
    elif choice[0] == 'size':
        print(stack.size())
    elif choice[0] == 'empty':
        print(stack.isEmpty())
    elif choice[0] == 'pop':
        print(stack.pop())